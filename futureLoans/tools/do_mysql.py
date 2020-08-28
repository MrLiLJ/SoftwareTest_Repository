#数据库
#导包
import mysql.connector
from tools.read_config import ReadConfig
from tools.get_path import *

class DoMysql():
        # 获取配置文件中数据库信息
        global config
        config = eval(ReadConfig.get_config(case_config_path, 'mysql', 'config'))
        #查询语句
        """
        参数
        state：查询结果返回值，值all为返回多个结果
               值1为返回1个结果
        """
        def do_mysql_query(self,sql,state='all'):
                #关键字参数的传递
                #创建连接
                conn=mysql.connector.connect(**config)
                #创建游标
                cursor=conn.cursor()
                #执行sql
                cursor.execute(sql)
                #获取结果
                if state==1:
                        res=cursor.fetchone()
                else:
                        res=cursor.fetchall()
                #释放资源
                cursor.close()
                conn.close()
                return res
if __name__ == '__main__':
    # 编写sql
    sql = 'select * from member where mobile_phone=15500000000'
    print(DoMysql().do_mysql_query(sql,1))