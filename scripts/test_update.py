import time

from base.base_get_driver import init_driver
from page.page import Page


class TestUpdate:

    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_update(self):
        # 一定记得login_if_not要传一个页面入口！！！！，定义的时候给了一个接收页面入口的参数
        self.page.home.login_if_not(self.page)
        self.page.my.click_setting()
        self.page.setting.click_about_out()
        self.page.about_out.click_update_version()
        # 为什么这里不像test_login一样，将toast参数化呢？因为它就一个固定值，没必要参数化
        # 不用获取toast文本断言，用能否找到toast的方法进行断言就行
        assert self.page.about_out.is_toast_exist('当前已是最新版本')
