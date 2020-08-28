#正则表达式
import re
# title='hellosword'
# res=re.match('(he)(llo)',title)
# print(res.group())
# print(res.group(0))
# print(res.group(1))
# print(res.group(2))

# title='hellowrodshello'
# res=re.findall('(he)(llo)',title)
# print(res)
title='{"mobile_phone":"${admin_tel}","pwd":"12345678",}'
while re.search('\${(.*?)\}',title):
    res=re.search('\${(.*?)\}',title)
    print(res.group(0))
    print(res.group(1))