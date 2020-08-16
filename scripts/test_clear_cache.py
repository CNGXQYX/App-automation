import time

from base.base_get_driver import init_driver
from page.page import Page


class TestClearCache:
    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    def test_clear_cache(self):
        self.page.home.login_if_not(self.page)
        self.page.my.click_setting()
        self.page.setting.click_clear_cache()
        assert self.page.setting.is_toast_exist('清理成功')