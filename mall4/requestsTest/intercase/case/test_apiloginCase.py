# ## 业务层 使用unittest框架 调用api对象 记得继承TestCase
# ## 不涉及定位元素 只需接口数据
#
# ## 数据参数化可优化
# import json
# import logging
# import unittest
#
# import requests
# from ddt import ddt, file_data, unpack
#
# import mall4
# from mall4.requestsTest.intercase.api.baseApi import baseApi
# from mall4.requestsTest.intercase.tools.getLogger import getLogger
#
# @ddt
# class apiloginCase(unittest.TestCase):
#     # def __init__(self,token):
#     #     # global token
#     #     self.token = token #创建对象 调用函数指向__init__方法，属性self指向token
#     @classmethod
#     def setUpClass(cls):
#         print("setupclass")
#         # cls.driver = getDriver().get_driver()
#         cls.log = getLogger().get_logger()
#         getLogger().getlogFileFormater(logger=cls.log, level=logging.INFO,
#                                        fileName=mall4.filePath.format("apiloginCase"), frm=mall4.frm)
#         cls.baseApi=baseApi()
#         cls.token=None
#         cls.orderIds = None
#         # global Token
#         #请求示例
#         # url = "https://cloud-api.mall4j.com/mall4cloud_auth/ua/login"
#         # header = {"Content-Type": "application/json"}
#         # data = {"userName": "13213818483", "passWord": "fMsqf8ylUu3ZdYtUxxsx/SINVS5RLEqtx6ZVWJS3C/0=","sysType":0}
# # # print("header:"+"data:"+json.dumps(data))  #字典转json json.loads(data))  #json转字典
#     @classmethod
#     def tearDownClass(cls):
#         print("teardownclass")
#         # getDriver().quit_driver()
#
#     @classmethod
#     def setMytoken(cls, token):
#         cls.token=token
#     @file_data(mall4.IFloginymlDataFileLoc)
#     @unpack
#     def test_1login(self,**kwargs):#ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z。
#         url=kwargs.get("url") #url是str 读取的是json 要转字典吗???
#         header=kwargs.get("header")
#         data=kwargs.get("data") #在jmeter工具中也要加密   data 字典
#         desc=kwargs.get("desc") #type为str
#         exptValueCode=kwargs.get("result")["code"]
#         exptValueSucc=kwargs.get("result")["success"]
#         re=baseApi.sendRequests(url=url,method="POST",headers=header,paramOrdata=data,contentType="application/json")#传字典即可 无需转json传
#         #分析响应数据
#         print(re.json()) #内部第一个参数是期望值 第二个是实际值 参数我给传反了 但两值相等无所谓
#         # print(self.assertEqual(re.json()['code'],exptValueCode)) #返回None 就是断言成功true 但是有时候也是true 不能用true直接判断
#         try:
#             self.assertEqual(re.json()['code'], exptValueCode)
#             self.assertEqual(re.json()['success'],exptValueSucc)# 若断言无异常 认为断言成功记录日志加赋值Token
#             self.log.info(desc + "响应码+success断言成功 ")
#             #正向登录时能拿到token 其他逆向时拿不到
#             if re.json()["data"] is not None:  # 当data:None时 .keys是NoneType无法in 所以保错 AttributeError: 'NoneType' object has no attribute 'keys'
#                 if type(re.json()["data"]) is not list: #登录接口的data里有list None 字典
#                     # if type(re.json()["data"]) is not str:
#                         if "accessToken" in re.json()["data"].keys():
#                             t=re.json()['data']['accessToken']
#                             self.setMytoken(t) #setter方式注入值
#             # apiloginCase().token=re.json()['data']['accessToken'] #???赋值为空Nonetype #此处用self是局部 用类名
#         except AssertionError:# 若断言有异常 记录异常日志
#             self.log.info(
#                 desc + "响应码+success断言失败 " + "code是(实际，期望)：" + re.json()['code'] + "," + exptValueCode)  # 不能是布尔型
#
#         # if re.json()['data'] is None:
#         #     if re.json()['msg'] is None:
#         #         self.log.info("data块和msg块内容都为空 ")
#         #     else:
#         #         self.log.info("msg 内容是："+str(re.json()['msg']))
#         # else:
#         #     self.log.info("data 内容是："+str(re.json()['data']))
#         #     self.assertEquals(exptValuedata, re.json()['data'])
#             # ???本来想断言data响应 但token值每次生成不一致 如何断言
#
#
#     @file_data(mall4.IFsearchymlDataFileLoc)
#     @unpack
#     def test_2search(self, **kwargs):
#         url = kwargs.get("url")  # url是str 读取的是json 要转字典吗???
#         header = kwargs.get("header")
#         paramOrdata = kwargs.get("data")
#         desc = kwargs.get("desc")  # type为str
#         exptValueCode = kwargs.get("result")["code"]
#         exptValueSucc = kwargs.get("result")["success"]
#         #给header设置token值
#         header['Authorization']=self.token
#         print("header is："+str(header))
#         re = baseApi.sendRequests(url=url, method="GET", headers=header,paramOrdata=paramOrdata)  # 传字典即可 无需转json传
#         # 分析响应数据
#         print(re.json())  # 内部第一个参数是期望值 第二个是实际值 参数我给传反了 但两值相等无所谓
#         try:
#             self.assertEqual(re.json()['code'], exptValueCode)
#             self.assertEqual(re.json()['success'], exptValueSucc)  # 若断言无异常 认为断言成功记录日志加赋值Token
#             self.log.info(desc + "响应码+success断言成功 ")
#         except AssertionError:  # 若断言有异常 记录异常日志
#             self.log.info(
#                 desc + "响应码+success断言失败 " + "code是(实际，期望)：" + re.json()['code'] + "," + exptValueCode)  # 不能是布尔型
#     @file_data(mall4.IFprodetailymlDataFileLoc)
#     @unpack
#     def test_3proDetails(self, **kwargs):
#         url = kwargs.get("url")  # url是str 读取的是json 要转字典吗???
#         header = kwargs.get("header")
#         method=kwargs.get("method")
#         paramOrdata = kwargs.get("data")
#         desc = kwargs.get("desc")  # type为str
#         exptValueCode = kwargs.get("result")["code"]
#         exptValueSucc = kwargs.get("result")["success"]
#         # 给header设置token值
#         header['Authorization'] = self.token
#         print("header is：" + str(header))
#         re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata)  # 传字典即可 无需转json传
#         # 分析响应数据
#         print(re.json())  # 内部第一个参数是期望值 第二个是实际值 参数我给传反了 但两值相等无所谓
#         try:
#             self.assertEqual(re.json()['code'], exptValueCode)
#             self.assertEqual(re.json()['success'], exptValueSucc)  # 若断言无异常 认为断言成功记录日志加赋值Token
#             self.log.info(desc + "响应码+success断言成功 ")
#         except AssertionError:  # 若断言有异常 记录异常日志
#             self.log.info(
#                 desc + "响应码+success断言失败 " + "code是(实际，期望)：" + re.json()['code'] + "," + exptValueCode)  # 不能是布尔型
#     @file_data(mall4.IFaddCartNumymlDataLoc)
#     @unpack
#     def test_4addcart(self, **kw):
#         # url = kwargs.get("url")  # url是str 读取的是json 要转字典吗???
#         # header = kwargs.get("header")
#         # method=kwargs.get("method")
#         # paramOrdata = kwargs.get("data")
#         url=kw["url"] #传进来的是字典 可直接使用
#         header = kw["header"]
#         method = kw["method"]
#         paramOrdata = kw["data"]
#         # 给header设置token值
#         header['Authorization'] = self.token
#         print("header is：" + str(header))
#         re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,contentType="application/json")  # 传字典即可 无需转json传
#         # 分析响应数据
#         print(re.json())  # 内部第一个参数是期望值 第二个是实际值 参数我给传反了 但两值相等无所谓
#         self.opResult(re,kw)
#
#
#     def opResult(self,re,kw):
#         # with self.subTest(value=re.json()['code']):
#             try:
#                 self.assertEqual(re.json()['code'], kw["result"]["code"])
#                 self.assertEqual(re.json()['success'], kw["result"]["success"])  # 若断言无异常 认为断言成功记录日志加赋值Token
#                 self.log.info(kw["desc"] + "响应码+success断言成功 ")
#                 print("kw['desc]"+kw["desc"])
#             except AssertionError:  # 若断言有异常 记录异常日志
#                 self.log.info(
#                     kw["desc"] + "响应码+success断言失败 " + "code是(实际，期望)：" + re.json()['code'] + "," + kw["result"]["code"])  # 不能是布尔型
#                 raise  #如果抛异常 后续会继续执行 无需要用 with self.subTest(value=value): 但自动化需要
#
#
#
# if __name__=="__main__":
#     unittest.main()
#
