import configparser

class ReadConfig:
    @staticmethod
    def get_config(file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]
if __name__ == '__main__':
    from tools.get_path import *
    mode=eval(ReadConfig.get_config(case_config_path,'MODE','mode'))
    for key in mode:
        print(key)