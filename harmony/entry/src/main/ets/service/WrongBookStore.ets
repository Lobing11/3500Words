import { preferences } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export class WrongBookStore {
  private pref: preferences.Preferences | null = null;
  private ids: Array<string> = [];

  async init(context: common.UIAbilityContext): Promise<void> {
    try {
      this.pref = await preferences.getPreferences(context, 'wrong_book');
      const saved: preferences.ValueType = await this.pref.get('ids', '[]');
      const text: string = saved as string;
      const parsed: Object = JSON.parse(text) as Object;
      const arr: Array<Object> = parsed as Array<Object>;
      const next: Array<string> = [];
      for (let i: number = 0; i < arr.length; i++) {
        next.push(arr[i] as string);
      }
      this.ids = next;
    } catch (e) {
      const err: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'Words3500', 'WrongBookStore init failed %{public}s', err.message);
      this.ids = [];
    }
  }

  wrongIds(): Array<string> {
    const copy: Array<string> = [];
    for (let i: number = 0; i < this.ids.length; i++) {
      copy.push(this.ids[i]);
    }
    return copy;
  }

  async markWrong(itemId: string): Promise<void> {
    if (!this.contains(itemId)) {
      this.ids.push(itemId);
      await this.persist();
    }
  }

  async markCorrect(itemId: string): Promise<void> {
    const next: Array<string> = [];
    for (let i: number = 0; i < this.ids.length; i++) {
      if (this.ids[i] !== itemId) {
        next.push(this.ids[i]);
      }
    }
    this.ids = next;
    await this.persist();
  }

  private contains(itemId: string): boolean {
    for (let i: number = 0; i < this.ids.length; i++) {
      if (this.ids[i] === itemId) {
        return true;
      }
    }
    return false;
  }

  private async persist(): Promise<void> {
    if (this.pref === null) {
      return;
    }
    try {
      await this.pref.put('ids', JSON.stringify(this.ids));
      await this.pref.flush();
    } catch (e) {
      const err: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'Words3500', 'WrongBookStore persist failed %{public}s', err.message);
    }
  }
}
