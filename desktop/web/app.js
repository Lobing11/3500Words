(() => {
  const homeView = document.getElementById("homeView");
  const quizView = document.getElementById("quizView");
  const doneView = document.getElementById("doneView");
  const unitSelect = document.getElementById("unitSelect");
  const segmentSelect = document.getElementById("segmentSelect");
  const modeSelect = document.getElementById("modeSelect");
  const countSelect = document.getElementById("countSelect");
  const unitHint = document.getElementById("unitHint");
  const wrongBadge = document.getElementById("wrongBadge");
  const promptText = document.getElementById("promptText");
  const hintText = document.getElementById("hintText");
  const answerInput = document.getElementById("answerInput");
  const progressText = document.getElementById("progressText");
  const modeTag = document.getElementById("modeTag");
  const resultBox = document.getElementById("resultBox");
  const nextBtn = document.getElementById("nextBtn");
  const summaryText = document.getElementById("summaryText");

  let units = [];
  let session = [];
  let index = 0;
  let graded = false;
  let correctCount = 0;
  let partialCount = 0;
  let wrongCountRound = 0;

  async function api(path, options) {
    const res = await fetch(path, options);
    const data = await res.json();
    if (!res.ok) throw new Error(data.error || res.statusText);
    return data;
  }

  function show(view) {
    homeView.classList.toggle("hidden", view !== "home");
    quizView.classList.toggle("hidden", view !== "quiz");
    doneView.classList.toggle("hidden", view !== "done");
  }

  function selectedUnit() {
    return units.find((u) => u.unitId === unitSelect.value);
  }

  function refreshUnitHint() {
    const u = selectedUnit();
    if (!u) {
      unitHint.textContent = "";
      return;
    }
    if (!u.hasContent) {
      unitHint.textContent = "该 Unit 内容尚未入库，请先选择已有内容的 Unit（当前可用：有「已入库」标记的项）。";
      document.getElementById("startBtn").disabled = true;
      return;
    }
    document.getElementById("startBtn").disabled = false;
    const range = u.rangeFrom && u.rangeTo ? `（${u.rangeFrom}—${u.rangeTo}）` : "";
    unitHint.textContent = `${u.name}${range} · 与手机端同一份 JSON`;
  }

  async function refreshWrongBadge() {
    const data = await api("/api/wrong");
    wrongBadge.textContent = `错题 ${data.ids.length}`;
  }

  async function loadManifest() {
    const man = await api("/api/manifest");
    units = (man.units || []).slice().sort((a, b) => a.order - b.order);
    unitSelect.innerHTML = "";
    for (const u of units) {
      const opt = document.createElement("option");
      opt.value = u.unitId;
      opt.textContent = u.hasContent ? `${u.name} · 已入库` : `${u.name} · 待入库`;
      if (!u.hasContent) opt.disabled = false;
      unitSelect.appendChild(opt);
    }
    const firstReady = units.find((u) => u.hasContent);
    if (firstReady) unitSelect.value = firstReady.unitId;
    refreshUnitHint();
    await refreshWrongBadge();
  }

  function renderQuestion() {
    const item = session[index];
    graded = false;
    nextBtn.disabled = true;
    resultBox.className = "result hidden";
    resultBox.textContent = "";
    answerInput.value = "";
    answerInput.focus();
    progressText.textContent = `${index + 1} / ${session.length}`;
    modeTag.textContent = item.type || "";
    promptText.textContent = item.prompt || "";
    hintText.textContent = item.hint ? `提示：${item.hint}` : "";
  }

  async function startSession() {
    const u = selectedUnit();
    if (!u || !u.hasContent) return;
    const mode = modeSelect.value;
    const segment = segmentSelect.value;
    const count = countSelect.value;
    const data = await api(
      `/api/session?unitId=${encodeURIComponent(u.unitId)}&mode=${encodeURIComponent(mode)}&segment=${encodeURIComponent(segment)}&count=${encodeURIComponent(count)}`
    );
    session = data.items || [];
    if (!session.length) {
      unitHint.textContent = "当前筛选下没有题目（可能是错题本为空，或该分段尚无对应考点）。";
      return;
    }
    index = 0;
    correctCount = 0;
    partialCount = 0;
    wrongCountRound = 0;
    show("quiz");
    renderQuestion();
  }

  async function checkAnswer(revealOnly) {
    const item = session[index];
    if (!item) return;
    if (revealOnly) {
      resultBox.className = "result";
      resultBox.textContent = `参考答案：${item.answerPrimary}${(item.answerAlts || []).length ? " ｜ 也可：" + item.answerAlts.join(" / ") : ""}`;
      graded = true;
      nextBtn.disabled = false;
      return;
    }
    const data = await api("/api/grade", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ item, input: answerInput.value }),
    });
    graded = true;
    nextBtn.disabled = false;
    wrongBadge.textContent = `错题 ${data.wrongCount}`;
    const map = { correct: "正确", partial: "部分正确", wrong: "错误" };
    resultBox.className = `result ${data.verdict}`;
    resultBox.textContent = `${map[data.verdict] || data.verdict} · 参考：${data.answerPrimary}${(data.answerAlts || []).length ? " ｜ 也可：" + data.answerAlts.join(" / ") : ""}`;
    if (data.verdict === "correct") correctCount += 1;
    else if (data.verdict === "partial") partialCount += 1;
    else wrongCountRound += 1;
  }

  function speak() {
    const item = session[index];
    if (!item || !window.speechSynthesis) return;
    const text = item.answerPrimary || item.prompt || "";
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = /[\u4e00-\u9fff]/.test(text) ? "zh-CN" : "en-US";
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(utter);
  }

  function nextQuestion() {
    if (!graded) return;
    if (index + 1 >= session.length) {
      summaryText.textContent = `共 ${session.length} 题：正确 ${correctCount}，部分正确 ${partialCount}，错误 ${wrongCountRound}。`;
      show("done");
      return;
    }
    index += 1;
    renderQuestion();
  }

  document.getElementById("startBtn").addEventListener("click", () => {
    startSession().catch((e) => {
      unitHint.textContent = String(e.message || e);
    });
  });
  document.getElementById("clearWrongBtn").addEventListener("click", async () => {
    await api("/api/wrong/clear", { method: "POST", headers: { "Content-Type": "application/json" }, body: "{}" });
    await refreshWrongBadge();
  });
  document.getElementById("checkBtn").addEventListener("click", () => checkAnswer(false));
  document.getElementById("revealBtn").addEventListener("click", () => checkAnswer(true));
  document.getElementById("speakBtn").addEventListener("click", speak);
  document.getElementById("nextBtn").addEventListener("click", nextQuestion);
  document.getElementById("exitBtn").addEventListener("click", () => show("home"));
  document.getElementById("againBtn").addEventListener("click", () => startSession());
  document.getElementById("homeBtn").addEventListener("click", () => show("home"));
  unitSelect.addEventListener("change", refreshUnitHint);
  answerInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      if (!graded) checkAnswer(false);
      else nextQuestion();
    }
  });

  loadManifest().catch((e) => {
    unitHint.textContent = `加载失败：${e.message || e}`;
  });
})();
