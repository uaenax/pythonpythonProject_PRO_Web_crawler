from lxml import etree
import requests

# 伪造浏览器的头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like '
                  'Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/113.0.0.0'
}
res = requests.get('https://xc01-mywbb.mysxl.cn/', headers=headers)
data = etree.HTML(res.text)
data = data.xpath('//div[@class="s-img-wrapper"]//img/@src')
num = 0
for row in data:
    # print(row)
    res = requests.get('https:' + row)
    with open(f'spyder/{num}.png', 'wb') as f:
        f.write(res.content)
    num += 1
