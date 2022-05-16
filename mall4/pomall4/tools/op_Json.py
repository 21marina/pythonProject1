#TODO文件位置还可优化 当参数传入
import json
import time


class OpJson():
    def readJsonFile(self,filePath):
        #打开文件
        print("readjsoning....")
        with open(filePath,"r",encoding='utf-8') as f:
            buf=f.read()
            # print(buf)
        return buf
        #解析文件？还是推荐放在测试类中获取数据的时候再解析 现在解析只是一种结果 工具类多是适用多种数据结果

    def readJsonFile2(self,filePath):  #以指定的编码类型（即文件本身的编码）打开文件
        #打开文件
        print("readjsoning2....")
        with open(filePath,"r",encoding='utf-8') as f:
            buf=json.load(f)
        return buf# 字典或列表 打印只能是字符串 不能是字典

    def writeJsonFile(self,data):
        with open("../data/{}.json".format(time.strftime("%Y-%m-%d_%H-%M-%S")),"w",encoding="utf-8") as f:
            f.write(data) #TypeError: write() argument must be str, not dict
            #是强转类型写 还是限制传入的参为字符串？？？
            #强制 控制台显示None 但是文件生成了
            #传str且强转str 控制台None 文件生成
            #传str 未强转 控制台None 文件生成
        #wb模式 不能要encode参数 且TypeError: a bytes-like object is required, not 'dict'

    def writeJsonFile2(self,data):
        with open("../data/{}.json".format(time.strftime("%Y-%m-%d_%H-%M-%S")),"w",encoding="utf-8") as f:
            json.dump(data,f) #传的是字符串"{\"name\": \"zhangsan\", \"age\": 1}"
            #传字典 {"name": "zhangsan", "age": 1}


if __name__=="__main__":
    data = {"name": "zhangsan", "age": 1}
    data=json.dumps(data)#字典转str
    print(data) #{"name": "zhangsan", "age": 1}
    print(OpJson().writeJsonFile2(data))