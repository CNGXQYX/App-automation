import page
from base.base_action import BaseAction

class PageAd(BaseAction):
    def click_skip(self):
        self.click(page.skip_button)
    def ad_if_not(self):
        if  self.driver.current_activity!='com.yunmall.ymctoc.ui.activity.GuideActivity':
            # 是首页
            return
        else:
            self.click_skip()