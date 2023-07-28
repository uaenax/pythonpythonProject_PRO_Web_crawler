import requests
from bs4 import BeautifulSoup
# 爬取cosplay网的图片与名称
with open("cosplay.html", "r", encoding="utf-8") as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")
imgs = soup.find_all("img")
for img in imgs:
    picture = img.get("src")
    title = img.get("alt")
    if picture.endswith(".jpg"):
        picture = f"http://www.cosplay8.com{picture}"
        pictures = requests.get(picture)
        file_name = f"{title}.jpg"
        with open(f"./photo/{file_name}", "wb") as f:
            f.write(pictures.content)
            print(f"已下载{file_name}")
