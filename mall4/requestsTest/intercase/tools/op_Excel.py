#获取excel文件  excel里面存的应该是用例 而不仅仅是数据
#先下载openpyxl-导包-
import json

import openpyxl
class readEx():
    def readEx(self,filepath,sheetName):
        # filepath="./aex.xlsx"
        excel=openpyxl.load_workbook(filepath)
        shet=excel[sheetName]  #注意excel文件中的kv键值对都要加双引号 才可作为字典
        datas= []
        # dit={"d1":{"username":"mmc","pwd":"p123"},"d2":{"username":"mmcc","pwd":"p123456"}}
        # for v in dit.values():
        #     print(v)
        for v in shet.values:#注意此处不带括号 ('编号', 'username', 'pwd')下一行(1, 132, 123456)下一行(2, 13213818483, 123456)
            # print(v)
            data={}
            if v[0].startswith('m-i'): #如果每一行的第一类是m-i开头 放在字典中
                data['id']=v[0] #放进去是str 但是header/data/rsult需要字典
                data['mk']=v[1]
                data['title']=v[3] #有的用desc描述
                data['method']=v[5]
                data['url']=v[6]
                data['header'] = json.loads(v[7])#必须excel的key值有引号 才能从str转dict
                data['data']= json.loads(v[8]) #注意有空参值
                data['result']=json.loads(v[9]) #期望值
                data['results']=v[10] #实际值 一般为None
                # datadict[v[0]]=data #以id左key 每个用例一个key 即字典嵌套以每个用例的字典
                datas.append(data)
        print(datas)
        return datas

if __name__ == "__main__":
    readEx().readEx("./aex.xlsx","yewu")
    # readEx().readEx("./aex.xlsx","confirm")

