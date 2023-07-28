import re
moblie = '13575008994a'
result = re.match('^1[3456789]\d{9}$', moblie)
if result:
    print('合理')
else:
    print('不合理')