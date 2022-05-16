#读取yaml文件数据
import yaml
class OpYaml:
    def get_yml(self,filepath):
        # filepath= "../data/loginyml.yml"
        with open(filepath, 'r', encoding='utf-8') as f:
        # 把文件内容读取出来
            data = yaml.safe_load(f)#IndentationError: expected an indented block #缩进错误
        print(data)
        return data
 # 读取yaml的值
 #        yamlindex = open(filepath,'r',encoding='utf-8')
 #        # 把文件内容读取出来
 #        data = yaml.full_load(yamlindex)
 #        print(data)
 #        return data
if __name__=="__main__":
    data=OpYaml().get_yml("../data/loginyml.yml")
    #此处解析测试
    arrs=[]
    for v in data.values():
        print(v) #{'username': '1232', 'password': '131'}下一行{'username': '12313818483', 'password': '123456'}
        arrs.append((v["username"],v["password"]))
    print(arrs)