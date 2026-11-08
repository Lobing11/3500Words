#!/usr/bin/env python3
"""Local Windows desktop server for 3500Words quiz — same curated JSON as mobile."""

from __future__ import annotations

import json
import os
import sys
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from quiz_core import build_session, grade

ROOT = Path(__file__).resolve().parents[1]
CURATED = ROOT / "content" / "curated"
WEB = Path(__file__).resolve().parent / "web"
DATA_DIR = Path(os.environ.get("LOCALAPPDATA", str(Path.home()))) / "Words3500"
WRONG_PATH = DATA_DIR / "wrong_book.json"
HOST = "127.0.0.1"
PORT = 8765


def ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not WRONG_PATH.exists():
        WRONG_PATH.write_text('{"ids":[]}\n', encoding="utf-8")


def load_wrong_ids() -> list[str]:
    ensure_data_dir()
    try:
        data = json.loads(WRONG_PATH.read_text(encoding="utf-8"))
        return list(data.get("ids") or [])
    except Exception:
        return []


def save_wrong_ids(ids: list[str]) -> None:
    ensure_data_dir()
    # preserve order, unique
    seen: set[str] = set()
    ordered: list[str] = []
    for i in ids:
        if i and i not in seen:
            seen.add(i)
            ordered.append(i)
    WRONG_PATH.write_text(
        json.dumps({"ids": ordered}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("[desktop] " + (fmt % args) + "\n")

    def _send_json(self, obj, status: int = 200) -> None:
        raw = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0:
            return {}
        body = self.rfile.read(length)
        return json.loads(body.decode("utf-8"))

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/health":
            self._send_json({"ok": True, "curated": str(CURATED)})
            return

        if path == "/api/manifest":
            man = json.loads((CURATED / "manifest.json").read_text(encoding="utf-8"))
            self._send_json(man)
            return

        if path.startswith("/api/unit/"):
            unit_id = path.split("/api/unit/", 1)[1].strip("/")
            man = json.loads((CURATED / "manifest.json").read_text(encoding="utf-8"))
            file_name = None
            for u in man.get("units", []):
                if str(u.get("unitId")) == unit_id:
                    file_name = u.get("file")
                    break
            if not file_name:
                self._send_json({"error": "unit not found"}, 404)
                return
            unit_path = CURATED / file_name
            if not unit_path.exists():
                self._send_json({"error": "content missing", "file": file_name}, 404)
                return
            data = json.loads(unit_path.read_text(encoding="utf-8"))
            self._send_json(data)
            return

        if path == "/api/wrong":
            self._send_json({"ids": load_wrong_ids()})
            return

        if path == "/api/session":
            qs = parse_qs(parsed.query)
            unit_id = (qs.get("unitId") or [""])[0]
            mode = (qs.get("mode") or ["mixed"])[0]
            segment = (qs.get("segment") or ["all"])[0]
            count = int((qs.get("count") or ["25"])[0])
            man = json.loads((CURATED / "manifest.json").read_text(encoding="utf-8"))
            file_name = None
            for u in man.get("units", []):
                if str(u.get("unitId")) == unit_id:
                    file_name = u.get("file")
                    break
            if not file_name or not (CURATED / file_name).exists():
                self._send_json({"error": "unit content missing"}, 404)
                return
            bank = json.loads((CURATED / file_name).read_text(encoding="utf-8"))
            items = build_session(
                bank.get("items") or [],
                mode=mode,
                segment=segment,
                wrong_ids=set(load_wrong_ids()),
                count=count,
            )
            self._send_json({"items": items, "unit": bank.get("name", unit_id)})
            return

        super().do_GET()

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        path = parsed.path
        data = self._read_json()

        if path == "/api/grade":
            item = data.get("item") or {}
            user_input = str(data.get("input") or "")
            verdict = grade(item, user_input)
            ids = load_wrong_ids()
            item_id = str(item.get("id") or "")
            if verdict in ("wrong", "partial"):
                if item_id and item_id not in ids:
                    ids.append(item_id)
                    save_wrong_ids(ids)
            elif verdict == "correct" and item_id in ids:
                ids = [i for i in ids if i != item_id]
                save_wrong_ids(ids)
            self._send_json(
                {
                    "verdict": verdict,
                    "answerPrimary": item.get("answerPrimary", ""),
                    "answerAlts": item.get("answerAlts") or [],
                    "wrongCount": len(load_wrong_ids()),
                }
            )
            return

        if path == "/api/wrong/clear":
            save_wrong_ids([])
            self._send_json({"ids": []})
            return

        self._send_json({"error": "not found"}, 404)


def main() -> None:
    if not CURATED.exists():
        print(f"ERROR: curated content not found: {CURATED}")
        sys.exit(1)
    ensure_data_dir()
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    url = f"http://{HOST}:{PORT}/"
    print(f"3500Words Desktop  ->  {url}")
    print(f"Content            ->  {CURATED}")
    print(f"Wrong book         ->  {WRONG_PATH}")
    print("Press Ctrl+C to stop.")
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
