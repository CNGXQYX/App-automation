import time

import pytest

from base.base_analyzes import analyzes_file
from base.base_get_driver import init_driver
from page.page import Page


class TestJoinVip:

    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    #    修饰器中 args要双引号,函数参数不用。data_join_vip也是,且不用写后缀
    @pytest.mark.parametrize("args",analyzes_file("data_join_vip","test_join_vip"))
    def test_join_vip(self,args):
        invite=args['invite']
        keyword=args['keyword']
        self.page.home.login_if_not(self.page)
        self.page.my.click_vip()
        # 原生环境和webview环境混合，一定要记得切换环境
        # 这句代码为了调试，获取上下文内容所用
        # print(self.driver.contexts)
        # ['NATIVE_APP', 'WEBVIEW_com.yunmall.lc', 'WEBVIEW_com.android.browser']
        # 第二个是webview环境，测试软件选第二个，测试系统浏览器选第三个
        # 记住切换的代码，还有下面是context，上面的获取还得加s，因为全部上下文，当然s
        # 切换上下文这一句也需要有对的chromedriver，才能运行


        time.sleep(3)
        # 不加time延时，手机显示输入不进去，其实不是输入不进，是这句话没切换成功，属于自己代码出问题，代码停止执行，应用关闭，因为到了输入那一步，误认为是输入不进去
        # 虽然看是切换，但实际里面是先获取上下文内容才能切换，不给延时，有时加载慢，上下文没出来完就已经切换了，肯定出错
        self.driver.switch_to.context('WEBVIEW_com.yunmall.lc')



        # 要对webview内容操作，不仅需要切换环境，还要下载对应手机浏览器内核版本对应的chromedriver，在appium软件中配置路径
        self.page.vip.input_invite(invite)
        self.page.vip.click_be_vip()
        # 这两句用来调试，看page_source里面的内容是什么，延时是看情况的，不延时打印不出，延时太久打印不出，自己看着罗
        # time.sleep(1)
        # print(self.driver.page_source)
        assert self.page.vip.is_keyword_in_page_source(keyword),'%s不在page_source中' % keyword
#         切换回原生环境
        self.driver.switch_to.context('NATIVE_APP')
