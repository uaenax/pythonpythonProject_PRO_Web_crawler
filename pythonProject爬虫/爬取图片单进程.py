'''
url = 'https://sc.chinaz.com/tupian/zhuangxiutupian.html'
//div[@class="item masonry-brick"]/img/@src
'''
import re
import requests
import multiprocessing
import threading

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like '
                  'Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/113.0.0.0'
}
res = requests.get('https://sc.chinaz.com/tupian/zhuangxiutupian.html', headers=headers)
data = res.content.decode('utf-8')
data = data.split('\n')


# print(data)
def get_url():
    ulr_list = []
    for i in data:
        # 'data-original="//scpic1.chinaz.net/files/default/imgs/2023-05-12/b87f1d0a5724919b_s.jpg"\r'
        resuly1 = re.match('.*data-original="(.*)"\r', i)
        if resuly1:
            ulr_list.append(resuly1.group(1))
    return ulr_list


def name_get():
    name_list = []
    for i in data:
        # <a class="name" href="/tupian/23051717136.htm" title="马来西亚风格客厅沙发茶几图片" target="_blank">马来西亚风格客厅沙发茶几图片</a>
        resuly2 = re.match('.*title="(.*)" target="_blank"', i)
        if resuly2:
            name_list.append(resuly2.group(1))
    return name_list


if __name__ == '__main__':
    get = threading.Thread(target=get_url)
    name = threading.Thread(target=name_get)
    get.start()
    name.start()
    url = get_url()
    name = name_get()
    for i in range(len(url)):
        jpg = requests.get('https:' + url[i])
        with open(f'01/{name[i]}.jpg', 'wb') as f:
            f.write(jpg.content)
