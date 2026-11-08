import { Blank, GradeVerdictConst, QuizItem } from '../model/QuizModels';

export class Grader {
  static normalize(raw: string): string {
    let s: string = raw.trim().toLowerCase();
    const spaceRe: RegExp = new RegExp('\\s+', 'g');
    s = s.replace(spaceRe, ' ');
    const endRe: RegExp = new RegExp('[.?!;:,]+$', 'g');
    s = s.replace(endRe, '');
    return s;
  }

  static grade(item: QuizItem, userInput: string): string {
    if (item.blanks.length > 0) {
      return Grader.gradeBlanks(item.blanks, userInput);
    }
    const candidates: Array<string> = [];
    candidates.push(item.answerPrimary);
    for (let i: number = 0; i < item.answerAlts.length; i++) {
      candidates.push(item.answerAlts[i]);
    }
    if (Grader.matchesAny(userInput, candidates)) {
      return GradeVerdictConst.CORRECT;
    }
    return GradeVerdictConst.WRONG;
  }

  private static gradeBlanks(blanks: Array<Blank>, userInput: string): string {
    const parts: Array<string> = Grader.splitAnswers(userInput);
    let correctCount: number = 0;
    const limit: number = blanks.length;
    for (let i: number = 0; i < limit; i++) {
      if (i >= parts.length) {
        continue;
      }
      const candidates: Array<string> = Grader.blankCandidates(blanks[i]);
      if (Grader.matchesAny(parts[i], candidates)) {
        correctCount += 1;
      }
    }
    if (correctCount === limit) {
      return GradeVerdictConst.CORRECT;
    }
    if (correctCount === 0) {
      return GradeVerdictConst.WRONG;
    }
    return GradeVerdictConst.PARTIAL;
  }

  private static splitAnswers(userInput: string): Array<string> {
    const rawParts: Array<string> = userInput.split('|');
    const result: Array<string> = [];
    for (let i: number = 0; i < rawParts.length; i++) {
      const piece: string = rawParts[i].trim();
      if (piece.length > 0) {
        result.push(piece);
      }
    }
    if (result.length <= 1) {
      const lines: Array<string> = userInput.split('\n');
      const lineResult: Array<string> = [];
      for (let j: number = 0; j < lines.length; j++) {
        const line: string = lines[j].trim();
        if (line.length > 0) {
          lineResult.push(line);
        }
      }
      if (lineResult.length > result.length) {
        return lineResult;
      }
    }
    return result;
  }

  private static blankCandidates(blank: Blank): Array<string> {
    const candidates: Array<string> = [];
    candidates.push(blank.answer);
    for (let i: number = 0; i < blank.alts.length; i++) {
      candidates.push(blank.alts[i]);
    }
    return candidates;
  }

  private static matchesAny(input: string, candidates: Array<string>): boolean {
    const normalized: string = Grader.normalize(input);
    for (let i: number = 0; i < candidates.length; i++) {
      if (Grader.normalize(candidates[i]) === normalized) {
        return true;
      }
    }
    return false;
  }
}
