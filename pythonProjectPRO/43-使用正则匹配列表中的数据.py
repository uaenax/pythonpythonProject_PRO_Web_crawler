import re

list1 = ["apple", "banana", "orange", "pear"]
str1 = str(list1)
result = re.findall(r'(apple|pear)', str1)
if result:
    for i in result:
        print(i)