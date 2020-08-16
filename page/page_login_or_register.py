import page
from base.base_action import BaseAction


class PageLoginOrRegister(BaseAction):

    def click_haved_account(self):
        self.click(page.haved_account)

