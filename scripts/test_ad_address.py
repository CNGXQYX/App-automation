import time

import pytest

from base.base_analyzes import analyzes_file
from base.base_get_driver import init_driver
from page.page import Page

class TestAdAddress():
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    @pytest.mark.parametrize('args',analyzes_file('data_ad_addr','test_ad_address'))
    # 一定记得给一个参数
    def test_ad_address(self,args):
        name=args['name']
        phone=args['phone']
        detail_addr=args['detail_addr']
        post_code=args['post']
        toast=args['toast']

        self.page.home.login_if_not(self.page)
        self.page.my.click_setting()
        self.page.setting.click_address()
        self.page.address_administration.click_new_address()
        self.page.new_address.input_receipt(name)
        self.page.new_address.input_phone(phone)
        self.page.new_address.input_detailed_address(detail_addr)
        self.page.new_address.input_post(post_code)
        self.page.new_address.click_defaul()

        # 这句不用写了，因为choose_region方法已经有点击并选择了
        # self.page.new_address.click_region()

        self.page.new_address.choose_region()
        self.page.new_address.click_save()

        if toast is None:
            # 获取第一个地址信息内容，与自己所填的是否一样进行断言
            # 看了uiautomater.发现名字和手机间有两个空格
            # assert self.page.address_administration.get_receipt_and_phone()=='name  phone','保存成功，默认地址与所输不一致'
            # 'name  phone'  加双引号之后，name phone就不是变量了，只是字符串，打印的结果是'name  phone'
            # 所以必须用%s的方法，它才是变量
            assert self.page.address_administration.get_receipt_and_phone() == '%s  %s' %(name,phone),'保存成功，默认地址与所输不一致'

        else:
            assert self.page.address_administration.is_toast_exist(toast),'保存不成功，toast内容与预期不符'



