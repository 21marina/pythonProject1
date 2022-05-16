from time import sleep

import mall4
from mall4.pomall4.Base.base import base


class pageIndex(base):
    def __init__(self,driver):
        self.driver=driver
    def page_search(self,content,typess):
        self.base_input(mall4.loc_search, content)
        # self.base_find_element(mall4.loc_search).send_keys(content)
        selectType = self.base_find_element(mall4.loc_search_type).text #img标签获取txt估计不太好获取 修改父span标签
        print("selectType:"+selectType)
        if typess != selectType:  # 如果当前的值和传进来的值不一致 则点击进行切换
            self.base_find_element(mall4.loc_search_type).click()
        sleep(1)
        self.base_find_element(mall4.loc_search_button).click()
    def zuzhuang(self,content,type):
        # destEle=self.base_find_element(mall4.loc_search)
        # print("destEle is:"+str(destEle))
        # self.base_moveMouseTo(destEle)
        sleep(1)
        self.page_search(content,type)
        sleep(1)