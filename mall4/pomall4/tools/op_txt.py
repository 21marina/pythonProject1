#读取txt数据文件
#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便

class OpTxt:
    def read_txt(self,filePath):
        with open(filePath,"r",encoding="utf_8") as f:
            #参数如果是utf-8 而没有encoding=会报错 TypeError: an integer is required (got type str)
            #因为跨参数了 open的第三个参数为buffering 是int型数据
            # print(f.readline()) #如果是readline 则之读第一行132,123456
            # print(f.readlines()) #['132,123456\n', '1321381843,123456']
            # print(f.readlines())#[]这个调用第二变及多次 都是[]
            return f.readlines() #注意位置
if __name__=="__main__":
    filepath="../data/testtxt"
    re=OpTxt().read_txt(filepath)#TypeError: 'NoneType' object is not iterable 是方法忘了返回值
    # print(re)
    #此处解析易测试 用到的时候再去业务层解析 要想用参数化还是需要[(1,2),(3,4)]
    arrs=[]
    # for d in re:
    #     # print(d)# 132,123456 空行 下一行 1321381843,123456
    #     # print(d.strip().split(","))#['132', '123456'] 下一行 ['1321381843', '123456']
    #     dss=d.strip().split(",")
    #     arrs.append(dss)
    #     print(arrs) #[['132', '123456'], ['1321381843', '123456']]
    for d in re:
        dss=d.strip().split(",")
        # print(dss) #['132', '123456'] 下一行 ['1321381843', '123456']
        ds=tuple(dss)
        # print(ds) #('132', '123456')下一行('1321381843', '123456')
        arrs.append(ds)
        print(arrs)#[('132', '123456'), ('1321381843', '123456')]