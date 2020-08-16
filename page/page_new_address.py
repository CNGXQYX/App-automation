import random
import time

import page
from base.base_action import BaseAction

class PageNewAddress(BaseAction):
    def input_receipt(self,text):
        self.input(page.receipt_name,text)

    def input_phone(self,text):
        self.input(page.phone_address,text)

    def input_detailed_address(self,text):
        self.input(page.detailed_address,text)

    def input_post(self,text):
        self.input(page.post_code,text)

    def click_defaul(self):
        self.click(page.defaul_address)

    def click_region(self):
        self.click(page.choose_region)

    def click_save(self):
        self.click(page.save_button)



    # 为什么在页面层，不在base层？
    # 随机选择地址。用一个循环，循环点击，直至选完。不同地区，点击次数不一样，如东莞市，其下没有可选地址，南宁市，其下还有县级镇级可选，循环次数不确实
    # 发现添加地址信息界面和选择省市界面是不一样的，而选完之后，会自动跳回添加地址信息页，所以判断界面名是否一样来退出循环
    # 怎么随机点击？发现省市区的页面中，省市区的ID都是一样的，所以每一次循环都执行获取所有相同id元素，然后算出有多少个，作为随机数产生范围，作为点击元素的下标

    # 进入选择地区，随机选择区域
    def choose_region(self):
        self.click_region()
        while True:
            if self.driver.current_activity!=page.new_address_activity:
                # 不滑动的话，永远是选择前面的
                self.scoll_index(5)
                # 将相同特征元素找出来，得到列表
                areas=self.find_elements(page.area_feature)
                # 是len不是lan
                areas_count=len(areas)
                # 产生列表下标
                areas_index=random.randint(0,areas_count-1)
                areas[areas_index].click()
            else:
                return
            # 点击之后可能动画什么的，所以给个时间，要不然，容易程序出错，说TimeoutException
            # 找元素没问题，因为它有时间等待，问题在获取界面名上，切换过程，获取界面可能出错
            time.sleep(1)




