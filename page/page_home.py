from selenium.webdriver.common.by import By

import page
from base.base_action import BaseAction
class PageHome(BaseAction):
    # 元素特征和By方法不用通过参数从其他地方传过来，所以函数的括号不用写参数了，再下一句直接放特征和By方法的调用
    def click_my(self):
        self.click(page.my_button)

#    没登录就登录的封装，为什么在page_home封装，不在base封装？
    # 判读用户是否登录，登录了就什么不做，一个return就好，没登录就进行登录操作
    # if判断，点击我的，页面界面名与注册登录弹出页的界面名不一样则说明已经登录，页面名与注册登录弹出页界面名一样则说明，没登录
    def login_if_not(self,page):
        # click_my是自己的页面，当然不需要用页面入口
        self.click_my()
        # 为什么下面这句没有自动补全？
        # 不要只记adb获取界面名，还得记appium获取界面名
        if self.driver.current_activity!= 'com.yunmall.ymctoc.ui.activity.LogonActivity':
            return
        # 不要else是什么效果？
        else:
          # 输入密码账号，点击登录，这些方法在各自页面文件中，所以这里要得到页面入口，不用实例化后赋值变量，太麻烦，而且不符合po思想
    # page相关页面不写init。所以自然想到通过参数接受page入口。所以在函数参数给了个自定义参数page
    #       为什么下面没有自动补全，因为写这个的时候，虽然有参数可以接收页面入口，但是我在test_.py还没有写传过来的代码，下面自然就不会自动补全了
          page.login_or_register.click_haved_account()
          page.login.input_username('itbainian')
          page.login.input_password('itbainian123')
          page.login.click_login()

