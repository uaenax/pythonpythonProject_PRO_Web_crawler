import re

str1 = 'qq:10567'
result = re.split(r':', str1)
print(result)
print(f'{result[0]}:{result[1]}')