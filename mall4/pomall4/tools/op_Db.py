#封装操作数据库的工具类
#先下载安装pymysql 导包-获取链接对象-获取游标对象-执行方法sql-关闭游标对象-关闭链接
# 【要执行所有方法包括执行参数语句返回的结果都在cusor对象里】

#获取链接 关闭链接 【同driver，logger一致使用单例模式】
#获取游标 关闭游标
#获取结果数据



#@classmethod 修饰符对应的函数不需要实例化 A为类名fun为方法名 一般是A().fun()才能实例化后在调用 标完之后直接A.fun()
#一般没标注解@classmethod的方法都需要实例化再调用 即A().fun() 如果不实例化报错 缺少一个必要参数self
# TypeError: get_dbdata() missing 1 required positional argument: 'self'
import pymysql
class opDb:
    url = "127.0.0.1"
    user = "root"
    pwd = "123456"
    dbname = "mingtest"
    sql = "select * from person"
    conn = None
    def opdbTest(self):
        con=pymysql.connect(user=self.user,password=self.pwd,host=self.url,database=self.dbname,charset="utf8")
        #注意不是utf-8 而且参数若直接传 不标= 则会显示init方法需要1一个参数 而传了5个参数
        cursor=con.cursor()
        cursor.execute(self.sql)
        re=cursor.fetchone()
        print("re is:",re)#re is: ('mmx', 0)  是个元组
        res=cursor.fetchall()#re is: (('mm', 1), ('mmxx', 2))如果先fetchone再fetchall时 fetchall的结果就只有两条
        #(('mmx', 0), ('mm', 1), ('mmxx', 2))  如果只有fetchall 结果就会有三条？？？
        print("re is:",res)
        # assert 0==re[0]
        cursor.close()
        con.close()
    def get_conn(self):#用单例
        # conn=None 注意此处时类变量教程  为啥不用类方法了？？？ 标上类方法也可以获取结果
        if self.conn is None:
            self.conn=pymysql.connect(user=self.user,password=self.pwd,host=self.url,database=self.dbname,charset="utf8")
        return self.conn
    def get_cursor(self):
        return self.get_conn().cursor()
    # def close_cursor(self):
    #     if self.cursor:
    #         self.cursor.close()
    def close_cursor(self,cursor):
        if cursor:
            cursor.close() #为啥连接不传 cursor传  因为conn是类变量 但为什么没有用类方法@classmethod表示了呢
    def colse_conn(self):
        if self.conn :
            self.conn.close()
    def get_dbdata2(self,sql):
       conn=opDb().get_conn()#如果是opDb.get_conn()报错TypeError: get_conn() missing 1 required positional argument: 'self'
       cur=opDb().get_cursor()
       cur.execute(sql)
       re=cur.fetchall()
       print("dddddd",re) #查完之后记得关闭  而且记得将结果返回给其他地方供其调用
#教程代码
    def get_dbdata(self, sql):
        cur=None
        data=None
        try:
            cur=self.get_cursor()#注意此时直接拿到了游标 而没有获取连接 因为游标会调用获取连接的方法
            cur.execute(sql)
            data=cur.fetchall()
            print("aaaa", data)
        except Exception as e:
            print(e)
        finally:
            self.close_cursor(cur)
            self.colse_conn()
        return data #事务 self.conn.commit()



if __name__=="__main__":
    opDb().get_dbdata (sql=opDb().sql)