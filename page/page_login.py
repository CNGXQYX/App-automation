import page
from base.base_action import BaseAction


class PageLogin(BaseAction):

    """输入文本从test_传过来，所以给个text参数接收
      元素特征和方法不用从其他地方传，直接调用，所以不用在函数定义给参数接收
     input函数有一个接收元素特征和方法的参数，所以下面给他传（调用后作为参数传）,还有一个接收text的参数，也有给他传"""
    # class下第一个三引号是灰色，其余会变成绿色
    # 若输三个引号注释后，下面的def有问题,准确说是引号的第二行有问题，标红??????
    # 顶格输三个引号就会标红，与def对齐就不会
    def input_username(self, text):
        self.input(page.username, text)

    def input_password(self, text):
        self.input(page.password, text)

    def click_login(self):
        self.click(page.login_button)



