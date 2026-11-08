import { QuizItem, QuizModeConst, QuizSegmentConst } from '../model/QuizModels';

export class QuizEngine {
  static filterBySegment(items: Array<QuizItem>, segment: string): Array<QuizItem> {
    if (segment === QuizSegmentConst.ALL) {
      return items;
    }
    if (segment === QuizSegmentConst.FIRST_25) {
      return QuizEngine.filterSegmentOrHalf(items, '1-25', true);
    }
    if (segment === QuizSegmentConst.LAST_25) {
      return QuizEngine.filterSegmentOrHalf(items, '26-50', false);
    }
    return items;
  }

  static filterByMode(items: Array<QuizItem>, mode: string, wrongIds: Array<string>): Array<QuizItem> {
    const result: Array<QuizItem> = [];
    for (let i: number = 0; i < items.length; i++) {
      const item: QuizItem = items[i];
      if (mode === QuizModeConst.ZH2EN) {
        if (item.type === 'zh2en') {
          result.push(item);
        }
      } else if (mode === QuizModeConst.CLOZE) {
        if (item.type === 'cloze' || item.type === 'word_form') {
          result.push(item);
        }
      } else if (mode === QuizModeConst.WRONG_ONLY) {
        if (QuizEngine.containsId(wrongIds, item.id)) {
          result.push(item);
        }
      } else {
        result.push(item);
      }
    }
    return result;
  }

  static pickSession(pool: Array<QuizItem>, count: number, mode: string): Array<QuizItem> {
    if (pool.length === 0) {
      return [];
    }
    let ordered: Array<QuizItem> = [];
    if (mode === QuizModeConst.MIXED) {
      ordered = QuizEngine.weightedShuffle(pool);
    } else {
      ordered = QuizEngine.shuffle(pool);
    }
    const limit: number = Math.min(count, ordered.length);
    const session: Array<QuizItem> = [];
    for (let i: number = 0; i < limit; i++) {
      session.push(ordered[i]);
    }
    return session;
  }

  private static filterSegmentOrHalf(items: Array<QuizItem>, segmentId: string, takeFirstHalf: boolean): Array<QuizItem> {
    const tagged: Array<QuizItem> = [];
    for (let i: number = 0; i < items.length; i++) {
      if (items[i].segment === segmentId) {
        tagged.push(items[i]);
      }
    }
    if (tagged.length > 0) {
      return tagged;
    }
    if (items.length === 0) {
      return [];
    }
    const mid: number = Math.floor((items.length + 1) / 2);
    const result: Array<QuizItem> = [];
    if (takeFirstHalf) {
      for (let i: number = 0; i < mid; i++) {
        result.push(items[i]);
      }
    } else {
      for (let i: number = mid; i < items.length; i++) {
        result.push(items[i]);
      }
    }
    return result;
  }

  private static containsId(ids: Array<string>, id: string): boolean {
    for (let i: number = 0; i < ids.length; i++) {
      if (ids[i] === id) {
        return true;
      }
    }
    return false;
  }

  private static weightOf(type: string): number {
    if (type === 'zh2en') {
      return 3;
    }
    if (type === 'cloze') {
      return 3;
    }
    if (type === 'word_form') {
      return 2;
    }
    if (type === 'phrase_cluster') {
      return 2;
    }
    if (type === 'pattern') {
      return 1;
    }
    return 1;
  }

  private static weightedShuffle(items: Array<QuizItem>): Array<QuizItem> {
    const bag: Array<QuizItem> = [];
    for (let i: number = 0; i < items.length; i++) {
      const item: QuizItem = items[i];
      const w: number = QuizEngine.weightOf(item.type);
      for (let j: number = 0; j < w; j++) {
        bag.push(item);
      }
    }
    const shuffled: Array<QuizItem> = QuizEngine.shuffle(bag);
    const unique: Array<QuizItem> = [];
    const seen: Array<string> = [];
    for (let k: number = 0; k < shuffled.length; k++) {
      const cur: QuizItem = shuffled[k];
      if (!QuizEngine.containsId(seen, cur.id)) {
        seen.push(cur.id);
        unique.push(cur);
      }
    }
    return unique;
  }

  private static shuffle(items: Array<QuizItem>): Array<QuizItem> {
    const copy: Array<QuizItem> = [];
    for (let i: number = 0; i < items.length; i++) {
      copy.push(items[i]);
    }
    for (let i: number = copy.length - 1; i > 0; i--) {
      const j: number = Math.floor(Math.random() * (i + 1));
      const tmp: QuizItem = copy[i];
      copy[i] = copy[j];
      copy[j] = tmp;
    }
    return copy;
  }
}
