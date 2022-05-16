#一个接口封装为一个api对象 接口对象层 然后共给业务层case调用
#单个测试数据
#多个测试数据 用用例编号做key
#设计主入口 执行多个测试类的多个测试数据
import json

import requests


class baseApi:
    def api_test_get(self,url, headers=None,param=None):
        res = requests.get(url=url, params=param,headers=headers)
            # .json()
        return res
    #json类型的请求体
    def api_test_post(self,url,headers=None,data=None):
        re=requests.post(url=url,headers=headers,json=data)
            # .json()
        # res = requests.post(url=url, data=data).json()
        return re#将请求响应数据返给业务层调用进行结果断言分析

    def api_test_post2(self,url, header=None, data=None):
        result = requests.post(url=url, data=data, headers=header)
            # .json()
        return result  # 将请求响应数据返给业务层调用进行结果断言分析
    def api_test_put(self,url, data):
        res = requests.put(url=url, data=data).json()
        return res

    def api_test_del(self,url, data):
        res = requests.delete(url=url, data=data).json()
        return res

    def sendRequests(url, method, paramOrdata=None,headers=None,contentType=None):
        res = None
        if method == 'GET':
            res = baseApi().api_test_get(url, headers,paramOrdata) #param
        elif method == 'POST':
            if contentType == "application/json":
                res = baseApi().api_test_post(url,headers,paramOrdata)#data
            else:
                res = baseApi().api_test_post2(url,headers,paramOrdata)#data
        elif method == 'PUT':
            res = baseApi().api_test_put(url, paramOrdata)#data
        elif method == 'DELETE':
            res = baseApi().api_test_del(url, paramOrdata)#data
        return res

    # def fangwen(self):
    # 通过requests库已经可以抓到网页源码，接下来要从源码中找到并提取数据。
    # BeautifulSoup是python的一个库, 其最主要的功能是从网页中抓取数据
    # BSoup目前已被移植到bs4库中，在导入BSoup时需先安装bs4库。之后还需安装lxml库。若不安装lxml库，则用Python默认解析器。
        #1直接访问url  urllib.request.urlopen(url)
#2设置请求头，访问Url request = urllib.request.Request(url)  # 请求地址
# request.add_header("user-agent", "mozilla/5.0")  # 修改请求头
# response2 = urllib.request.urlopen(request)
#3设置coockie，返回的cookie
# cj = http.cookiejar.CookieJar()
#  opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
# urllib.request.install_opener(opener)
#  response3 = urllib.request.urlopen(url)


