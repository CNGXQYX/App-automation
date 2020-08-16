import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import page


class BaseAction():

    # __init__和base_get_driver中init的区别
    def __init__(self,driver):
        self.driver=driver

    #     自己定义的函数括号里的参数可以自己写，根据自己需求，写多少个都行，名字也可以自己取
    # self不是参数，别人调用她时，不用想着写一个self上去
    def find_element(self,feature,timeout=10,poll_frequency=1.0):
        by = feature[0]
        value = feature[1]
        # 一定注意WebDriverWait都是大写开头
        # 自带的类或方法什么的，括号内的属性是固定的，不能自己取个名字放进去
        # 都是括号里的东西，一个是参数，一个是属性，记住了
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x: x.find_element(by,value))
    # 不仅finde_lement加s，until里面也加s！！！！！！！！！！！！！！！！！！！
    def find_elements(self,feature,timeout=10,poll_frequency=1.0):
        by = feature[0]
        value = feature[1]
        # 一定注意WebDriverWait都是大写开头
        # 自带的类或方法什么的，括号内的属性是固定的，不能自己取个名字放进去
        # 都是括号里的东西，一个是参数，一个是属性，记住了
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x: x.find_elements(by,value))

    # 点击元素，就要找元素，肯定是要传入元素特征，通过参数传递，那么给个参数feature
    # 为什么不给timeout这个参数呢,不写的话，到时候脚本想传查找延迟的时间怎么传？那得调用find_element
    # 不写timeout是因为我们设计脚本调用click不能改时间延迟
    def click(self,feature):
        # 同是函数里面的代码,为什么15行用self.driver，这里用self呢？
        # 因为上面属性是driver,而这里是对象调用方法,当然是self了.搞清楚self是个什么东西
        self.find_element(feature).click()

    def input(self,feature,text):
        self.find_element(feature).send_keys(text)

    def get_text(self, feature):
        return self.find_element(feature).text

    def is_toast_exist(self,message):
#         是否存在，说明要返回 是 或 否 ，要通过查找元素来判断方法才能知道是否找到，找到程序没问题，单找不到程序就报错了
# 所以要想到用捕获异常来解决程序报错的问题
         #查找的方法和元素特征,熟记下面包含和%s的写法
# toast的特征是有text的，所以从text入手即可，不用想其他特征
        message_xpath=By.XPATH,"//*[contains(@text,'%s')]"%message
        try:
            # message.xpath不用self点吗？自己函数下的属性肯定不用了。调用时才用到点
            # 频率自己设了浮点数，那么上面的find_element也要设为浮点数，要不然报错
            # 找toast频率一定得快，要不然消失了
            self.find_element(message_xpath,5,0.1)
            # True False 用的都是大写开头
            return True
        # 找不到当然是时间异常了TimeoutError
        except TimeoutError:
            return False
#     登录页面用不到，但是先封装，其他会用到
#     获取要分toast存在的情况和toast不存在的情况，所以用if
#     存在 才能找得到并且返回文本
#     不存在 则得抛异常（get_toast_text这个方法是获取文本，那你既然获取不到文本，那不就是异常吗，所以抛异常）
    def get_toast_text(self,message):
        message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
        if self.is_toast_exist(message):
            # 记得text
            return self.find_element(message_xpath,5,0.1).text
        else: raise Exception('toast未出现，请检查参数是否正确或者toast是否出现在屏幕上')

    def scroll_page_one_time(self,direction='up'):

        #         通过坐标滑动，坐标不写死。
        #         针对不同手机、软件，和上下导航栏遮挡问题，计算出可滑动的坐标点
        #         获取当前手机分辨率，计算出上下左右四点
        #         上下点选择四分之一和四分之三的位置，避开上下导航栏。左右两点也是
        #           封装不同方向的滑动，传参direction 进行选择滑动方向
        #
        width=self.driver.get_window_size()['width']
        height=self.driver.get_window_size()['height']

        center_x=width/2
        center_y=height/2

        left_x=width/4*1
        left_y=center_y
        right_x=width/4*3
        right_y=center_y
        top_x=center_x
        top_y=height/4*1
        bottom_x=center_x
        botoom_y=height/4*3

        #       封装不同方向的滑动
        # 从下往上
        if direction=='up':
            # 防止惯性，时间给大一点，3秒
            self.driver.swipe(bottom_x,botoom_y,top_x,top_y,3000)
        if direction=='down':
            self.driver.swipe(top_x,top_y,bottom_x,botoom_y,3000)
        #     从左往右
        if direction == 'right':
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)

        if direction == 'left':
            self.driver.swipe(right_x, right_y,left_x, left_y, 3000)
    # 封装随机次数滑动
    def scoll_index(self,num):
        page_source=''
        # 产生随机数
        index=random.randint(0,num)
        i=0
        while i<index:
            self.scroll_page_one_time()
            # 加sleep是等滑动结束，要不然获取的page_source会变化,好像也可不加。
            if self.driver.page_source==page_source:
                # 用return才能退出循环，break退不出
                return
            page_source=self.driver.page_source
            # i=+1代码没错，但没有加的效果，一定不要写错，到时候循环退不出，只能等到滑到底才能退出！
            i += 1


    #封装边滑边找的方法，只是找元素，对元素进行什么动作不写，返回元素就好了
    # 记得传参数：feature元素特征和查找方法  还有方向directon，记得是给默认值，默认值的话，别人调用它，可传参也可不传参,但是自己函数下调用，就得传参，如下面
    def find_element_with_scroll(self,feature,directon='up'):
        # 不同手机，软件，还有找的元素位置不同，不知道要滑多少次，所以写一个死循环，找到即停止，滑到底也停止
        # 找不到元素，程序会报错，不执行了，所以在这里用一个捕获异常，这样就不会导致不执行
        # 定义一个变量接收page_source

        page_source=''
        while True:
            try:
                # 有return了就不用写break退出了
                return self.find_element(feature)
            except Exception:
                self.scroll_page_one_time(directon)
                # 判断是否到底，到底就退出
                # 用break退出
                if self.driver.page_source==page_source:
                    print('到底了')
                    break
                else:
                    page_source=self.driver.page_source

    # 在加入vip页面中，输入验证码，有个类似toast的弹出来，为什么不是toast呢，这个系统toast在底部显示，然而这里在中间显示，
    # 一般按程序设计的统一性，如果都是toast，不可能一个在底部，一个在中间
    # 它其实是仿toast写的div标签，当弹窗弹出来时，看chrome调试工具，HTML中会看到看到div标签出现，弹窗消失，HTML中的div也不见
    #瞬间出现然后消失，我们看不到div的内容，怎么确定，弹窗弹窗且内容与我们预期一样呢？
    #输入hello， 打印page_source（打印前给两秒延时）看看里面有什么，发现有“请输入正确验证码”
    # 所以通过在找相应内容是否在page_source中，判断弹窗内容是否符合预期
    # 要有查找时间和频率还有预期内容的参数
    # ***********************！！！！！！！！！！！！
    # 频率要尽可能低，div转身即逝，频率太慢，查找的age_source中的div就没有预期内容，因为page_source变成了没有弹窗的page_source
    # ***********************！！！！！！！！！！！！
    def is_keyword_in_page_source(self,keyword,timeout=10,poll=0.1):
        # time.time()是当前时间戳,timeout是接收参数的
        end_time=time.time()+timeout
        while True:
            if end_time<=time.time():
                # 这个封装是用来脚本中断言的，所以要返回True或False,不要只return或者break
                return False
            if keyword in self.driver.page_source:
                return True
            # poll是接收参数的
            time.sleep(poll)













