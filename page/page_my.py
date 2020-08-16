import time

import page
from base.base_action import BaseAction


class PageMy(BaseAction):

    def get_nickname_text(self):
        return self.find_element(page.nick_name_text_view).text

    def click_setting(self):
        self.click(page.setting_button)
    # 为什么加5秒呢，因为我们在脚本*调试*获取上下文内容时，打印上下文内容，点击后不停留的话，可能上下文没出来完就打印了，不完全
    # 还要正式流程时，如果后面是点击，不用专门给时间加载，因为寻找元素设置了显示等待，如果下面是获取信息等等，就得专门给他5秒加载了
    def click_vip(self):
        self.click(page.join_super_vip)
        time.sleep(5)
