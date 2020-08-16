import page
from base.base_action import BaseAction

class PageAddressAdministration(BaseAction):
    def click_new_address(self):
        self.find_element_with_scroll(page.new_address_butotn).click()

    #     H获取地址管理第一个默认地址的姓名和手机
    def get_receipt_and_phone(self):
        # *********base虽然，return了，不代表这里也是自动return。这里不return，调用的时候等不到东西！！！！！！！！！
        # 获取文本的，每一层都得return
        return self.get_text(page.receipt_and_name)

