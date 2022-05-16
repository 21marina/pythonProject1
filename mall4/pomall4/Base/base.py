#pomall4 优化 之对driver的封装



#基类  单封装driver 封装对页面的通用操作
#如定位元素 点击 获取文本
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait


class base:
    def __init__(self,driver):#注意unittest框架里不能用init方法 用setup方法
        self.driver=driver
        # driver为虚拟 谁调用base，谁来传参 直接调用的时候新建类对象时通过构造函数的参数一起传
        # self.driver=webdriver.Chrome()#暂用固定的 后续修改优化
        # self.driver.maximize_window()
        # self.driver.get("https://www.baidu.com/")
        # self.driver.implicitly_wait(6)
    def base_find_element(self,loc,tim=3,fre=0.5): #若timeout有传值 就用传的值  若没有传值 就用默认值
        #webDriverWait设置查询条件 包括指定driver 时间 频率 直到找到某元素 否则没有driver去找元素
        #*loc解包  将元组解包(By.ID,"userId")实际是（"id","userid）-->解包后去掉引号和括号 id userId 列表，元组，字典均可
        #一种用 * 解的只有key，一种用 ** 解的有key、value。但是这个方法 ** 只能在函数定义中使用。 *解包字典会只有key
        #返回的是查到的元素 如果没查到呢？？？InvalidSelectorException
       return WebDriverWait(self.driver,timeout=tim,poll_frequency=fre).until(lambda x:x.find_element(*loc))
    def base_find_elements(self,loc,tim=3,fre=0.5):
        return WebDriverWait(self.driver, timeout=tim, poll_frequency=fre).until(lambda x: x.find_elements(*loc))
    def base_click(self,loc):#要用self才能调用其他方法
        ## 该语言的作用是将调用对象显式传递给每个方法作为第一个参数，该参数用于访问状态和其他方法。
        self.base_find_element(loc).click() #此处不需要加*解包 因为会拿着实参去调用找元素方法解包
        #调用方法时不用传self参数吗？？？
    def base_input(self,loc,content):
        ele=self.base_find_element(loc)
        ele.clear()#text输入框一定要先记得清空后在发送 否不请空 第二次发送输入的值会和第一次的值拼接
        ele.send_keys(Keys.CONTROL, 'a')
        ele.send_keys(Keys.DELETE) #type=number的输入框clear不能清空
        ele.send_keys(content)
    def base_getText(self,loc):
        return self.base_find_element(loc).text
    def base_getImage(self):
        self.driver.get_screenshot_as_file("./img/{}.png".format(time.strftime("%Y-%m-%d_%H_%M_%S")))
    # def base_eleIsExit(self,loc):
    #     if self.base_find_element(loc) is None:
    #         return False
    #     return True#一定要大写开头的True 小写会有红色波浪线提示
    def base_eleIsExit(self,loc):
        try:
            self.base_find_element(loc)
        except Exception as e:
          return False
        return True
    def base_moveMouseTo(self,destEle):
        # # 第一步：创建一个鼠标操作的对象
        action = ActionChains(self.driver)
        # # 第二步：添加移动操作
        action.move_to_element(destEle)
        # # 第三步：执行动作
        action.perform()