import requests
from Utils import url_manager

user_agent = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"""
headers = {
    "User-Agent": user_agent
}
cookies = {
    "Hm_lvt_1893a75fb13d3c54441162f35c31e6c2": "1684219483,1684296936",
    "Hm_lpvt_1893a75fb13d3c54441162f35c31e6c2": "1684296936"
}
root_url = "http://www.cosplay8.com/pic/Lolita/"
urls = url_manager.UrlManager()
urls.add_new_url(root_url)

while urls.has_new_url():
    curr_url = urls.get_url()
    response = requests.get(curr_url, headers=headers, cookies=cookies, timeout=3)
    if response.status_code != 200:
        print("unsuccessful" + f":{response.status_code}")
        continue
    with open("cosplay.html", "wb") as f:
        f.write(response.content)




