# 1以字典序的方式编写test方法 把想要先执行的case字典序排到前面
# 遇到test_login这种不是数字结尾的方法。可写成test_数字_业务的模式
# 2手写一个loader继承自TestLoader类，改写里面的排序方法
# 在unittest运行的时候传入这个新的loader

import unittest


class MyTestLoader(unittest.TestLoader):
    def getTestCaseNames(self, testcase_class):
        # 调用父类的获取“测试方法”函数
        test_names = super().getTestCaseNames(testcase_class)
        # 拿到测试方法list
        testcase_methods = list(testcase_class.__dict__.keys())
        # 根据list的索引对testcase_methods进行排序
        test_names.sort(key=testcase_methods.index)
        # 返回测试方法名称
        return test_names


class Testcase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_1(self):
        print("执行第一个")

    def test_2(self):
        print("第二个")

    def test_3(self):
        print("第三个")

    def test_10(self):
        print("第四个")

    def test_11(self):
        print("第五个")

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main(testLoader=MyTestLoader())
