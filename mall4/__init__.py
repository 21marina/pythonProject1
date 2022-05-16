import time

from selenium.webdriver.common.by import By
# def loc():
logFilePath="../log"
frm = "%(asctime)s %(name)s %(lineno)s %(message)s"
filePath = "../log/log_{}.txt"
IFfilePath = "../log/log_{}.txt"
filePath2 = "../log/log{}.txt".format(time.strftime("%Y-%m-%d_%H_%M_%S"))
regymlDataFileLoc="../data/regyml.yml"
loginymlDataFileLoc="../data/loginyml.yml"
IFloginymlDataFileLoc="../data/loginyml.yml"
searchymlDataFileLoc="../data/searchyml.yml"
IFsearchymlDataFileLoc="../data/searchyml.yml"
# pageChangeDataFileLoc="../data/pageChangeyml.yml"
IFprodetailymlDataFileLoc="../data/prodetailyml.yml"
addCartNumymlDataLoc ="../data/addCartNumyml.yml"
IFaddCartNumymlDataLoc="../data/addCartNumyml.yml"
IFyewuymlDataLoc="../data/yewuyml.yml"
jifenymlDataLoc="../data/jifenyml.yml"
caseyewuDataLoc="../data/caseyml.yml"
jsonDataFileLoc="../data/jstest"
#reg part because of verifyCode
loc_reglink=(By.XPATH,"//*[@class='link']")
loc_regUser=(By.XPATH,"//*[@class='input-box phone']/input")
loc_regNext=(By.XPATH,"//*[@class='next']")
loc_regMsgbox_user=(By.XPATH,"//*[@class='error-text']")
loc_regMsgbox_pwd=(By.XPATH,"//*[@class='error-text']")
#Login
loc_denglulink = (By.XPATH,"//*[@id='__layout']/div/div[1]/div/div[2]/div[1]/span[2]/a[1]")
loc_username = (By.XPATH,"//*[@class='item account']/input")
loc_pwd=(By.XPATH,"//*[@class='item password']/input")
loc_denglusub = (By.XPATH,"//*[@class='login-button']")
loc_msgbox_top=(By.CLASS_NAME,"el-message__content")
loc_msgbox_user=(By.XPATH,"//*[@class='login-con']/div[2]")
loc_msgbox_pwd=(By.XPATH,"//*[@class='login-con']/div[4]")
#//*[@id='__layout']/div/div[1]/div[2]/div[2]/div[3]/div[4]
#选商品
loc_pro=(By.XPATH,"//div[text()='15分钟快速救脸，射频多功能美容仪']")
loc_pro_cart=(By.XPATH,"//a[text()='15分钟快速救脸，射频多功能美容仪']/../preceding-sibling::div[@class='tab-check']/input[@class='checkbox default']")
loc_pro_carted=(By.XPATH,"//a[text()='15分钟快速救脸，射频多功能美容仪']/../preceding-sibling::div[@class='tab-check']/input[@class='checkbox default checked']")
loc_pro_cartDiv=(By.CLASS_NAME,"//*[@class='cart-con']")
loc_all_btn=(By.ID,"allCheckBottom")
loc_search=(By.CLASS_NAME,"search-input")
loc_search_type=(By.CLASS_NAME,"search-type")
loc_search_button=(By.CLASS_NAME,"search-btn")
loc_selectPro=(By.XPATH,"//*[@class='list-con four-item-line']/div[1]/div[1]/img")
loc_proType=(By.XPATH,"//*[@class='con']/span[@class='item']")
loc_num_incr=(By.CLASS_NAME,"increase")
loc_num_input=(By.XPATH,"//*[@class='goods-number']/input")
loc_num_desc=(By.XPATH,"//*[@class='goods-number']/span[@class='reduce']")
loc_num_stock=(By.XPATH,"//*[@class='stock']/span") #当前库存量影响是否加购
loc_cart_top=(By.CLASS_NAME,"cart-btn")
loc_collect_btn=(By.CLASS_NAME,"collect")
loc_collected_btn=(By.CLASS_NAME,"collect active")

loc_msgaddCollect=(By.CLASS_NAME,"el-message__content")
# 加购
loc_addCart=(By.CLASS_NAME,"add-cart")
loc_msgaddCart=(By.CLASS_NAME,"el-message__content")
loc_cartSelect=(By.XPATH,"//*[@class='cart-con']/div[1]/div[2]/div[1]/div[1]/div[1]/input")
loc_cartproNum=(By.XPATH,"//*[@class='cart-con']/div[1]/div[2]/div/div/div[5]/div/input")
loc_confirm_btn = (By.CLASS_NAME, "btn")
# 立即购买
loc_buy=(By.CLASS_NAME,"buy-now")
loc_jifendisc_select=(By.CLASS_NAME,"el-checkbox__input")
loc_jifendisc_selected=(By.CLASS_NAME,"el-checkbox__input is-checked")
loc_jifendisc_input=(By.XPATH,"//*[@class='integral-item integral-input-box']/input")
loc_jifendisc_disc=(By.CLASS_NAME,"integral-money")
loc_jifendisc_max=(By.XPATH,"//*[@class='integral-item integral-input-box']/span[2]")
loc_jifendisc_maxAccount=(By.XPATH,"//*[@class='integral-item integral-input-box']")#账户最大可用积分
loc_detail_num=(By.XPATH,"//*[@class='goods-item']/div[@class='number']") #当前商品的数量
loc_addDetail=(By.CLASS_NAME,"item add-address")
loc_qujiesuan=(By.CLASS_NAME,"//*[@class='btn']")
loc_submit_btn=(By.CLASS_NAME,"btn")
loc_pay_btn=(By.CLASS_NAME,"btn")
