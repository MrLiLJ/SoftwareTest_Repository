import unittest
from tools.get_header import GetHeader
from tools.http_request import HttpRequest
from ddt import ddt,data,unpack
from tools.do_execl import DoExecl
from tools.get_path import *
from tools.my_log import MyLog
from tools.do_mysql import DoMysql
from tools.get_data import GetData
from tools.my_log import MyLog

test_data=DoExecl.read_execl(test_case_path)

@ddt
class TestHttpRequest(unittest.TestCase):

    def setUp(self):
        pass
    @data(*test_data)
    def test_api(self,item):
        MyLog().my_log("执行用例：{0}".format(item['title']),'INFO')
        #需要数据库检验
        before_value = None
        after_value=None
        sql_check=None
        if item['sql']!=None:
           sql=eval(item['sql'])['sql']
           before_value=int(DoMysql().do_mysql_query(sql,1)[0])
        # print(item)
        if item['data'].find('${loanId}')!=-1:
            if getattr(GetData,'loanId')==None:
                sql='select max(id) from loan where member_id={0}'.format(getattr(GetData,'memberId'))
                loanId=DoMysql().do_mysql_query(sql,1)[0]
                item['data']=item['data'].replace('${loanId}', str(loanId))
                setattr(GetData, 'loanId',loanId)
            else:
                item['data']=item['data'].replace('${loanId}', str(getattr(GetData,'loanId')))

        res=HttpRequest.http_request(item['url'],getattr(GetHeader,'header'),eval(item['data']),item['http_method'])
        # #需要数据库检验
        if item['sql']!=None:
            sql = eval(item['sql'])['sql']
            after_value = int(DoMysql().do_mysql_query(sql,1)[0])
        if item['sql']!=None:
            if  before_value==abs(after_value-int(eval(item['data'])['amount'])):
                sql_check='pass'
            else:
                sql_check='fail'

        try:
            header = {
                "X-Lemonban-Media-Type": "lemonban.v2",
                "Content-Type": "application/json",
                "Authorization": "Bearer " + res.json()['data']['token_info']['token']
            }
            setattr(GetHeader,'header',header)
        except Exception as e:
            header = {
                "X-Lemonban-Media-Type": "lemonban.v2",
                "Content-Type": "application/json",
            }
            setattr(GetHeader,'header',header)
        #断言
        try:
            self.assertEqual(item['expected'],res.json()['code'])
            test_result='PASS'
        except AssertionError as e:
            test_result='Fail'
            MyLog().log_error(e)
            # raise e
        finally:
            DoExecl.write_execl(test_case_path, item['mode'], item['case_id'] + 1, str(res.json()), test_result,sql_check)
            # print('执行结果为：{0}'.format(res.json()))
            MyLog().log_info('执行结果为：{0}'.format(res.json()))





    def tearDown(self):
        pass