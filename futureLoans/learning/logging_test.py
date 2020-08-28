import logging
# logging.debug("日志级别：debug")
# logging.info("日志级别：info")
# logging.warning("日志级别：warning")
# logging.error("日志级别：error")
# logging.critical("日志级别：critical")

#设置收集器
my_logging=logging.getLogger("logging_test")
#设置收集级别
my_logging.setLevel("DEBUG")

#设置日志输出格式
formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息∶%(message)s')


#设置输出渠道
logging_handler=logging.StreamHandler()
#设置输出级别
logging_handler.setLevel("DEBUG")
logging_handler.setFormatter(formatter)
#设置输出渠道：输出到文件中
file_logging=logging.FileHandler('file_logging.txt',encoding='utf-8')
#设置输出级别
file_logging.setLevel("DEBUG")
file_logging.setFormatter(formatter)



#关联:给收集器指定输出渠道
my_logging.addHandler(logging_handler)
my_logging.addHandler(file_logging)

my_logging.debug("日志级别：debug")
my_logging.error("日志级别：error")
