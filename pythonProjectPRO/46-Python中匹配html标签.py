'''
需求:从字符串中匹配出<html><h1>www.itcast.cn</h1><html>
增加需求:只想要标签中的内容

分析:所有的HTML标签,如果是双标签都是有开头且有结尾
'''
import re

str1 = '<html><h1>www.itcast.cn</h1></html>'
result = re.match(r'<(\w+)><(\w+)>(.*)</\2></\1>', str1)
if result:
    print(result.group(3))
