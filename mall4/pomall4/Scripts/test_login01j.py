# #vdata优化 数据驱动 +Log日志记录
# # 新建文件夹data下新建存放数据的文件+读文件数据的工具类tools
# #json文件主要是用用例编号做key，本用例的总数据做value 也是json格式
# #json类似于python的字典 但字典可以getkey获取到value值 而json字符串不能get Java中一般用map来操作json
# #定位元素的位置数据也要单独保存
# #定义类时没有继承时  要加（）吗？？？
#
#
#
# #测试类和测试方法都要以test开头 为了好命名 类名直接大驼峰去模块名即可
# #组装对页面的操作流程 测试类继承unittest 配置装置函数及测试方法
# #要想调用page内的组装方法 得先导入
# # 不用传loc loc再page里 script业务层只传数据即可
# import json
# import unittest
#
# import parameterized
# from ddt import ddt, file_data, unpack
# from selenium.webdriver.common.by import By
#
# import mall4
# from mall4.pomall4.Page.page_login import pageLogin
# from mall4.pomall4.Base.base import base
# from mall4.pomall4.tools.get_driver import getDriver
# from mall4.pomall4.tools.op_Json import OpJson
#
#
# def get_data():
#     # return [("132", "123456"), ("13213818483", "123456")]
#     # 单参数 是元组[1,2]或[(1,),(2,)] 多参数 是列表嵌套元组[(1,2),(2,3)] 所以进行json到元组的转换
#     #json到元组得先 json到字典 通过字典的getkey方法将数据再次拼接
#     # dict=json.loads(re)
#     # print(dict) #{'test01': {'username': '132', 'pwd': '123456'}, 'tset02': {'username': '13213818483', 'pwd': '123456'}}
#     # dictv=dict.values() #要变成[("132", "123456"), ("13213818483", "123456")]
#     # arrs=[]
#     # for dv in dictv:
#     #     arrs.append((dv['username'],dv['pwd']))
#     #     # arrs.append((dv.get('username'),dv.get('pwd')))#与上述效果等价
#     #     # arrs.append("(")
#     #     # arrs.append(dv.get("username"))
#     #     # arrs.append(dv.get('pwd'))
#     #     # arrs.append(")")#['(', '132', '123456', ')', '(', '13213818483', '123456', ')']
#     # print(arrs) #[('132', '123456'), ('13213818483', '123456')]
#     # return arrs
#
# # 如果读jsan文件用的是load方法 那读的结果是字典或列表
#     re = OpJson().readJsonFile2(mall4.jsonDataFileLoc)
#     print(re) #json文件字符串 参数化需要的是数组
#     arrs=[]
#     for dv in re.values():
#         arrs.append((dv['username'], dv['password'], dv['result']))
#     print(arrs)
#     return arrs
# # if __name__=="__main__":
# #     get_data()
# # @unittest.skip("暂跳")
# @ddt
# class testLogin01j(unittest.TestCase):
#     # driver=None #不要也可以  定义类变量只是为了给各个方法都可使用 而不用每次都getDriver().get_driver()
#     @classmethod
#     def setUpClass(cls):
#         # cls.pageLogin01=pageLogin01# 要加括号 不加的话是获取的类 加完括号是获取的类对象 类对象可调取其方法
#         print("setupclass")
#         #传入封装好的driver
#         cls.driver= getDriver().get_driver()#？？？这个driver和类属性driver有啥关系
#         #获取登录界面page对象
#         cls.pageLogin=pageLogin(cls.driver)
#         print("setupending")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("teardownclass")
#         getDriver().quit_driver()
#
#     @unittest.skip("json参数化")
#     # [("132", "123456"), ("13213818483", "123456")]
#     @parameterized.parameterized.expand(get_data())
#     def test01_login(self,userName,password,exceptedValue):
#         base(self.driver).base_find_element(mall4.loc_denglulink).click()
#         self.pageLogin.zuzhuang(userName,password)
#         # 如果反向用例会有这个定位值 如果正向无值 无需此处定位再断言  定位不到会超时 所以先判断
#         if base(self.driver).base_eleIsExit(mall4.loc_msgbox):#等于true 说明有元素
#             value = base(self.driver).base_find_element(mall4.loc_msgbox).text
#             print("value is:" + value)
#             self.assFunc(value, exceptedValue)
#            #第一个用例走完后 没有结束的标志 无法下一个用例
#             self.driver.get("https://cloud-pc.mall4j.com/")
#
#     #暂不行 输入可以 但是会执行5个 失败2个 成功2个 忽略一个 失败报超时异常 像是又执行了一遍似的
#     @file_data(mall4.jsonDataFileLoc)
#     @unpack
#     def test02_login(self, **kwargs):
#         # 怎么从可变参数获取ymal文件中的key值来遍历呢  直接取得就是{"username": "1232", "password": "131"}
#         print("*kwargs json:" + json.dumps(kwargs)) # 打印只能是个字符串 而不能是个字典{"username": "1232", "password": "131"}
#         # print("*kwargs:" + kwargs.get("username")) # 打印的不能是NoneType
#         userName = kwargs.get("username")
#         pwd = kwargs.get("password")
#         exceptedValue=kwargs.get("result")
#         base(self.driver).base_find_element(mall4.loc_denglulink).click()
#         self.pageLogin.zuzhuang(userName, pwd)
#         if base(self.driver).base_eleIsExit(mall4.loc_msgbox):  # 等于true 说明有元素
#             value = base(self.driver).base_find_element(mall4.loc_msgbox).text
#             print("value is:" + value)
#             self.assFunc(value, exceptedValue)
#             # 第一个用例走完后 没有结束的标志 无法下一个用例
#             self.driver.get("https://cloud-pc.mall4j.com/")
#
#     #断言相等
#     def assFunc(self,value, exceptedValue):
#         try:
#             # if(type("str")==type(ExceptedValue)):
#             self.assertEqual(value,exceptedValue)
#             return True
#         except AssertionError:
#             # self.log.error("body error,body is %s,expected_body is %s" % (value, exceptedValue))
#             return False
#             raise
#
#
#
# if __name__=="__main__":
#     unittest.main()