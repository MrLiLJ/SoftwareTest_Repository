import logging
from tools.get_path import *

class MyLog():
    """
    msg:日志信息
    level：日志级别：DEBUG，INFO，WARNING，ERROR,CRITICAL
    """
    def my_log(self,msg,level):
        #设置收集器
        my_logging=logging.getLogger("my_logging")
        #设置收集级别
        my_logging.setLevel("DEBUG")
        #设置日志输出格式
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息∶%(message)s')
        #设置输出渠道：输出到文件中
        file_logging=logging.FileHandler(test_log_path,encoding='utf-8')
        #设置输出级别
        file_logging.setLevel("DEBUG")
        #设置日志格式
        file_logging.setFormatter(formatter)
        #关联:给收集器指定输出渠道
        my_logging.addHandler(file_logging)
        if level=='DEBUG':
            my_logging.debug(msg)
        elif level=='INFO':
            my_logging.info(msg)
        elif level=='WARNING':
            my_logging.warning(msg)
        elif level=='ERROR':
            my_logging.error(msg)
        elif level=='CRITICAL':
            my_logging.critical(msg)
        #关闭输出渠道
        my_logging.removeHandler(file_logging)

    def log_debug(self,msg):
        self.my_log(msg,'DEBUG')
    def log_info(self,msg):
        self.my_log(msg,'INFO')
    def log_warning(self,msg):
        self.my_log(msg,'WARNING')
    def log_error(self,msg):
        self.my_log(msg,'ERROR')
    def log_critical(self,msg):
        self.my_log(msg,'CRITICAL')

if __name__ == '__main__':
    MyLog().log_info('日志级别：info')
    MyLog().log_warning('日志级别：warning')
    MyLog().log_error('日志级别：error')