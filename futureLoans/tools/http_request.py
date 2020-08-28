#导包
import requests

class HttpRequest:
        #请求
        @staticmethod #静态方法
        def http_request(url,header,data,http_method):
            try:
                    #字符串方法upper()返回只包含大写字符的副本
                    if http_method.upper()=="GET":
                        res=requests.get(url,headers=header,json=data)
                    elif http_method.upper()=="POST":
                        res=requests.post(url,headers=header,json=data)
                    elif http_method.upper()=="PATCH":
                        res=requests.patch(url, headers=header, json=data)
                    else:
                        print("输入的请求方式错误")
            except Exception as e:
                print("请求方式异常：{0}".format(e))
                raise e
            return res #返回结果