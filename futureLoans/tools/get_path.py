'''获取路径'''
import os
# path=os.path.realpath(__file__)
# print(path)
path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#测试用例的路径
test_case_path=os.path.join(path,'test_data','login_testcase.xlsx')
#测试报告的路径
test_result_path=os.path.join(path,'test_result','html_report','test_api.html')
#日志路径
test_log_path=os.path.join(path,'test_result','log','log.txt')
#配置文件的路径
case_config_path=os.path.join(path,'config','case.config')
 # print(case_config_path)