from appium import webdriver
from selenium.webdriver.common.by import By

from base.base_action import BaseAction
from page.page_home import PageHome

# 用来检测滑动找元素的封装写对没有
class TestDemo:
#这里没有单例设计？
    def setup(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '1'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 关键字：noResete和值：no_rest
        #  no_reset参数为True时，不用重置应用
        # desired_caps['noRest']=True
        #告诉appium使用uiautomator2框架获取toast内容
        driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.home=PageHome(driver)
    def test_hello(self):
        # 发现find_element_with_scroll（）在page_home中没有定义，但为什么没出错？
        # 因为在base定义了，home继承了，所以调用home调用了base的
        # 所以TestDome这个类不用继承base也能调用滑动查找方法，也不用在page页写相关动作
        # （我们写代码的思维是base page 都要写，这里没写page，因为这里是检测而已，demo而已，减少不必要麻烦）

        self.home.find_element_with_scroll((By.XPATH,"//*[@text='关于手机']"))
