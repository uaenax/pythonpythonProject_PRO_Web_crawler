import requests
from bs4 import BeautifulSoup
value = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
headers = {
    "User-Agent":value
}
# response = requests.get("http://www.cosplay8.com/pic/Lolita/", headers=headers)
for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    response.encoding = "utf-8"
    if response.ok:
        print("successful"+f":{response.status_code}")
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        # all_prices = soup.findAll("p", attrs={"class": "txtover"})
        all_title = soup.findAll("span", attrs={"class": "title"})
        for title in all_title:
            title_string = title.string
            if "/" not in title_string:
                print(title_string)
    else:
        print("unsuccessful"+f":{response.status_code}")