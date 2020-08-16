import page
from base.base_action import BaseAction


class PageAboutOut(BaseAction):

    def click_update_version(self):
        # 每次自动补齐完成，都忘记写click！！！！！！！
        self.find_element_with_scroll(page.update_version_button).click()