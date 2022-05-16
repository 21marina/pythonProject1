import logging
import threading
import unittest

from ddt import file_data, ddt, unpack

import mall4
from mall4.requestsTest.intercase.api.baseApi import baseApi
from mall4.requestsTest.intercase.tools.getLogger import getLogger

@ddt
class apiYewu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = getLogger().get_logger()
        getLogger().getlogFileFormater(logger=cls.log, level=logging.INFO,
                                       fileName=mall4.filePath.format("yewuCase"), frm=mall4.frm)
        cls.baseApi = baseApi()
        cls.token = None
        cls.orderIds=None

    @classmethod
    def tearDownClass(cls):
        print("业务teardownclass")

    # @file_data(mall4.IFyewuymlDataLoc)
    # @unpack
    # def test_1yewu(self, **kwargs):
    #     # 正向登录-选商品详情-立即购买-生成订单-提交订单-去支付
    #     print("kwstart is:" + str(kwargs))
    #     l=self.ss(kwargs,"login")
    #     self.ss(l,"proInfo")
    #     self.ss(l,"confirm")
    #     self.ss(l,"submit")
    #     self.ss(l,"order")
    #
    # def ss(self, ll,key):
    #     l=ll[key]
    #     url = l["url"]
    #     method = l["method"]
    #     header = l["header"]
    #     paramOrdata = l["data"]
    #     header['Authorization'] = self.token
    #     if "orderIds" in l["data"].keys():
    #         l["data"]["orderIds"] = self.orderIds
    #     re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,
    #                               contentType="application/json")  # 传字典即可 无需转json传
    #     print(re.json())
    #  #.keys() 类型dict_keys
    #     if re.json()["data"] is not None: #当data:None时 .keys是NoneType无法in 所以保错 AttributeError: 'NoneType' object has no attribute 'keys'
    #         if type(re.json()["data"]) is not list:
    #             if type(re.json()["data"]) is not str:
    #                 if "accessToken" in re.json()["data"].keys():
    #                     #python判断字典中key存在 d.has_key("name)【python2.2之前】 或 "name" in d.keys()
    #                     #提交订单的时候 返回的data是个订单表编号的数组 数组list无keys属性
    #                     #取支付时  返回的是str的form表单  无keys属性
    #                     self.token=re.json()["data"]["accessToken"]
    #     #提交订单后返回的订单id值要传给支付接口  #先取再赋值
    #     # print("type(re.json()['data'])"+str(type(re.json()["data"])) )#字典
    #     # print("re.json()['success']"+str(type(re.json()["success"]))) #bool
    #     if type(re.json()["data"]) is list and re.json()["success"] is True:
    #         #取值
    #         self.orderIds=re.json()["data"]
    #         print("orderIds"+str(self.orderIds))
    #     try:
    #         self.assertEqual(re.json()['code'], "00000")
    #         self.assertEqual(re.json()['success'], True)
    #         self.log.info(l["desc"] + "   响应码+success断言成功 ")
    #     except AssertionError:  # 若断言有异常 记录异常日志
    #         self.log.info(
    #             l["desc"] + "响应码+success断言失败 " + "code是(实际，期望)：" + re.json()['code'] + "," + l["result"]["code"])  # 不能是布尔型
    #         raise
    #     return ll

#     @file_data(mall4.IFyewuymlDataLoc)
#     @unpack
#     def test_2yewu(self, **kwargs):
#         print("yewuTest")
#         # 正向登录-选商品详情-立即购买-生成订单-提交订单-去支付
#         print("kwstart is:" + str(kwargs))
#         l = kwargs["login"]
#         url = l["url"]
#         method = l["method"]
#         header = l["header"]
#         paramOrdata = l["data"]
#         re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,
#                                       contentType="application/json")
#         print(re.json())
#         to=re.json()["data"]["accessToken"]
#
#         l = kwargs["proInfo"]
#         url = l["url"]
#         method = l["method"]
#         header = l["header"]
#         paramOrdata = l["data"]
#         header['Authorization'] = to
#         re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,
#                                   contentType="application/json")
#         print(re.json())
#         l = kwargs["confirm"]
#         url = l["url"]
#         method = l["method"]
#         header = l["header"]
#         paramOrdata = l["data"]
#         header['Authorization'] = to
#         re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,
#                                   contentType="application/json")
#         print(re.json())
#         l = kwargs["submit"]
#         url = l["url"]
#         method = l["method"]
#         header = l["header"]
#         paramOrdata = l["data"]
#         header['Authorization'] = to
#         re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,
#                                   contentType="application/json")
#         print(re.json())
#         orderId = re.json()["data"]
#         l = kwargs["order"]
#         url = l["url"]
#         method = l["method"]
#         header = l["header"]
#         header['Authorization'] = to
#         # l["data"]["orderIds"] = self.orderIds
#         paramOrdata = l["data"]
#         paramOrdata["orderIds"] = orderId
#         re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,
#                                   contentType="application/json")
#         print(re.json())
#
# if __name__ == "__main__":
#     # thread = threading.Thread(target=action).start()
#     unittest.main()