import page
from base.base_action import BaseAction


class PageVip(BaseAction):
    def input_invite(self,text):
        # 输入一般是在当前屏幕，不用滑动
        # 点击可能滑动，所以一般点击用滑动方法
        self.input(page.invite_frame,text)
    def click_be_vip(self):
        self.find_element_with_scroll(page.be_vip_button).click()


