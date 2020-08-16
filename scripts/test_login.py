import time

import pytest

from base.base_analyzes import analyzes_file
from base.base_get_driver import init_driver
from page.page import Page
#为什么不用导 import pytest


class TestLogin:
    def setup(self):
        print('准备获取driver')
        self.driver = init_driver(no_reset=False)
        print('已经获取:',self.driver)

        self.page=Page(self.driver)

    def teardown(self):
        print('准备关闭driver')
        time.sleep(3)
        self.driver.quit()
        print('已经关闭driver')


    # def test_hello(self):
    #     self.page.home.login_if_not(self.page)

    # setup这些开头可以不写test,搜到class,他们就会执行
    # 但是测试用例要写,,虽然搜索到了class,但是搜不到用例,就不执行
    # 参数名要引号,还有记得将参数名传给test_login，它要使用，不要以为标记了就可以，不传他也用不了
    @pytest.mark.parametrize("args",analyzes_file('data_login','test_login'))
    def test_login(self,args):
        username=args["username"]
        password=args["password"]
        toast=args["toast"]


        ''''# else和’是流程‘平级，缩进才是else的下属
        # ****这个一定注意**********如果在if中用return，不只是退出if判断，而是退出整个test_login，所以return是针对整个函数而言
        # if self.driver.current_activity!='com.yunmall.ymctoc.ui.activity.GuideActivity':
        #    return print('是首页')
        #
        # else:
        #      print('广告')'''

        # 不要只写click，要知道page_home里写的是click_my（）
        # page_login_or_register里面写的是click_haved_account()
        # page不是包名，也不是.py名。更不可能是类名（大写）。
        # page不是单独，
        # self.page是一个整体，是前面的self.page=Page(self.driver)，
        # 不要想self调用了page，是self.page成了页面入口
        print('是流程')
        self.page.ad.ad_if_not()
        self.page.home.click_my()
        self.page.login_or_register.click_haved_account()
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_login()

        # toast出现与不出现都断言，这样只要与预期不一样都能知道
        # 预期中，toast不出现，但实际出现，不知道错误，顺利执行了els，那岂不是没发现bug？
        # 那els来把关，再断言，就能知道有bug了
        # 所以toast出现与不出现都断言
        # None的写法
        # toast是在上面参数化取值时定义过了，要不然系统不知道它是什么
        if toast is None:
            # 没有toast，可以用登录后的昵称显示断言，昵称显示是否等于输入的用户名
            # 断言逗号后面是断言失败才执行
            assert self.page.my.get_nickname_text()==username,'登录后的用户名于输入后的不一致'
        else:
            # 虽然page_my页面用中没封装is_toast_exist（），但可以继承的找下去
            # 用是否存在断言即可，不用到获取toast比较来断言，因为查找的时候通过预期的toast查找，找到就是预期实际一致，找不到就是预期实际不一致
            # 一定记得传toast进去，因为封装的is_toast_exist()有一message参数，
            assert self.page.my.is_toast_exist(toast)
