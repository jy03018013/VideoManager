import re

fwa = 'pages'
pattern = re.compile(fwa + '(.*?)\d+')  # 用于匹配至少一个数字
m = pattern.search("var jsTimeSharingData={pages:13,data:[fr234")  # 查找头部，没有匹配
print(m.group())
pattern = re.compile('\d+')
n= pattern.search(m.group())
print(n.group())

