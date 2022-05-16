#vdata优化 暂无



#调用base来封装页面元素 一个页面一个page 要继承base类再调用其方法[继承时还需要导包]
#封装包括定位元素 对元素的操作 及组装操作流程供script业务层调用 实现也买你和业务脚本的分离
#组装可有可无  如果没有 则会写多次调用基类方法 若有 则调一次即可
from time import sleep
from mall4.pomall4.Base.base import base


class pageLogin(base):
    def __init__(self,driver):
        self.driver=driver
        # self.driver = webdriver.Chrome()  # 暂用固定的 后续修改优化
        # self.driver.maximize_window()
        # self.driver.get("https://cloud-pc.mall4j.com/")
        # self.driver.implicitly_wait(6)
        # #临时数据 后续优化  元组的括号可以省略 吧
        # loc_denglulink=(By.XPATH,"//*[@id='__layout']/div/div[1]/div/div[2]/div[1]/span[2]/a[1]")
        # self.loc_username = (By.XPATH,"//*[@class='item account']/input")
        # self.loc_pwd=(By.XPATH,"//*[@class='item password']/input")
        # self.loc_denglusub = (By.XPATH,"//*[@class='login-button']")

    #写多个方法也是为了可用既调用组合方法 想调单个方法时也可以
    def page_denglu(self,loc):
        self.base_click(loc)
    def page_inputstr(self,loc,content):
        self.base_input(loc,content)
    # def inputPwd(self):
    def zuzhuang(self,contentUser,contentPwd,loc_username,loc_pwd,loc_denglusub):
        # self.page_denglu(self.loc_denglulink)#调用本类中的其他方法和方法外的全局变量都要加self才可 不加会报红曲线
        sleep(1)
        self.page_inputstr(loc_username,contentUser)
        self.page_inputstr(loc_pwd,contentPwd)
        sleep(1)
        self.page_denglu(loc_denglusub)
        sleep(1)

