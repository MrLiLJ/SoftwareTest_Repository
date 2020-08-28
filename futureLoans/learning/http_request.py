#导包
import requests

#注册接口
register_url="http://api.lemonban.com/futureloan/member/register"
register_headers={
                    "X-Lemonban-Media-Type":"lemonban.v2",
                    "Content-Type":"application/json"
                    }
register_data={
                    "mobile_phone":"13889977668",
                    "pwd":"12345678",
                    "reg_name":"mumu"
                }
res=requests.post(register_url,headers=register_headers,json=register_data)
#text解析结果
print(res.text)
print(res.json())

#登陆接口
login_url="http://api.lemonban.com/futureloan/member/login"
login_headers={
                    "X-Lemonban-Media-Type":"lemonban.v2",
                    "Content-Type":"application/json"
                    }
login_data={
                    "mobile_phone":"13889977668",
                    "pwd":"12345678",
                }
login_res=requests.post(login_url,headers=login_headers,json=login_data)
#解析结果
# print("text解析结果：",login_res.text)
print("json解析结果:",login_res.json()['data']['token_info']['token'])

#充值接口
recharge_url="http://api.lemonban.com/futureloan/member/recharge"
recharge_headers={
                    "X-Lemonban-Media-Type":"lemonban.v2",
                    "Content-Type":"application/json",
                    "Authorization":"Bearer "+login_res.json()['data']['token_info']['token']
                }
recharge_data={
                    "member_id":"2086026",
                    "amount":"10001",
                }
res=requests.post(recharge_url,headers=recharge_headers,json=recharge_data)
#解析结果
# print("text解析结果：",res.text)
print("json解析结果:",res.json())

# register_url="http://www.iwebshop.com/index.php?controller=simple&action=reg_act"
# register_data={
#             "callback":"?controller=simple&action=login",
#             "email":"124389@qq.com",
#             "username":"李四",
#             "password":"123456",
#             "repassword":"123456",
#             "captcha":"juiif"
#             }
# res=requests.post(register_url,register_data)
# #text解析结果
# print(res.text)

# 登陆
# login_url="http://www.iwebshop.com/index.php?controller=simple&action=login_act"
# login_data={
#             "callback":"?controller=site&action=index",
#             "login_info":"admin",
#             "password":"admin123"
#             }
# res=requests.post(login_url,login_data)
# #text解析结果
# print(res.text)
#json解析结果
#print(res.json())