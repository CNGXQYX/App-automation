

from appium import webdriver

#这里没有单例设计？
def init_driver(no_reset=True):
    desired_caps = dict()
    desired_caps['platformName'] = 'android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '1'
    desired_caps['appPackage'] = 'com.yunmall.lc'
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    # 关键字：noResete和值：no_rest
    #  no_reset参数为True时，不重置应用
    desired_caps['noReset'] = no_reset
    #告诉appium使用uiautomator2框架获取toast内容
    desired_caps['automationName'] = 'Uiautomator2'
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)


    return driver
