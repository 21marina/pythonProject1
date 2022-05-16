#定义获取日志类 类方法+类属性 同driver驱动 用单例模式使公用此对象
#只封装了一句话 看起来没什么用 但是主要是调用的时候 无论调用多少次 返回的都是同一个logger对象 因为不为空则返回
#为啥不在主函数调用一次 其他用的时候传进去就好？？？这样的话就要预留参数 感觉也不方便
import logging
import logging.handlers
# import logging
# import sys
import time
from inspect import currentframe

class getLogger:
    logger=None
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger=logging.getLogger()
        return cls.logger

    def setlogger(self,logger,logLevel,fmt,type,fileName,Rfilename,Tfilename):
        if logLevel is not None:
            logger.setLevel(level=logLevel)
        if fmt is not None:
            format=logging.Formatter(fmt=fmt)#三个参数fmt若none 为默认值 datefmt为none 默认“%Y-%m-%d %H:%M:%S" style=‘%’
        if type is not None:
            for t in type:
                if type=="Stream":
                    sh=logging.StreamHandler()#输出日志到控制台 文件+控制台是logging包下的 其他再logging.handlers包下
                    sh.setFormatter(format)
                elif type=="file":
                    fh=logging.FileHandler(fileName,mode='a',encoding='UTF-8',delay=False)
                    #fileName,mode,encode,delay  mode为a 追加 w每次打开一个新文件
                    fh.setFormatter(format)
                elif type=="rotatingFile": #根据大小切割
                    rf=logging.handlers.RotatingFileHandler(Rfilename, maxBytes=1024, backupCount=5)
                    rf.setFormatter(format)
                    logger.addHandler(rf)
                elif type=="timedRotatingFile":
                    trf=logging.handlers.TimedRotatingFileHandler(Tfilename, when='M', interval=10,backupCount=30 )
                    #filename, when, interval,backupCount保留的文件数量 最新的会覆盖老的
                    trf.setFormatter(format)
                    logger.addHandler(trf)
        logger.addHandler(sh)
        logger.addHandler(fh)
        logger.addHandler(rf)
        logger.addHandler(trf)





    def a_log(self):
        logging.info("python的logging测试info")
        logging.debug("python的logging测试debug")
    def test_loggingTest(self):
        frm="%(asctime)s %(name)s %(lineno)s %(message)s"#%(levelname) 显示Arguments: ()???
        filePath="./log{}.txt".format(time.strftime("%Y-%m-%d_%H_%M_%S"))
        # logging.basicConfig(level=logging.DEBUG,format=frm,
        #                     filename="./log{}.txt".format(time.strftime("%Y-%m-%d_%H_%M_%S")))
                            # filemode="utf-8")
        # #filemode ：日志文件的打开模式。 默认值为’a’，表示日志消息以追加的形式添加到日志文件中。如果设为’w’, 那么每次程序启动的时候都会创建一个新的日志文件；
        #使用logging记日志的时候，需要带中文的字符串前面再加上u
        # logging.info(u'++++++++++ 开始启动抓取程序... ++++++++++ ')
        # sys.setdefaultencoding('utf8')#AttributeError: module 'sys' has no attribute 'setdefaultencoding'
        logging.basicConfig(level=logging.DEBUG, format=frm, filename=filePath)
        self.a_log()

    def getStreamlog(self,logger,level):##
        logger.setLevel(level)
        sh=logging.StreamHandler()
        logger.addHandler(sh)
        logger.info("testing StreamHandler...")

    def test_logFile(self,logger,level,fileName):
        logger.setLevel(level)
        sh = logging.FileHandler(filename=fileName,encoding="utf-8")
        logger.addHandler(sh)
        logger.info("testing filehandler打这个...")#不会乱码

    def getlogFileFormater(self, logger,level,fileName,frm):##
        logger.setLevel(level)
        sh = logging.FileHandler(filename=fileName, encoding="utf-8")
        fo=logging.Formatter(frm)
        sh.setFormatter(fo)
        logger.addHandler(sh)
        logger.info("testing Formater打这个...")  # 不会乱码
#以上logging 以下logging.handlers

    def getlogTimedRFH(self, logger,level,fileName,frm):
        logger.setLevel(level)
        sh = logging.handlers.TimedRotatingFileHandler(filename=fileName,when='s',interval=1,backupCount=3)
        fo=logging.Formatter(frm)
        sh.setFormatter(fo)  #TypeError: not all arguments converted during string formatting
        logger.addHandler(sh)
        for i in range(0,1000,1):
            logger.info("testing test_logTimedRFH打这个...{}".format(i)) # 不会乱码
        #有四个文件 一个是log时间，txt【log2022-03-24_09_59_09.txt】 九万多开始
        # 另三个是log日期.txt.日期   log2022-03-24_09_59_09.txt.2022-03-24_09-59-13【14，15】 13是五万多 6万多 7万多 说明前面的被覆盖了
        # 分隔片段超过三个 后面的新数据会覆盖此三个文件
    def pack_LoggerTest(self,logger,level,fileName,frm):
        logger.setLevel(level)
        sh = logging.FileHandler(filename=fileName, encoding="utf-8")
        fo = logging.Formatter(frm)
        sh.setFormatter(fo)
        logger.addHandler(sh)
        for i in range(0,100,1):
            logger.info("testing test_logTimedRFH打这个...{}".format(i))


if __name__=="__main__":
    frm="[%(asctime)s] %(thread)s %(threadName)s %(name)s %(lineno)s %(message)s"#%(levelname) 显示Arguments: ()???
    filePath="../log/log{}.txt"
        # .format(time.strftime("%Y-%m-%d_%H_%M_%S"))
    # testLogger03().test_logTimedRFH(filePath,frm)
    log=getLogger().get_logger()
    getLogger().getStreamlog(log,logging.DEBUG)
    getLogger().getlogFileFormater(logger=log,level=logging.DEBUG,fileName=filePath,frm=frm)
    # getLogger().test_logTimedRFH(logger=log, level=logging.DEBUG, fileName=filePath, frm=frm)
    # lastframe = currentframe().f_back
    # filepath = lastframe.f_code.co_filename
    # funcn = lastframe.f_code.co_name #日志所在的函数名
    # lineo = lastframe.f_lineno #日志所在行号
    log.debug("debugdddddddddddddddddddddddd"+"函数名：")
    log.info("infoooooooooaaaaaaaaaaaaaaaaaa"+"函数名：")
    log.warning("warninggggggggggggggg"+"函数名：")
    log.error("errorrrrrrrrrrrrrrrrrr"+"函数名：")
    log.critical("critacallllllll"+"函数名：")





