#封装driver 供业务层调用 业务层调base 故业务层传递driver驱动对象
#使用单例模式 从头到尾新建的都是同一个对象

#视频教学设置的driver为类属性 为了让所所有公用同一个驱动对象
from selenium import webdriver
from selenium.webdriver.common.by import By


class getDriver:
    # def get_driver(self):
    #     driver=None
    #     if driver is None:
    #         driver=webdriver.Chrome()
    #         driver.maximize_window()
    #         driver.implicitly_wait(6)
    #         driver.get("https://www.baidu.com/")
    #     print(driver)
    #     return driver
    driver = None#???这个一定要有 如果没有怎么cls中有 如何判断为空 AttributeError: type object 'getDriver' has no attribute 'driver'
    @classmethod #???
    def get_driver(cls):
        if cls.driver is None:
            cls.driver=webdriver.Chrome()#???
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(6)
            cls.driver.get("https://cloud-pc.mall4j.com/")
            # cls.driver.find_element(By.ID,"s-top-loginbtn").click()
            #第一个用例跑完之后 不会回到百度首页 无法点击首页的登录按钮
            # 会报错selenium.common.exceptions.ElementClickInterceptedException: Message: element
            #大致意思就是当前元素是不可以点击,但是确实存在在页面上,有可能是被loading覆盖了  所以我手动将登录挪过来
            # 实际项目中正向用例不会再回来的 而是按照顺序往下走
            #后来调到到业务层去了
        print(cls.driver)
        return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None



#quit关闭之后除了地址 所有东西都清空了【类似栈还在 堆内容无】 置空cls.driver=None之后 driver才是None
if __name__=="__main__":
    # getDriver.get_driver()#TypeError: get_driver() missing 1 required positional argument: 'self'
    getDriver().get_driver()