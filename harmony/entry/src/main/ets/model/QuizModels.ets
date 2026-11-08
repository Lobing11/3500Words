export class Blank {
  index: number = 0;
  answer: string = '';
  alts: Array<string> = [];
}

export class QuizItem {
  id: string = '';
  unitId: string = '';
  type: string = '';
  prompt: string = '';
  answerPrimary: string = '';
  answerAlts: Array<string> = [];
  blanks: Array<Blank> = [];
  hint: string = '';
  tags: Array<string> = [];
  relatedGroupId: string = '';
  sourceRef: string = '';
}

export class UnitBank {
  unitId: string = '';
  name: string = '';
  order: number = 0;
  items: Array<QuizItem> = [];
}

export class UnitMeta {
  unitId: string = '';
  name: string = '';
  order: number = 0;
  file: string = '';
}

export class ManifestRoot {
  version: number = 1;
  units: Array<UnitMeta> = [];
}

export class GradeVerdictConst {
  static readonly CORRECT: string = 'correct';
  static readonly PARTIAL: string = 'partial';
  static readonly WRONG: string = 'wrong';
}

export class QuizModeConst {
  static readonly ZH2EN: string = 'zh2en';
  static readonly CLOZE: string = 'cloze';
  static readonly MIXED: string = 'mixed';
  static readonly WRONG_ONLY: string = 'wrong_only';
}
