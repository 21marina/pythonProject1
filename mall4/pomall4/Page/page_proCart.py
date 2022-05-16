from time import sleep

from selenium.webdriver.common.by import By

import mall4
from mall4.pomall4.Base.base import base


class pageProCart(base):
    def __init__(self,driver):
        self.driver = driver

    # 单击事件  点击购物车图标  去结算订单
    def page_proClick(self ,loc):
        # self.base_find_element(loc).click()
        self.base_click(loc)
        print("点击购物车图标 成功")
    def page_proClickjs(self ,loc):
        self.driver.execute_script("arguments[0].click();", self.base_find_element(loc))
        print("点击购物车图标js 成功")
    #购物车挑选商品 以待去结算  默认有上次勾选的 所以先双击全选 在选自己想要的
    def page_proCart(self):
        print("挑选商品开始 即将全选")
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.base_find_element(mall4.loc_all_btn))
        self.base_find_element(mall4.loc_all_btn).click()
        sleep(1)
        # self.base_click(mall4.loc_all_btn)#全选
        self.base_click(mall4.loc_all_btn)#取消全选
        #找到复选框 判断有无被选 若有选 不选 如未选 点击
        print("挑选商品开始 取消全选 即将选美容仪")
        if self.base_eleIsExit(mall4.loc_pro_carted):#已选
            pass
        else:
            self.base_click(mall4.loc_pro_cart)
        print("挑选商品 选择完商品")
        sleep(1)
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.base_find_element(mall4.loc_all_btn))

    #校验购物车单个商品信息中的数量 单价 小计是否正确
    def page_checkInfo(self,price,num,countPrice):
        # price=self.base_find_element(locPrice).text
        # num=self.base_find_element(locNum).text
        # countPrice=self.base_find_element(locCount).text
        if float(countPrice[1:]) == float(price[1:]) * float(num):
            return True
        print("num is:"+num)
        return False
    def checkInfo(self):
        #遍历购物车的每个item 里的每个商品
        # li=self.base_find_elements(mall4.loc_pro_cartDiv)
        print("driver"+str(self.driver))
        li=self.driver.find_elements(By.CLASS_NAME,"//*[@class='cart-con']")#???
        print("list is:"+li)
        for i in li:
            print("ele is:" + str(i))
            # e=i.find_element(By.CLASS_NAME,"discount-con")
            # ee=e.find_element(By.CLASS_NAME,"discount-prod")
            # eee = ee.find_element(By.CLASS_NAME, "item")
        # for i, goods in enumerate(li):
        #         print("索引i："+i+"goods:"+goods)
        #         locprice = goods.find_element_by_css_selector("div div.discount-con div.discount-prod div.item div.tab-price div").text  # 商品名
        #         locnum = goods.find_element_by_css_selector("div div.discount-con div.discount-prod div.item div.tab-number div input").text  # 商品名
        #         locCount = goods.find_element_by_css_selector(
        #             "div div.discount-con div.discount-prod div.item div.tab-total").text  # 商品名
        #         # href = goods.find_element_by_css_selector("a.title").get_attribute("href")  # 地址
        #         self.page_checkInfo(locprice,locnum,locCount)

#组装
    def zuzhuangCartPage(self):
        #点击购物车图标 #校验价钱计算是否正确 #勾选购物车商品 #点击去结算
        # self.checkInfo()
        sleep(1)
        self.page_proCart()
        print("即将去结算")
        sleep(1)
        self.page_proClickjs(mall4.loc_submit_btn)
        sleep(2)
        # self.page_proOrder()



