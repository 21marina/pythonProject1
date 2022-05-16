from time import sleep

import mall4
from mall4.pomall4.Base.base import base


class pageOrder(base):
    def __init__(self,driver):
        self.driver = driver

    def page_proAddr(self):
        pass
        #默认地址什么也不干  新增地址 或编辑地址
        # if base(self.driver).base_eleIsExit(mall4.loc_proType):
        #  self.base_find_element(mall4.loc_addDetail).click()
        #
    def page_projifen(self,loc=mall4.loc_jifendisc_select,num=0):
        #勾选使用积分 有的商品有  有的没有
        if self.base_eleIsExit(mall4.loc_jifendisc_select):
            self.base_find_element(mall4.loc_jifendisc_select).click()
            self.base_input(loc,num)
    # 下订单
    def page_proOrder(self,loc):
        self.driver.execute_script("arguments[0].click();", self.base_find_element(loc))
        # self.base_find_element(mall4.loc_submit_btn).click()


#组装
    def zuzhuangOrder(self,loc,num):
        #地址(2) #支付方式 #积分(2) #配送方式 #商品信息详情 #点击提交
        self.page_proAddr()
        self.page_projifen(loc,num)
        self.page_proOrder(mall4.loc_submit_btn)

