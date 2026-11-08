import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';
import { Blank, QuizItem, UnitBank, UnitMeta } from '../model/QuizModels';

export class ContentRepository {
  private context: common.UIAbilityContext;

  constructor(context: common.UIAbilityContext) {
    this.context = context;
  }

  async loadManifest(): Promise<Array<UnitMeta>> {
    const text: string = await this.readRawFile('content/manifest.json');
    const rootObj: Record<string, Object> = JSON.parse(text) as Record<string, Object>;
    const unitsObj: Object = rootObj['units'];
    const unitsArr: Array<Object> = unitsObj as Array<Object>;
    const list: Array<UnitMeta> = [];
    for (let i: number = 0; i < unitsArr.length; i++) {
      const row: Record<string, Object> = unitsArr[i] as Record<string, Object>;
      const meta: UnitMeta = new UnitMeta();
      meta.unitId = row['unitId'] as string;
      meta.name = row['name'] as string;
      meta.order = row['order'] as number;
      meta.file = row['file'] as string;
      if (row['rangeFrom'] !== undefined && row['rangeFrom'] !== null) {
        meta.rangeFrom = row['rangeFrom'] as string;
      }
      if (row['rangeTo'] !== undefined && row['rangeTo'] !== null) {
        meta.rangeTo = row['rangeTo'] as string;
      }
      if (row['wordsPerUnit'] !== undefined && row['wordsPerUnit'] !== null) {
        meta.wordsPerUnit = row['wordsPerUnit'] as number;
      }
      if (row['hasContent'] !== undefined && row['hasContent'] !== null) {
        meta.hasContent = row['hasContent'] as boolean;
      }
      list.push(meta);
    }
    list.sort((a: UnitMeta, b: UnitMeta): number => {
      return a.order - b.order;
    });
    return list;
  }

  async loadUnit(fileName: string): Promise<UnitBank> {
    const text: string = await this.readRawFile(`content/${fileName}`);
    const rootObj: Record<string, Object> = JSON.parse(text) as Record<string, Object>;
    const bank: UnitBank = new UnitBank();
    bank.unitId = rootObj['unitId'] as string;
    bank.name = rootObj['name'] as string;
    bank.order = rootObj['order'] as number;
    if (rootObj['rangeFrom'] !== undefined && rootObj['rangeFrom'] !== null) {
      bank.rangeFrom = rootObj['rangeFrom'] as string;
    }
    if (rootObj['rangeTo'] !== undefined && rootObj['rangeTo'] !== null) {
      bank.rangeTo = rootObj['rangeTo'] as string;
    }
    if (rootObj['wordsPerUnit'] !== undefined && rootObj['wordsPerUnit'] !== null) {
      bank.wordsPerUnit = rootObj['wordsPerUnit'] as number;
    }
    const itemsObj: Object = rootObj['items'];
    const itemsArr: Array<Object> = itemsObj as Array<Object>;
    const items: Array<QuizItem> = [];
    for (let i: number = 0; i < itemsArr.length; i++) {
      const row: Record<string, Object> = itemsArr[i] as Record<string, Object>;
      items.push(ContentRepository.parseItem(row));
    }
    bank.items = items;
    return bank;
  }

  private static parseItem(row: Record<string, Object>): QuizItem {
    const item: QuizItem = new QuizItem();
    item.id = row['id'] as string;
    item.unitId = row['unitId'] as string;
    item.type = row['type'] as string;
    item.prompt = row['prompt'] as string;
    item.answerPrimary = row['answerPrimary'] as string;
    item.answerAlts = ContentRepository.toStringArray(row['answerAlts']);
    item.blanks = ContentRepository.toBlankArray(row['blanks']);
    if (row['hint'] !== undefined && row['hint'] !== null) {
      item.hint = row['hint'] as string;
    }
    item.tags = ContentRepository.toStringArray(row['tags']);
    if (row['relatedGroupId'] !== undefined && row['relatedGroupId'] !== null) {
      item.relatedGroupId = row['relatedGroupId'] as string;
    }
    if (row['sourceRef'] !== undefined && row['sourceRef'] !== null) {
      item.sourceRef = row['sourceRef'] as string;
    }
    if (row['segment'] !== undefined && row['segment'] !== null) {
      item.segment = row['segment'] as string;
    }
    return item;
  }

  private static toStringArray(value: Object | undefined | null): Array<string> {
    const result: Array<string> = [];
    if (value === undefined || value === null) {
      return result;
    }
    const arr: Array<Object> = value as Array<Object>;
    for (let i: number = 0; i < arr.length; i++) {
      result.push(arr[i] as string);
    }
    return result;
  }

  private static toBlankArray(value: Object | undefined | null): Array<Blank> {
    const result: Array<Blank> = [];
    if (value === undefined || value === null) {
      return result;
    }
    const arr: Array<Object> = value as Array<Object>;
    for (let i: number = 0; i < arr.length; i++) {
      const row: Record<string, Object> = arr[i] as Record<string, Object>;
      const blank: Blank = new Blank();
      blank.index = row['index'] as number;
      blank.answer = row['answer'] as string;
      blank.alts = ContentRepository.toStringArray(row['alts']);
      result.push(blank);
    }
    return result;
  }

  private async readRawFile(relativePath: string): Promise<string> {
    try {
      const resourceManager = this.context.resourceManager;
      const fileData: Uint8Array = await resourceManager.getRawFileContent(relativePath);
      const textDecoder: util.TextDecoder = util.TextDecoder.create('utf-8', {
        ignoreBOM: true
      });
      return textDecoder.decodeToString(fileData);
    } catch (e) {
      const err: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'Words3500', 'readRawFile failed %{public}s %{public}s', relativePath, err.message);
      throw new Error(`readRawFile failed: ${relativePath}`);
    }
  }
}
