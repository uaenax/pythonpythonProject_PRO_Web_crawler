import requests
import re


# 定义一个函数 => get_pic_url() => 获取所有图片的链接地址
def get_pic_url():
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
    # print(url_list)
    return url_list


# 用于实现爬取图片的保存
def save_pic(pic_url_list):
    num = 0
    # 1.循环遍历图片的url地址
    for pic_url in pic_url_list:
        # 2.向图片的服务器端发送请求,获取图片的内容
        res = requests.get('http://127.0.0.1:8000' + pic_url[1:])
        # 3.把以上得到的图片信息,直接写入到图片中
        with open(f'spyder/{num}.jpg', 'wb') as f:
            f.write(res.content)
        num += 1



if __name__ == '__main__':
    pic_url_list = get_pic_url()
    save_pic(pic_url_list)
