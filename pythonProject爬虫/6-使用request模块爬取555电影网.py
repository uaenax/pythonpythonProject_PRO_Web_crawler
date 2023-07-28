import requests
from lxml import etree
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like '
                  'Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666 Edg/113.0.0.0'
}
res = requests.get('https://555dyy13.com/vodplay/416793-5-1.html', headers=headers)
data = res.content.decode('utf-8')
print(data)
