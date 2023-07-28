import re

str1 = 'hellojava, hellopython'
result = re.finditer(r'hello(java|python)', str1)
if result:
    for i in result:
        print(i.group())
