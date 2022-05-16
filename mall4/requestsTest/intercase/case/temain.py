import json
import logging
import threading
import unittest
import  time

import requests
from ddt import ddt, data, unpack, file_data

import mall4
from mall4.pomall4.Page.page_index import pageIndex
from mall4.pomall4.Page.page_login import pageLogin
from mall4.pomall4.Page.page_proCart import pageProCart
from mall4.pomall4.Page.page_proDetails import pageProDetails
from mall4.pomall4.Base.base import base
from mall4.pomall4.Page.page_proOrder import pageOrder
from mall4.pomall4.tools.BeautifulReport import BeautifulReport
from mall4.pomall4.tools.getLogger import getLogger
from mall4.pomall4.tools.get_driver import getDriver
import urllib


class testmain():
    def mainf(self):
        # self.suite = unittest.TestSuite()
        # self.suite.addTests([
        #     unittest.defaultTestLoader.loadTestsFromTestCase(SampleTest0),
        su = unittest.defaultTestLoader.discover("./", pattern="test*.py")
        filepath = "{}.html".format(time.strftime("%Y-%m-%d_%H-%M-%S"))
        BeautifulReport(su).report(description="beautify", filename=filepath, log_path="../log/")

if __name__=="__main__":

    testmain().mainf()
    #遗留问题  业务的去支付需要前一接口的订单编号  paramOrdata["orderIds"] = orderId 加上之后后续报告就会有误
