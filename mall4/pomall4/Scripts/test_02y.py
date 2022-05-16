import json
import logging
import unittest
from time import sleep

import requests
from ddt import ddt, data, unpack, file_data

import mall4
from mall4.pomall4.Page.page_index import pageIndex
from mall4.pomall4.Page.page_login import pageLogin
from mall4.pomall4.Page.page_proCart import pageProCart
from mall4.pomall4.Page.page_proDetails import pageProDetails
from mall4.pomall4.Base.base import base
from mall4.pomall4.Page.page_proOrder import pageOrder
from mall4.pomall4.tools.getLogger import getLogger
from mall4.pomall4.tools.get_driver import getDriver
import urllib

@ddt
class test02y(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.pageLogin01=pageLogin01# 要加括号 不加的话是获取的类 加完括号是获取的类对象 类对象可调取其方法
        print("setupclass")
        #传入封装好的driver
        cls.driver= getDriver().get_driver()#？？？这个driver和类属性driver有啥关系
        #获取加购界面page对象  调用时要么是self.pageProDetails.zuzhuang  要么是pageProDetails（self.driver）
        cls.pageProDetails=pageProDetails(cls.driver)
        cls.pageSearch=pageIndex(cls.driver)
        print("setupending")
        cls.Token=None
        cls.log = getLogger().get_logger()
        getLogger().getlogFileFormater(logger=cls.log, level=logging.INFO,
                                       fileName=mall4.filePath.format("test02y"), frm=mall4.frm)
        test02y().getLogin()#cls.getLogin()会提示缺少self参数
        cls.base_url = "https://cloud-pc.mall4j.com/"
        cls.pageOrder=pageOrder(cls.driver)
        cls.pageProCart=pageProCart(cls.driver)
    @classmethod
    def tearDownClass(cls):
        print("teardownclass")
        getDriver().quit_driver()
#     @unittest.skip("search skip")
    @file_data(mall4.searchymlDataFileLoc)
    @unpack
    def test02_search(self, **kwargs):
        #Q：???当商品用例走完最后一个为-3  下一个用例切换为店铺的空 send空 但是url的值还会是上一个-3
          # con=content if content is None else "NULL"
        content = kwargs.get("content")
        type = kwargs.get("type")
        exceptedValue = kwargs.get("result")
        print("type:"+type+" exceptedValue："+exceptedValue)
        self.pageSearch.zuzhuang(content,type)
        #断言 空的时候断言消息框 非空搜索后的url与期望值做比较  断言数据库返回的数据
        if base(self.driver).base_eleIsExit(mall4.loc_msgbox_top):#元素一直存在吗 第二个用例页进来
            print("aa"+base(self.driver).base_find_element(mall4.loc_msgbox_top).text)
            self.opResult(mall4.loc_msgbox_top, exceptedValue)
        else:
            print("else 语句")
            sleep(1)
            value=self.driver.current_url  #和zuzhuang函数是并行 所以显示跳转前url 真实是ascii类似%253D%25E4%25B8
            strList = value.split('=')
            value=strList[0]+"="+urllib.parse.unquote(strList[1], encoding="utf-8")
            print("value url is:"+value+"......."+exceptedValue)
            self.assFunc(value, self.base_url+exceptedValue)
    # @unittest.skip("test02_addCart")
    @file_data(mall4.addCartNumymlDataLoc)
    @unpack
    def test02_addCart(self, **kwargs): #显示查询结果列表下的页数切换
        numContnet = kwargs.get("content")
        exceptedValue = kwargs.get("result")
        if numContnet=="stock":
            if base(self.driver).base_eleIsExit(mall4.loc_num_stock):
                stock=base(self.driver).base_find_element(mall4.loc_num_stock).text
                numContnet=stock#给购物车数量如何获取???
                print(numContnet+" stock exceptedValue：" + exceptedValue)
                #库存247 填写247旧提示库存不足 因为购物车有一些   所以这个最大输入值应该是 库存量-购物车数量
            else:
                numContnet="9999" #暂定最大库存量为9999
        print(numContnet+" exceptedValue：" + exceptedValue)
        base(self.driver).base_find_element(mall4.loc_pro).click() #找到商品进商品详情页
        self.pageProDetails.zuzhuangCart(mall4.loc_num_input,numContnet)
        #v=v.replace(/[^\d]/g,'')
        # //是界定符g全局标志   ^有限定开头+反向字符两个用处 一般是带[]的字符串中内表示取反
        # 正则替换所有的'/'字符写法 replace(/\//g, '') \转义
        # 获取商品元素 #进入商品详情  #选规格 加数量
        # 加入购物车断言  判断msg加购成功元素是否存在 存在可断言成功 不存在？？？暂记录日志
        if base(self.driver).base_eleIsExit(mall4.loc_msgaddCart):
            sleep(1)
            self.opResult(mall4.loc_msgaddCart,exceptedValue) #断言包含其中
        else:
            self.log.info("addCart 无成功提示msg")
#
#
# # 注册要验证码 暂不自动化
# #     @file_data(mall4.regymlDataFileLoc)
# #     @unpack
# #     def test02_reg(self, **kwargs):
#
# #     @unittest.skip("暂跳过")
# #     def test02_index(self):
# #         ele=base(self.driver).base_find_element(mall4.loc_pro).click()
#         #先滚动屏幕  居然无需滚屏  #点击美容仪图片
#     @unittest.skip("跳过test02_Buy")
    @file_data(mall4.addCartNumymlDataLoc)
    @unpack
    def test02_Buy(self,**kwargs):
        numContent = kwargs.get("content")
        exceptValue=kwargs.get("result")
    # 获取商品元素 进入商品详情 选规格 加数量  # 立即购买 # 加断言
        base(self.driver).base_find_element(mall4.loc_pro).click()
        if numContent == "stock":
            if base(self.driver).base_eleIsExit(mall4.loc_num_stock):
                stock=base(self.driver).base_find_element(mall4.loc_num_stock).text
                numContent=stock #暂定最大值 应该为库存量-购物车数量
            else:
                numContent="9999" #暂定最大库存量为9999
        self.pageProDetails.zuzhuangBuy(mall4.loc_num_input, numContent)  # 立即购买之后跳转订单页 怎么断言
        if base(self.driver).base_eleIsExit(mall4.loc_msgaddCart):  # 没存在 说明点击立即购买没有成功  断言
            sleep(1)
            self.opResult(mall4.loc_msgaddCart, exceptValue)
            self.log.info("Buybyprod 商品-立即购买失败 但断言成功 提示请输入正确的商品数量 预期也是")
        elif base(self.driver).base_eleIsExit(mall4.loc_detail_num):
            sleep(1)
            if self.isfushu(numContent):#true 说明是整数或负数  字符串进不来
                self.opResult(mall4.loc_detail_num, str(abs(int(numContent))))
            #断言包括对整个订单信息的断言 现只做数量断言
            #当前在订单页  还需再回到商品详情页进行下一个用例 注意是回到首页在进入商品详情页
            # self.driver.back()#返回 forward refresh
            self.driver.get("https://cloud-pc.mall4j.com/")
#
#     @unittest.skip("暂跳过")
    def test02_collect(self):
        base(self.driver).base_find_element(mall4.loc_pro).click()
        if base(self.driver).base_eleIsExit(mall4.loc_collected_btn):
            sleep(1)
            value= base(self.driver).base_find_element(mall4.loc_collected_btn).text
            print("yishoucang :"+value)
        elif base(self.driver).base_eleIsExit(mall4.loc_collect_btn):# 无论collect是否active 都只会捕捉到collect 不能区分收藏状态
            sleep(1)
            value= base(self.driver).base_find_element(mall4.loc_collect_btn).text
            print("未shoucang :" + value)
        print("value:"+value)
        if value=="取消收藏":
                exceptValue="已取消收藏" #商品的当前收藏状态:已收藏 点击完之后未收藏 反馈信息为已取消收藏
        elif value=="收藏商品":# 未收藏
                exceptValue="已添加收藏"
        print("collect exceptValue is:"+exceptValue)
        pageProDetails(self.driver).zuzhuangCollect(mall4.loc_collect_btn)
        #先获取提示信息 再断言 若无提示 记录日志
        if base(self.driver).base_eleIsExit(mall4.loc_msgaddCollect):
            self.opResult(mall4.loc_msgaddCollect, exceptValue)
        else:
            self.log.info("商品-收藏失败 没有弹出提示框")


#引用带文件的方法 会读取到其文件吗
    def test02_order1(self, **kwargs):
        # 点击购物车图标 购物车结算生成订单
        self.pageProCart.page_proClick(mall4.loc_cart_top)
        sleep(1)
        exptValue=self.driver.current_url#首页
        self.pageProCart.zuzhuangCartPage()
        sleep(1)
        # 断言
        # ???购物车点击去结算没反应 普通click显示元素不可达 js的click无反应
        value=self.driver.current_url #只要真实的urlvalue不等于现在的url 即认为成功
        if exptValue!=value:
            self.log.info(value + ":real url value assert success excptValue is:"+exptValue)
        else:
            self.log.info(value + ":real url value assert fail")

    @file_data(mall4.jifenymlDataLoc)
    @unpack
    def test02_order2(self,**kwargs):
    # 立即购买生成订单     # 选商品 点击结算 下订单（地址+折扣+商品详情）
        numContent=kwargs.get("content")
        exptValue=kwargs.get("result")
        self.driver.get("https://cloud-pc.mall4j.com/detail/155")
        #立即购买
        base(self.driver).base_find_element(mall4.loc_buy).click()
        self.pageOrder.zuzhuangOrder(mall4.loc_jifendisc_input,numContent)
    #断言
    #传的空 字符 中文 特殊字符 实际值￥0.00  #传超过最大值 实际值￥0.00 #传负数 实际值绝对值
        if numContent=="stock":
            if base(self.driver).base_eleIsExit(mall4.loc_jifendisc_max):
                #获取当前商品订单可抵扣的最大值 大于此值时会是此值
                numContent = base(self.driver).base_find_element(mall4.loc_jifendisc_max).text #（该订单最多可用 9 积分）
                numContent= list(filter(str.isdigit,numContent))
                numContent=str(int(numContent[0]) + 1) #输入比当前可抵扣数额大一的值
            elif base(self.driver).base_eleIsExit(mall4.loc_jifendisc_maxAccount):#还有一个账户最大可用值
                numContent = base(self.driver).base_find_element(mall4.loc_jifendisc_maxAccount).text#账户共 2001 积分，本次使用
                numContent = list(filter(str.isdigit, numContent))
                numContent = str(int(numContent[0]) + 1)
            else:
                numContent="9999"
        sleep(2)
        if self.isfushu(numContent):  # true 说明是整数或负数  字符串进不来
            if exptValue is None: # 超过可抵扣最大值 断言 实际值为max
                # #但实际上大于库存值时send不进去 所以默认为￥0.00
                self.opResult(mall4.loc_jifendisc_disc, '￥0.00')
            else:  # stock的预期值为空 真实值会变成最大值
                self.opResult(mall4.loc_jifendisc_disc,'￥'+str(abs(int(numContent)))+'.00')
        else:
            self.opResult(mall4.loc_jifendisc_disc, exptValue) #预测值和content值差不多

    @file_data(mall4.caseyewuDataLoc)
    @unpack
    def test_yewu1(self,**kwargs):#切记是双星
        content=kwargs.get("searchContent")
        proType=kwargs.get("searchType")
        numContent=kwargs.get("numCount")
        numjfContent=kwargs.get("numjfCount")
        # 登录成功-搜索商品-选商品-立即购买
        self.pageSearch.zuzhuang(content, proType)#输入-点击搜索
        self.log.info("搜索框输入-点击搜索")
        base(self.driver).base_find_element(mall4.loc_pro).click() #进入商品详情
        self.log.info("进入商品详情")
        self.pageProDetails.zuzhuangBuy(mall4.loc_num_input, numContent)#输入数量 立即购买
        self.log.info("输入数量 立即购买")
        self.pageOrder.zuzhuangOrder(mall4.loc_jifendisc_input, numjfContent)
        self.log.info("输入积分抵扣 提交订单")
        #断言


    # def test_yewu2(self):
    # 登录成功-购物车-选商品-去结算  同上述test02_order1

                # 断言相等
    def assFunc(self, value, exceptedValue):
      with self.subTest(value=value):
                try:
                    self.assertEqual(value, exceptedValue)
                    self.log.info(value + "value assert success")
                except AssertionError:
                    self.log.info("body error,实际body is %s,expected_body is %s" % (value, exceptedValue))
                    raise
    def opResult(self, elePath, exceptedValue):
        value= base(self.driver).base_find_element(elePath).text
        print("opresult assert value:"+value)
        self.assFunc(value, exceptedValue)
    # def getTokenByReq(self):
    #     url = "https://cloud-api.mall4j.com/mall4cloud_auth/ua/login/"
    #     header = {"Content-Type": "application/json"}
    #     data = {"username": "13213818483", "password": "123456"}
    #     re = requests.post(url,headers=header,json=data)
    #     # {'msg': None, 'fail': False, 'code': '00000', 'data': {'expiresIn': 2592000,
    #     #                                                        'accessToken': 'Kz6WVi3MA1OAgKNQXygu9cabjUPsG/DJRFyi2jaf6aSvynuDU0h+QEdx0aEVg8FZ',
    #     #                                                        'refreshToken': 'o5mljedpWKlR4QyoCXgHi+jYnweWu0cjMvZjo/DzoVmvynuDU0h+QEdx0aEVg8FZ'},
    #     #  'success': True}
    #     self.Token=re.json()["data"]["token"]
    def getLogin(self):
        userName="13213818483"
        pwd="123456"
        base(self.driver).base_find_element(mall4.loc_denglulink).click()
        pageLogin(self.driver).zuzhuang(userName, pwd, mall4.loc_username, mall4.loc_pwd, mall4.loc_denglusub)
    def isfushu(self,str): #判断是否为整数或负数
        try:
            num = int(str)
            return isinstance(num, int) #str.isdigit()来做，输入正整数没问题
        except ValueError:
            return False

# if __name__=="__main__":
#     unittest.main()