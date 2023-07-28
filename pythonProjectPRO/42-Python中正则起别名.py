import re

str1 = '<book></book>'
result = re.search(r'<(?P<mark>\w+)></(?P=mark)>', str1)
if result:
    print(result.group())