from tools.get_path import *
import pandas  as pd

class GetData:
    # title='15713806789'
    #未注册手机号
    tel=int(pd.read_excel(test_case_path,sheet_name='init').iloc[0,0])
    #借款的用户id
    memberId=int(pd.read_excel(test_case_path,sheet_name='init').iloc[1,0])
    # 借款用户手机号
    borrower_tel = int(pd.read_excel(test_case_path, sheet_name='init').iloc[2, 0])
    #管理员手机号
    admin_tel=int(pd.read_excel(test_case_path,sheet_name='init').iloc[3,0])
    #投资项目id
    loanId=None
    #投资用户手机号
    investor_tel=int(pd.read_excel(test_case_path,sheet_name='init').iloc[5,0])
    #投资用户id
    investor_id=int(pd.read_excel(test_case_path,sheet_name='init').iloc[6,0])
# #设置属性值
# setattr(GetCookie,"cookie",'str')
# #判断是否有该属性值
# print(hasattr(GetCookie,"cookie"))
# #删除该属性
# delattr(GetCookie,"cookie")
# #获取属性值
# print(int(getattr(GetData,"tel")))

