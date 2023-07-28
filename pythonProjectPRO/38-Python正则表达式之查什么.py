import re
# str1 = '&#'
# result = re.match('.', str1)
# print(result.group())
str2 = '055adafaaefa'
result = re.match('[0-9]{2}', str2)
print(result.group())