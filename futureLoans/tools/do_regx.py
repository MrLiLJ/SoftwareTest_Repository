#参数正则表达式替换工具类
import re
from tools.get_data import GetData
class DoRegx:
    @staticmethod
    def do_regx(res):
        while re.search('\$\{(.*?)\}',res):
            regx_res=re.search('\$\{(.*?)\}',res)
            key=regx_res.group(0)
            value=regx_res.group(1)
            res=res.replace(key,str(getattr(GetData,value)))
        return res


if __name__ == '__main__':
    res='{"investor_id":"${investor_id}","pwd":"12345678",}'
    print(DoRegx.do_regx(res))

