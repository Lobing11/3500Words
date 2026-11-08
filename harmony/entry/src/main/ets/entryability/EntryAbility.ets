import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { AppServices } from '../common/AppServices';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'Words3500', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(0x0000, 'Words3500', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    this.bootstrap(windowStage);
  }

  private async bootstrap(windowStage: window.WindowStage): Promise<void> {
    try {
      await AppServices.init(this.context);
      windowStage.loadContent('pages/Index', (err: BusinessError): void => {
        if (err.code) {
          hilog.error(0x0000, 'Words3500', 'Failed to load content %{public}d', err.code);
          return;
        }
        hilog.info(0x0000, 'Words3500', 'Succeeded in loading content');
      });
    } catch (e) {
      const err: Error = e as Error;
      hilog.error(0x0000, 'Words3500', 'AppServices init failed %{public}s', err.message);
    }
  }

  onWindowStageDestroy(): void {
    hilog.info(0x0000, 'Words3500', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    hilog.info(0x0000, 'Words3500', 'Ability onForeground');
  }

  onBackground(): void {
    hilog.info(0x0000, 'Words3500', 'Ability onBackground');
  }
}
