import requests
import re
import threading

# 定义一个函数 => get_pic_url() => 获取所有图片的链接地址
def get_pic():
    res = requests.get('http://127.0.0.1:8000/')
    # 获取目标页面的html源码
    data = res.content.decode('utf-8')
    # 对html代码进行切割
    data = data.split('\n')
    # print(data)

    url_list = []
    # 对列表进行遍历
    for row in data:
        result = re.match('.*src="(.*)" width',
                          row)  # <td><img src="./images/4.jpg" width="184px" height="122px" /></td>
        if result:
            url_list.append(result.group(1))
    num = 0
    # 1.循环遍历图片的url地址
    for pic_url in url_list:
        # 2.向图片的服务器端发送请求,获取图片的内容
        res = requests.get('http://127.0.0.1:8000' + pic_url[1:])
        # 3.把以上得到的图片信息,直接写入到图片中
        with open(f'spyder/{num}.jpg', 'wb') as f:
            f.write(res.content)
        num += 1


def get_gdp():
    country_list = []
    gdp_list = []

    res = requests.get('http://127.0.0.1:8000/gdp.html')
    data = res.content.decode('utf-8')
    data = data.split('\n')
    for row in data:
        result1 = re.match('.*<a href=""><font>(.*)</font></a>.*',
                           row)  # <td>&nbsp;&nbsp;<a href=""><font>波兰</font></a></td>
        if result1:
            country_list.append(result1.group(1))
        result2 = re.match('.*￥(.*)亿元.*', row)  # <td class="rank_prev"><font>￥41194.3686亿元</font></td>
        if result2:
            gdp_list.append(float(result2.group(1)))

    # print(country_list)
    # print(gdp_list)
    # 把以上得到的结果转换为[(),(),()]
    print(list(zip(country_list, gdp_list)))


if __name__ == '__main__':
    p1 = threading.Thread(target=get_pic())
    p2 = threading.Thread(target=get_gdp())

    p1.start()
    p2.start()