#读取excel文件中的接口【tools/xlsx】 无需再写ymldata文件
# 接口中的key值记得加双引号 读取完之后是str 要记得json转字典 value值是数组不影响字典操作
# 将读取的[{k1:v1,k2:v2}，{k1:v1,k2:v2}]结果进行解包 然后用可变参数**kw来接收
# 解包之后就是{k1:v1,k2:v2}作为一组传进去 如果不解包 则全部作为一个这个题传进去
#data文件-分析文件发请求requests-处理结果断言log-执行套件用例生成报告html
#Q: 业务生成BeautifulReport报告尚存问题
import logging
import unittest

from ddt import file_data, ddt, unpack, data

import mall4
from mall4.requestsTest.intercase.api.baseApi import baseApi
from mall4.requestsTest.intercase.tools.getLogger import getLogger
from mall4.requestsTest.intercase.tools.op_Excel import readEx


def get_data(sheetName):
    data = readEx().readEx("../tools/aex.xlsx",sheetName)  # 是个list [{},{}]
    # print("data is:" + str(data))
    return data
@ddt
class apiExcel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = getLogger().get_logger()
        getLogger().getlogFileFormater(logger=cls.log, level=logging.INFO,
                                       fileName=mall4.filePath.format("readExcelCase"), frm=mall4.frm)
        cls.baseApi = baseApi()
        # cls.token = None
        # cls.orderIds=None

    @classmethod
    def tearDownClass(cls):
        print("业务teardownclass")

    @classmethod
    def setMyValue(cls, token=None,orderIds=None):
        cls.token=token
        cls.orderIds=orderIds
    @data(*get_data("login"))
    @unpack
    def test_readEx1Login(self, **kwargs):
        print("kwstart is:" + str(kwargs)) #会执行15遍 字典
        url = kwargs.get("url") # 传进来的是字典 可直接使用
        header = kwargs.get("header")
        method = kwargs["method"]
        paramOrdata = kwargs["data"]
        re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,contentType="application/json")  # 传字典即可 无需转json传
        print(re.json()) #字典
        self.opResult(re,kwargs)
        # 正向判断拿到accesstoken
        try:
            #正向登录时能拿到token 其他逆向时拿不到
            if re.json()["data"] is not None:  # 当data:None时 .keys是NoneType无法in 所以保错 AttributeError: 'NoneType' object has no attribute 'keys'
                if type(re.json()["data"]) is not list: #登录接口的data里有list/None/字典
                    # if type(re.json()["data"]) is not str:
                        if "accessToken" in re.json()["data"].keys():
                            token=re.json()['data']['accessToken']
                            self.setMyValue(token=token) #setter方式注入值
            print("登录accseeToken值："+token)
        except AssertionError:# 若断言有异常 记录异常日志
            self.log.info("取accseeToken 出错啦")
    # @unittest.skip("addcart skip")
    @data(*get_data("cart"))
    @unpack
    def test_readEx2Addcart(self, **kwargs):
        print("kwstart is:" + str(kwargs))  # 字典
        url = kwargs["url"] # 传进来的是字典 可直接使用
        header = kwargs["header"]
        method = kwargs["method"]
        paramOrdata = kwargs["data"]
        # print("addcart token:"+self.token)
        header['Authorization'] = self.token
        print("header is：" + str(header))
        re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,
                                  contentType="application/json")  # 传字典即可 无需转json传
        print(re.json())  # 字典
        self.opResult(re, kwargs)

    # @unittest.skip("proinfo skip")
    @data(*get_data("proinfo"))
    @unpack
    def test_readEx3proInfo(self, **kwargs):
        print("kwstart is:" + str(kwargs))  # 会执行15遍 字典
        url = kwargs.get("url")  # 传进来的是字典 可直接使用
        header = kwargs.get("header")
        method = kwargs["method"]
        paramOrdata = kwargs["data"]
        re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,
                                  contentType="application/json")  # 传字典即可 无需转json传
        print(re.json())  # 字典
        self.opResult(re, kwargs)
    # @unittest.skip("confirm skip")
    @data(*get_data("confirm"))
    @unpack
    def test_readEx4confirm(self, **kwargs):
        print("kwstart is:" + str(kwargs))  # 会执行15遍 字典
        url = kwargs.get("url")  # 传进来的是字典 可直接使用
        header = kwargs.get("header")
        method = kwargs["method"]
        paramOrdata = kwargs["data"]
        header['Authorization'] = self.token
        print("header is：" + str(header))
        re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,
                                  contentType="application/json")  # 传字典即可 无需转json传
        print(re.json())  # 字典
        self.opResult(re, kwargs)
    # @unittest.skip("submit skip")
    @data(*get_data("submit"))
    @unpack
    def test_readEx5submit(self, **kwargs):
        print("kwstart is:" + str(kwargs))  # 会执行15遍 字典
        url = kwargs.get("url")  # 传进来的是字典 可直接使用
        header = kwargs.get("header")
        method = kwargs["method"]
        paramOrdata = kwargs["data"]
        header['Authorization'] = self.token
        print("header is：" + str(header))
        re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,
                                  contentType="application/json")  # 传字典即可 无需转json传
        print(re.json())  # 字典
        self.opResult(re, kwargs)
    @unittest.skip("submit skip")
    @data(*get_data("yewu"))
    @unpack
    def test_readEx6yewu(self, **kwargs):
        print("kwstart is:" + str(kwargs))  # 会执行15遍 字典
        # 解析
        url = kwargs.get("url")  # 传进来的是字典 可直接使用
        header = kwargs.get("header")
        method = kwargs["method"]
        paramOrdata = kwargs["data"]
        # 给header设置token值
        header['Authorization'] = self.token
        print("header is：" + str(header))
        print("paramOrdata.keys():"+str(paramOrdata.keys()))
        #dict_keys(['payType', 'orderIds', 'returnUrl'])
        if "orderIds" in paramOrdata.keys():
            print("判断orderIds:"+str(self.orderIds))
            paramOrdata["orderIds"] = self.orderIds
        print("paramOrdata:"+str(paramOrdata))
        re = baseApi.sendRequests(url=url, method=method, headers=header, paramOrdata=paramOrdata,
                                  contentType="application/json")  # 传字典即可 无需转json传
        # 分析响应数据
        print(re.json())  # 字典
        # 断言
        self.opResult(re, kwargs)
        if type(re.json()["data"]) is list and re.json()["success"] is True:
            #取值
            orderIds=re.json()["data"]
            self.setMyValue(token=self.token,orderIds=orderIds)#如果此时不设置token 则token会为空
            print("orderIds"+str(self.orderIds))

    def opResult(self, re, kw):
    # with self.subTest(value=re.json()['code']):
                try: #(kwargs["result"])))#dict
                    #kw["result"]["code"] 从excel文件中读的是字符串 而返回的是bool类型 所以断言不匹配
                    self.assertEqual(str(re.json()['code']), kw["result"]["code"])
                    self.assertEqual(str(re.json()['success']), kw["result"]["success"])  # 若断言无异常 认为断言成功记录日志加赋值Token
                    self.log.info(kw["title"] + "响应码+success断言成功 ")
                    print("kw['title]"+kw["title"])
                except AssertionError:  # 若断言有异常 记录异常日志
                    self.log.info(
                        kw["title"] + "响应码+success断言失败 " + "code是(实际，期望)：" + re.json()['code'] + "," + kw["result"]["code"])  # 不能是布尔型
                    raise  #如果抛异常 后续会继续执行 无需要用 with self.subTest(value=value): 但自动化需要



if __name__ == "__main__":
    unittest.main()
    # get_data()