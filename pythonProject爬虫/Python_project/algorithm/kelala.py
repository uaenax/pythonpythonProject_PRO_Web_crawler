import requests
from bs4 import BeautifulSoup

from Python_project.Utils.url_manager import UrlManager

urls = UrlManager()
url_list = ["https://pixiv.re/108074607-1.jpg",
"https://pixiv.re/108074607-2.jpg",
"https://pixiv.re/108074607-3.jpg",
"https://pixiv.re/108074607-4.jpg",
"https://pixiv.re/108074607-5.jpg",
"https://pixiv.re/108074607-6.jpg",
"https://pixiv.re/108074607-7.jpg",
"https://pixiv.re/108074607-8.jpg",
"https://pixiv.re/108074607-9.jpg",
"https://pixiv.re/108074607-10.jpg",
"https://pixiv.re/108074607-11.jpg",
"https://pixiv.re/108074607-12.jpg",
"https://pixiv.re/108074607-13.jpg",
"https://pixiv.re/108074607-14.jpg",
"https://pixiv.re/108074607-15.jpg",
"https://pixiv.re/108074607-16.jpg",
"https://pixiv.re/108074607-17.jpg",
"https://pixiv.re/108074607-18.jpg"]
urls.add_new_urls(url_list)

while urls.has_new_url():
    url = urls.get_url()
    headers = {"User-Agent":"""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"""}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("unsuccessful" + f":{response.status_code}")
        continue
    html = response.content
    soup = BeautifulSoup(html, "html.parser", from_encoding="iso-8859-1")
    imgs = soup.find_all("img")
    for img in imgs:
        picture = img.get("src")
        print(picture)
        file_name = f"克拉拉{picture[-5]}"
        with open(f"./photo/{file_name}") as f:
            f.write(picture)
            print(f"已下载{file_name}")
