import re

str1 = '1478670@qq.com, go@126.com, heima123@163.com'
result = re.finditer(r'\w+@(qq|126|163)\.com', str1)
if result:
    for i in result:
        print(i.group())