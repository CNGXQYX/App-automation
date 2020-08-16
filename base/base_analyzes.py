import os
# yaml得pip下载
import yaml

# 这个其实可以放在tools文件下，不放base
def analyzes_file(file_name,key):
    # 熟练此写法
    # ./不是在当前目录吗，即base，怎么能找到data文件夹？？？？？？？？
    with open('.%sdata%s%s' % (os.sep,os.sep,file_name),'r',encoding='UTF-8') as f:
        case_data=yaml.load(f,Loader=yaml.FullLoader)[key]
        data_lsit=list()
        # values（）是只对值进行遍历，不对关键字遍历
        for data in case_data.values():
            data_lsit.append(data)
        # 切片知识
        # return data_lsit[0:1]
        return data_lsit

    # def analyze_file(file_name, key):
    #
    #     with open(".%sdata%s%s" % (os.sep, os.sep, file_name), "r") as f:
    #         case_data = yaml.load(f)[key]
    #
    #         data_list = list()
    #         for i in case_data.values():
    #             data_list.append(i)
    #
    #         return data_list


