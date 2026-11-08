import { common } from '@kit.AbilityKit';
import { ContentRepository } from '../service/ContentRepository';
import { WrongBookStore } from '../service/WrongBookStore';

export class AppServices {
  static content: ContentRepository | null = null;
  static wrongBook: WrongBookStore | null = null;

  static async init(context: common.UIAbilityContext): Promise<void> {
    AppServices.content = new ContentRepository(context);
    const store: WrongBookStore = new WrongBookStore();
    await store.init(context);
    AppServices.wrongBook = store;
  }
}
