# #主入口的实现 启动整个测试 并运行测试套件 且生成报告
# import unittest
# import time
#
# from tools.BeautifulReport import BeautifulReport
# from tools.HTMLTestRunner import HTMLTestRunner
#
# # suite=unittest.defaultTestLoader.discover("./case",pattern="test*.py")
# # filepath="./tools/{}.html".format(time.strftime("%Y-%m-%d_%H-%M-%S"))
# # with open(filepath,"wb") as f:
# #     HTMLTestRunner(stream=f).run(suite)
# su = unittest.defaultTestLoader.discover("./", pattern="test*.py")
# # filepath="{}.html".format(time.strftime("%Y-%m-%d_%H-%M-%S"))
# BeautifulReport(su).report(description="beautify", filename="brep.html", log_path="./log/")
# # # 当前脚本所在文件真实路径
# # cur_path = os.path.dirname(os.path.realpath(__file__))
# # def add_case(caseName="case", rule="test_*.py"):
# # """第一步：加载所有测试用例"""
# # case_path = os.path.join(cur_path, caseName) # 用例文件夹
# # # 文件夹不存在就创建一个文件夹
# # if not os.path.exists(case_path): os.mkdir(case_path)
# # # 定义discover加载所有测试用例
# # # case_path：执行用例的目录；pattern：匹配脚本名称的规则；top_level_dir：默认为None
# # discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
# # return discover
# # def run_case(all_case, reportName="report"):
# # """第二步：执行所有的用例，并把结果写入到html测试报告中"""
# # now = time.strftime("%Y_%m_%d_%H_%M_%S")
# # report_path = os.path.join(cur_path, reportName)
# # if not os.path.exists(report_path): os.mkdir(report_path)
# # report_abspath = os.path.join(report_path, now "result.html")
# # print("report path:%s" % report_abspath)
# # fp = open(report_abspath, "wb")
# # runner = HTMLTestRunner(stream=fp, title="自动化测试报告，测试结果如下：",
# # description="用例执行情况")
# # # 调用add_case函数
# # runner.run(all_case)
# # fp.close()
# # def get_report_file(report_path):
# # """第三步：获取最新的测试报告"""
# # lists = os.listdir(report_path)
# # lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
# # print("最新测试生成的报告：" lists[-1])
# # # 找到生成最新的报告文件
# # report_file = os.path.join(report_path, lists[-1])
# # return report_file
# # if __name__ == '__main__':
# # all_case = add_case() # 加载用例
# # run_case(all_case) # 执行用例
# # report_path = os.path.join(cur_path, "report")
# # report_file = get_report_file(report_path) # 生成报告
