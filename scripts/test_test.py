
import time
from base.base_get_driver import init_driver
#为什么不用导 import pytest


class TestTest:
    def setup(self):
        # from导的包可以不要包名.函数  可以直接函数
        print('准备获取driver')
        self.driver = init_driver()
        print('已经获取:',self.driver)

    def teardown(self):
        print('准备关闭driver')
        self.driver.quit()
        print('已经关闭driver')

    # 与上面一模一样，为什么这个不执行，不仅不是最后执行，而且也不是顺序执行，直接是不执行
    # teardown写成m了
    # 所以程序显示拼写错误是有用的，直接看单词有没有拼错！！！！，不要考虑其他！！！！
    # def teardowm(self):
    #     print('准备关闭driver')
    #     time.sleep(5)
    #     self.driver.quit()
    #     print('已经关闭driver')

    def test_test(self):
        print('初始化设置')

