# #执行代码的入口
# from tools.http_request import HttpRequest
# from tools.do_execl import DoExecl
# from tools.get_header import GetHeader
#
# #读取execl表格数据
# test_datas=DoExecl().read_execl("./test_data/login_testcase.xlsx","register")
#
# def run(test_datas,sheet_name):
#     # # #请求头
#     # header = {
#     #     "X-Lemonban-Media-Type": "lemonban.v2",
#     #     "Content-Type": "application/json"
#     # }
#     # #鉴权信息
#     # token=''
#     for test_data in test_datas:
#         print("正在测试的用例是:{0}".format(test_data['title']))
#         res = HttpRequest().http_request(test_data['url'],getattr(GetHeader,'header'), eval(test_data['data']), test_data['http_method'])
#
#         try:
#             setattr(GetHeader,'token',res.json()['data']['token_info']['token'])
#         except Exception as e:
#             token=''
#
#         # if token!='':
#         #     header = {
#         #         "X-Lemonban-Media-Type": "lemonban.v2",
#         #         "Content-Type": "application/json",
#         #         "Authorization": "Bearer " +token
#         #     }
#
#         print("响应结果:{0}".format(res.json()))
#         DoExecl().write_execl("./test_data/login_testcase.xlsx",sheet_name,test_data['case_id']+1,str(res.json()))
#
# run(test_datas,'register')
import unittest
from tools.test_http_request import TestHttpRequest
from tools.get_path import *
# from tools.HTMLTestRunner import HTMLTestRunner
import HTMLTestRunner
# 构造测试套件
suite=unittest.TestSuite()
# suite.addTest(TestHttpRequest('test_api'))#测试类的实例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
with open(test_result_path,'wb') as file:
    #执行用例
    # runner=unittest.TextTestRunner()
    runner=HTMLTestRunner.HTMLTestRunner(file)
    runner.run(suite)