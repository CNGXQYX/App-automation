import page
from base.base_action import BaseAction


class PageSetting(BaseAction):

    def click_about_out(self):
        # 这里之前忘记加click，脚本总是失败(但是不是程序失败，看控制台时一定要分清楚，这样有利于找问题)，没点击，
        # 但是该代码没问题，也找到了元素它得到了调用滑动查找所返回的元素，但是没点击，页面没进入下一个页面，脚本的后一句代码是在下一个页面滑动查找，就会找不到元素，滑动到底，打印“到底了”
        # 所以这个打印到底了，在测试流程中，不是第一句滑动查找点击元素脚本代码打印的，是第二句脚本代码打印的
        self.find_element_with_scroll(page.about_out_button).click()
    def click_clear_cache(self):
        self.find_element_with_scroll(page.clear_cache_button).click()

    def click_address(self):
        self.find_element_with_scroll(page.address_administration_button).click()
