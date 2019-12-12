# coding=utf-8
import configparser
import os

os.chdir("E:\\Automation\\UI\\testcase")
cf = configparser.ConfigParser()

# read(filename) 读文件内容
filename = cf.read("test.ini")
print(filename)

# sections() 得到所有的section，以列表形式返回
sec = cf.sections()
print(sec)

# options(section) 得到section下的所有option
opt = cf.options("mysql")
print(opt)

# items 得到section的所有键值对
value = cf.items("driver")
print(value)

# get(section,option) 得到section中的option值，返回string/int类型的结果
mysql_host = cf.get("mysql","host")
mysql_password = cf.getint("mysql","password")
print(mysql_host,mysql_password)