import re

# str1 = 'acavavca1823cwac'
#
# num = re.search('\d(\d)(\d)', str1)
# print(num.group())
# print(num.group(1))  # 获取一号分组的数据
# print(num.group(2))  # 获取二号分组的数据

# str2 = 'afaccw1111efac'
# num = re.search(r'(\d)\1\1\1', str2)
# print(num.group())
str3 = 'wacaw3569ac1221ac'
num = re.search(r'(\d)\1\2', str3)
print(num.group())
