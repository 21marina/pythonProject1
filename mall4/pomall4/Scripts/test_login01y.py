import json
import logging
import unittest

# import ddt  # TypeError: 'module' object is not callable  应该改为下面

from ddt import ddt, data, unpack, file_data
import parameterized

import mall4
from mall4.pomall4.Page.page_login import pageLogin
from mall4.pomall4.Base.base import base
from mall4.pomall4.tools.getLogger import getLogger
from mall4.pomall4.tools.get_driver import getDriver
from mall4.pomall4.tools.logUtil import LogUtil
from mall4.pomall4.tools.op_yaml import OpYaml


def get_data():
    re=OpYaml().get_yml(mall4.ymlDataFileLoc)
    print(re) #{'test01': {'username': '1232', 'password': '131'}, 'test02': {'username': '12313818483', 'password': '123456'}}
    arrs=[]
    for dv in re.values():
        arrs.append((dv['username'], dv['password'],dv['result']))#单个的字典{}  转成了[(),()] 参数化p用 data用（（），（））
    print(arrs)
    return arrs

# @unittest.skip("暂跳")
@ddt
class testLogin01y(unittest.TestCase):
    # driver=None #不要也可以  定义类变量只是为了给各个方法都可使用 而不用每次都getDriver().get_driver()
    @classmethod
    def setUpClass(cls):
        # cls.pageLogin01=pageLogin01# 要加括号 不加的话是获取的类 加完括号是获取的类对象 类对象可调取其方法
        print("setupclass")
        #传入封装好的driver
        cls.driver= getDriver().get_driver()#？？？这个driver和类属性driver有啥关系
        #获取登录界面page对象
        cls.pageLogin=pageLogin(cls.driver)
        print("setupending")
        cls.log = getLogger().get_logger()
        getLogger().getlogFileFormater(logger=cls.log, level=logging.INFO, fileName=mall4.filePath.format("testLogin01y"), frm=mall4.frm)


    @classmethod
    def tearDownClass(cls):
        print("teardownclass")
        getDriver().quit_driver()

    # [("132", "123456"), ("13213818483", "123456")] data参数是一系列的值(1,2,3)三个值
    # 用*loc解包 用@unpack分解：字典({k1:1,k2:v2},{k1:3,k2:4})  元组（（1，2），（3，4）） list[1,2,3,4,'a','b')]
    #ddt不能用元组列表[(),()] 如果返回的是[(),()]可以用变量存放 对变量*解包 而paramized的数据是元组列表
    # file_data参数是文件名 可是json或yaml
    # @data(("132", "123456"),("13213818483", "ming862578"))
    # @unpack
    # @unittest.skip("ddt-data succcess")
    # def test01_login(self,userName,pwd):
    #     base(self.driver).base_find_element(mall4.loc_denglulink).click()
    #     self.pageLogin.zuzhuang(userName,pwd)
    #     self.driver.get("https://cloud-pc.mall4j.com/")
    #

    # @unittest.skip("ddt-file_data succcess")
    @file_data(mall4.loginymlDataFileLoc)
    @unpack
    def test02_login(self, **kwargs):
        # 怎么从可变参数获取ymal文件中的key值来遍历呢  直接取得就是{"username": "1232", "password": "131"}
        # print("*kwargs json:" + json.dumps(kwargs)) # 打印只能是个字符串 而不能是个字典{"username": "1232", "password": "131"}
        # print("*kwargs:" + kwargs.get("username")) # 打印的不能是NoneType
        userName=kwargs.get("username")
        pwd=kwargs.get("password")
        exceptedValue=kwargs.get("result")
        base(self.driver).base_find_element(mall4.loc_denglulink).click()
        self.pageLogin.zuzhuang(userName, pwd,mall4.loc_username,mall4.loc_pwd,mall4.loc_denglusub)
        #TypeError: zuzhuang() missing 1 required positional argument: 'self'
        # 要么用类对象 要么用self.类
        if base(self.driver).base_eleIsExit(mall4.loc_msgbox_top):
            #等于true 说明有元素 元素存在说明头上提示用户名或密码不正确
            self.opResult(mall4.loc_msgbox_top, exceptedValue)
        elif base(self.driver).base_eleIsExit(mall4.loc_msgbox_user):
             # 元素不存在 有可能是成功 也有可能提示在输入框下面 比如用户名为空 密码
            self.opResult(mall4.loc_msgbox_user, exceptedValue)
        elif base(self.driver).base_eleIsExit(mall4.loc_msgbox_pwd):
            self.opResult(mall4.loc_msgbox_pwd, exceptedValue)



        # 断言相等
    def assFunc(self, value, exceptedValue):
            with self.subTest(value=value):
                try:
                    self.assertEqual(value, exceptedValue)
                    self.log.info(value+"value assert success")
                except AssertionError as e:
                    print("assrtlog:")
                    #加日志
                    self.log.info("body error,body is %s,expected_body is %s" %(value,exceptedValue))
                    print("assertlogend")
                    raise
    def opResult(self,elePath,exceptedValue):
        value=base(self.driver).base_find_element(elePath).text
        self.assFunc(value, exceptedValue)
        self.driver.get("https://cloud-pc.mall4j.com/")
# if __name__=="__main__":
#     unittest.main()


#参数化
    # @parameterized.parameterized.expand(get_data())
    # def test03_login(self, userName, pwd,exceptedValue):
    #     base(self.driver).base_find_element(mall4.loc_denglulink).click()
    #     self.pageLogin.zuzhuang(userName, pwd)
    #     if base(self.driver).base_eleIsExit(mall4.loc_msgbox):  # 等于true 说明有元素
    #         value = base(self.driver).base_find_element(mall4.loc_msgbox).text
    #         print("value is:" + value)
    #         self.assFunc(value, exceptedValue)
    #         # try:
    #         #     with self.subTest(value=value):#如果不用 1错2对 会两个都错误 用完之后会tests failed上显示2，passed1 但控制台显示执行两个失败一个
    #         #        self.assertEqual(value, exceptedValue)
    #         #     # CheckPoint().checkAssertEqual(value, exceptedValue,"断言失败")
    #         # except Exception as e:
    #         #     # print("断言有误"+AssertionError+e)
    #         #     raise
    #         # 第一个用例走完后 没有结束的标志 无法下一个用例
    #         self.driver.get("https://cloud-pc.mall4j.com/")