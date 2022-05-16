from time import sleep

import mall4
from mall4.pomall4.Base.base import base


class pageProDetails(base):
    def __init__(self,driver):
        self.driver = driver
#选商品要加进来吗？
    ##选规格  非默认
    def page_proType(self):
        #规格有一个的话 未激活的没有 那就不选规格
        # 两个的话 未激活的有一个
        # note:三个的话 未激活旧有多个 暂取第一个
        if base(self.driver).base_eleIsExit(mall4.loc_proType):
             self.base_find_element(mall4.loc_proType).click()

    #加数量 一个一个加
    def page_proCountincr(self,num): #num指的是输入框的值 还是点击数 选点击数
        # num 取绝对值遍历  若是负数 绝对值与num不想等
        for n in range(1,num):
            self.base_find_element(mall4.loc_num_incr).click()
    def page_proCountdesc(self,num):
        # num 取绝对值遍历  若是负数 绝对值与num不想等
        for n in range(num,0):
            self.base_find_element(mall4.loc_num_desc).click()
    def page_proCountinput(self, loc,num):
        self.base_input(loc,content=num)
    # 加购
    def page_proCart(self):
        self.base_find_element(mall4.loc_addCart).click()

#立即购买
    def page_proBuy(self):
        self.base_find_element(mall4.loc_buy).click()
        #订单

#收藏
    def page_collect(self,collect_btn):# 有collect和collect active来区别当前商品状态
        self.base_find_element(collect_btn).click()

#组装
    def zuzhuangCart(self,loc,num):
        self.page_proType()
        # if num<0:
        #     self.page_proCountdesc(num)
        # else:
        #     self.page_proCountincr(num)
        self.page_proCountinput(loc,num)
        self.page_proCart()
    def zuzhuangBuy(self,loc,num):
        self.page_proType()
        self.page_proCountinput(loc,num)
        self.page_proBuy()
    def zuzhuangCollect(self,collect_btn):
        sleep(1)
        self.page_collect(collect_btn)
        sleep(1)

