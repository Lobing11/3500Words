import { GradeVerdictConst, QuizItem, QuizModeConst, QuizSegmentConst, UnitMeta } from '../model/QuizModels';
import { AppServices } from '../common/AppServices';
import { Grader } from '../service/Grader';
import { QuizEngine } from '../service/QuizEngine';
import { ContentRepository } from '../service/ContentRepository';
import { WrongBookStore } from '../service/WrongBookStore';

@Entry
@Component
struct Index {
  @State units: Array<UnitMeta> = [];
  @State selectedUnitId: string = '';
  @State selectedUnitName: string = '';
  @State selectedFile: string = '';
  @State selectedHasContent: boolean = false;
  @State mode: string = QuizModeConst.MIXED;
  @State segment: string = QuizSegmentConst.FIRST_25;
  @State wrongCount: number = 0;
  @State message: string = '';
  @State inSession: boolean = false;
  @State finished: boolean = false;
  @State session: Array<QuizItem> = [];
  @State index: number = 0;
  @State inputText: string = '';
  @State revealed: boolean = false;
  @State lastVerdict: string = '';
  @State correctCount: number = 0;
  @State answeredCount: number = 0;

  aboutToAppear(): void {
    this.bootstrap();
  }

  private async bootstrap(): Promise<void> {
    const content: ContentRepository | null = AppServices.content;
    const wrongBook: WrongBookStore | null = AppServices.wrongBook;
    if (content === null || wrongBook === null) {
      this.message = '服务未初始化';
      return;
    }
    const units: Array<UnitMeta> = await content.loadManifest();
    this.units = units;
    let preferred: UnitMeta | null = null;
    for (let i: number = 0; i < units.length; i++) {
      if (units[i].hasContent) {
        preferred = units[i];
        break;
      }
    }
    if (preferred === null && units.length > 0) {
      preferred = units[0];
    }
    if (preferred !== null) {
      this.selectedUnitId = preferred.unitId;
      this.selectedUnitName = preferred.name;
      this.selectedFile = preferred.file;
      this.selectedHasContent = preferred.hasContent;
    }
    this.wrongCount = wrongBook.wrongIds().length;
  }

  private selectUnit(unit: UnitMeta): void {
    this.selectedUnitId = unit.unitId;
    this.selectedUnitName = unit.name;
    this.selectedFile = unit.file;
    this.selectedHasContent = unit.hasContent;
    this.message = '';
  }

  private selectMode(mode: string): void {
    this.mode = mode;
  }

  private selectSegment(segment: string): void {
    this.segment = segment;
  }

  private async startSession(count: number): Promise<void> {
    const content: ContentRepository | null = AppServices.content;
    const wrongBook: WrongBookStore | null = AppServices.wrongBook;
    if (content === null || wrongBook === null) {
      this.message = '服务未初始化';
      return;
    }
    if (this.selectedFile.length === 0) {
      this.message = '请先选择 Unit';
      return;
    }
    if (!this.selectedHasContent) {
      this.message = `${this.selectedUnitName} 词库尚未入库（目录已对齐，内容待补充）`;
      return;
    }
    const bank = await content.loadUnit(this.selectedFile);
    const bySegment: Array<QuizItem> = QuizEngine.filterBySegment(bank.items, this.segment);
    const pool: Array<QuizItem> = QuizEngine.filterByMode(bySegment, this.mode, wrongBook.wrongIds());
    const session: Array<QuizItem> = QuizEngine.pickSession(pool, count, this.mode);
    if (session.length === 0) {
      this.message = '当前范围没有可抽题目';
      return;
    }
    this.session = session;
    this.index = 0;
    this.inputText = '';
    this.revealed = false;
    this.lastVerdict = '';
    this.correctCount = 0;
    this.answeredCount = 0;
    this.finished = false;
    this.inSession = true;
    this.message = '';
    this.wrongCount = wrongBook.wrongIds().length;
  }

  private currentItem(): QuizItem | null {
    if (this.index < 0 || this.index >= this.session.length) {
      return null;
    }
    return this.session[this.index];
  }

  private currentPrompt(): string {
    const item: QuizItem | null = this.currentItem();
    if (item === null) {
      return '';
    }
    return item.prompt;
  }

  private currentType(): string {
    const item: QuizItem | null = this.currentItem();
    if (item === null) {
      return '';
    }
    return item.type;
  }

  private currentHint(): string {
    const item: QuizItem | null = this.currentItem();
    if (item === null) {
      return '';
    }
    return item.hint;
  }

  private currentAnswer(): string {
    const item: QuizItem | null = this.currentItem();
    if (item === null) {
      return '';
    }
    return item.answerPrimary;
  }

  private currentAltsText(): string {
    const item: QuizItem | null = this.currentItem();
    if (item === null) {
      return '';
    }
    if (item.answerAlts.length === 0) {
      return '';
    }
    return item.answerAlts.join(' / ');
  }

  private currentBlankCount(): number {
    const item: QuizItem | null = this.currentItem();
    if (item === null) {
      return 0;
    }
    return item.blanks.length;
  }

  private progressText(): string {
    return `第 ${this.index + 1}/${this.session.length} · ${this.currentType()}`;
  }

  private async submitAnswer(): Promise<void> {
    const item: QuizItem | null = this.currentItem();
    const wrongBook: WrongBookStore | null = AppServices.wrongBook;
    if (item === null || wrongBook === null) {
      return;
    }
    if (this.revealed) {
      return;
    }
    const verdict: string = Grader.grade(item, this.inputText);
    this.lastVerdict = verdict;
    this.revealed = true;
    this.answeredCount = this.answeredCount + 1;
    if (verdict === GradeVerdictConst.CORRECT) {
      this.correctCount = this.correctCount + 1;
      await wrongBook.markCorrect(item.id);
    } else {
      await wrongBook.markWrong(item.id);
    }
    this.wrongCount = wrongBook.wrongIds().length;
  }

  private async revealAnswer(): Promise<void> {
    const item: QuizItem | null = this.currentItem();
    const wrongBook: WrongBookStore | null = AppServices.wrongBook;
    if (item === null || wrongBook === null) {
      return;
    }
    if (this.revealed) {
      return;
    }
    this.lastVerdict = GradeVerdictConst.WRONG;
    this.revealed = true;
    this.answeredCount = this.answeredCount + 1;
    await wrongBook.markWrong(item.id);
    this.wrongCount = wrongBook.wrongIds().length;
  }

  private goNext(): void {
    const nextIndex: number = this.index + 1;
    if (nextIndex >= this.session.length) {
      this.finished = true;
      this.inSession = false;
      return;
    }
    this.index = nextIndex;
    this.inputText = '';
    this.revealed = false;
    this.lastVerdict = '';
  }

  private speakAnswer(): void {
    // Phase1: TTS 接入放到后续迭代，避免 SDK 版本 API 差异阻断编译。
    console.info(`speak: ${this.currentAnswer()}`);
  }

  private exitSession(): void {
    this.inSession = false;
    this.finished = false;
    this.session = [];
  }

  private verdictLabel(): string {
    if (this.lastVerdict === GradeVerdictConst.CORRECT) {
      return '正确';
    }
    if (this.lastVerdict === GradeVerdictConst.PARTIAL) {
      return '部分正确';
    }
    if (this.lastVerdict === GradeVerdictConst.WRONG) {
      return '错误';
    }
    return '';
  }

  @Builder
  HomeBlock() {
    Column({ space: 12 }) {
      Text('3500 词汇抽背')
        .fontSize(28)
        .fontWeight(FontWeight.Bold)
      Text('目录：每 Unit 50 词；抽查可拆前/后 25 词')
        .fontSize(14)
        .fontColor('#666666')

      Text('选择 Unit（1–60）')
        .fontSize(18)
        .margin({ top: 8 })

      List() {
        ForEach(this.units, (unit: UnitMeta) => {
          ListItem() {
            Text(this.unitLabel(unit))
              .width('100%')
              .padding(10)
              .onClick(() => {
                this.selectUnit(unit);
              })
          }
        }, (unit: UnitMeta): string => unit.unitId)
      }
      .height(160)

      Text('分段（每 Unit 约 50 词）').fontSize(18)
      Row({ space: 8 }) {
        Button('前25')
          .onClick(() => {
            this.selectSegment(QuizSegmentConst.FIRST_25);
          })
        Button('后25')
          .onClick(() => {
            this.selectSegment(QuizSegmentConst.LAST_25);
          })
        Button('整Unit')
          .onClick(() => {
            this.selectSegment(QuizSegmentConst.ALL);
          })
      }

      Text('抽背模式').fontSize(18)
      Row({ space: 8 }) {
        Button('中译英')
          .onClick(() => {
            this.selectMode(QuizModeConst.ZH2EN);
          })
        Button('填空')
          .onClick(() => {
            this.selectMode(QuizModeConst.CLOZE);
          })
        Button('混合')
          .onClick(() => {
            this.selectMode(QuizModeConst.MIXED);
          })
        Button('错题')
          .onClick(() => {
            this.selectMode(QuizModeConst.WRONG_ONLY);
          })
      }

      Text(`分段：${this.segmentLabel()} · 模式：${this.modeLabel()} · 错题 ${this.wrongCount}`)

      if (this.message.length > 0) {
        Text(this.message).fontColor('#B00020')
      }

      Button('开始抽背（25题）')
        .width('100%')
        .onClick(() => {
          this.startSession(25);
        })
      Button('快速 10 题')
        .width('100%')
        .onClick(() => {
          this.startSession(10);
        })
    }
    .width('100%')
    .alignItems(HorizontalAlign.Start)
  }

  private unitLabel(unit: UnitMeta): string {
    let mark: string = '';
    if (!unit.hasContent) {
      mark = ' · 待入库';
    }
    if (unit.unitId === this.selectedUnitId) {
      return `● ${unit.name}${mark}`;
    }
    return `○ ${unit.name}${mark}`;
  }

  private segmentLabel(): string {
    if (this.segment === QuizSegmentConst.FIRST_25) {
      return '前25词';
    }
    if (this.segment === QuizSegmentConst.LAST_25) {
      return '后25词';
    }
    return '整Unit';
  }

  private modeLabel(): string {
    if (this.mode === QuizModeConst.ZH2EN) {
      return '中译英';
    }
    if (this.mode === QuizModeConst.CLOZE) {
      return '填空';
    }
    if (this.mode === QuizModeConst.WRONG_ONLY) {
      return '错题';
    }
    return '混合';
  }

  @Builder
  QuizBlock() {
    Column({ space: 12 }) {
      Text(this.progressText()).fontSize(14)
      Text(this.currentPrompt())
        .fontSize(22)
        .fontWeight(FontWeight.Medium)

      if (this.currentHint().length > 0) {
        Text(`提示：${this.currentHint()}`).fontSize(12).fontColor('#666666')
      }

      if (this.currentBlankCount() > 1) {
        Text('多空请用 | 分隔，例如：on|under').fontSize(12).fontColor('#666666')
      }

      TextInput({ text: this.inputText, placeholder: '你的答案' })
        .enabled(!this.revealed)
        .onChange((value: string) => {
          this.inputText = value;
        })

      if (this.revealed) {
        Text(`结果：${this.verdictLabel()}`).fontSize(18)
        Text(`参考答案：${this.currentAnswer()}`)
        if (this.currentAltsText().length > 0) {
          Text(`也可接受：${this.currentAltsText()}`)
        }
      }

      Row({ space: 8 }) {
        if (!this.revealed) {
          Button('提交')
            .onClick(() => {
              this.submitAnswer();
            })
          Button('不会 / 揭晓')
            .onClick(() => {
              this.revealAnswer();
            })
        } else {
          Button('下一题')
            .onClick(() => {
              this.goNext();
            })
          Button('发音')
            .onClick(() => {
              this.speakAnswer();
            })
        }
      }

      Button('结束本轮')
        .onClick(() => {
          this.exitSession();
        })
    }
    .width('100%')
    .alignItems(HorizontalAlign.Start)
  }

  @Builder
  ResultBlock() {
    Column({ space: 12 }) {
      Text('本轮结束').fontSize(28).fontWeight(FontWeight.Bold)
      Text(`正确 ${this.correctCount} / ${this.answeredCount}`)
      Text(`当前错题本：${this.wrongCount} 题`)
      Button('返回首页')
        .width('100%')
        .onClick(() => {
          this.exitSession();
        })
      Button('再来一轮')
        .width('100%')
        .onClick(() => {
          this.startSession(25);
        })
    }
    .width('100%')
    .alignItems(HorizontalAlign.Start)
  }

  build() {
    Column() {
      if (this.inSession) {
        this.QuizBlock()
      } else if (this.finished) {
        this.ResultBlock()
      } else {
        this.HomeBlock()
      }
    }
    .padding(20)
    .width('100%')
    .height('100%')
  }
}
