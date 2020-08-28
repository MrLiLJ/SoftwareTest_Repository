import requests
code_url="http://www.iwebshop.com/index.php?controller=simple&action=getCaptcha&random0.19667279803489457"
res=requests.get(code_url)
#text解析结果
print(res.text)
print(res.content)