import re


def url(rex, path):
    res = re.match(f'.*{rex}', path)
    res = res.group(1)
    return res


path1 = "http://127.0.0.1:/books/100"  # 匹配获取ID 100
path2 = "http://127.0.0.1:/heroes/qiaofeng"  # 匹配并返回结果  {"name":'qiaofeng'}
# 调用说明:
res1 = url(r'/books/(\d+)', path1)
# 输出结果（100，）
print(res1)

# 不要字符/,q,i,a,o
res2 = url(r'/heroes/(?P<name>[^/]+)', path2)
# 输出结果{"name":'qiaofeng'}
print(res2)
