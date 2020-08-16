from page.page_about_out import PageAboutOut
from page.page_ad import PageAd
from page.page_address_administration import PageAddressAdministration
from page.page_home import PageHome
from page.page_login import PageLogin
from page.page_login_or_register import PageLoginOrRegister
from page.page_my import PageMy
from page.page_new_address import PageNewAddress
from page.page_setting import PageSetting
from page.page_vip import PageVip


class Page:

    def __init__(self,driver):
        self.driver=driver

    @property
    def home(self):
        # 函数的结果是某个东西时，记得返回，如找元素。但是点击这种不用返回，因为它是一个操作
        return PageHome(self.driver)
        # 没有这种写法
        # self.home=PageHome(self.driver)
    @property
    def login_or_register(self):
        return PageLoginOrRegister(self.driver)
        # self.login_or_register=PageLoginOrRegister
    @property
    def login(self):
        return PageLogin(self.driver)

    @property
    def my(self):
        return PageMy(self.driver)
    @property
    def ad(self):
        return PageAd(self.driver)

    @property
    def setting(self):
        return PageSetting(self.driver)

    @property
    def about_out(self):
            return PageAboutOut(self.driver)

    @property
    def vip(self):
        return PageVip(self.driver)

    @property
    def address_administration(self):
        return PageAddressAdministration(self.driver)

    @property
    def new_address(self):
        return PageNewAddress(self.driver)
