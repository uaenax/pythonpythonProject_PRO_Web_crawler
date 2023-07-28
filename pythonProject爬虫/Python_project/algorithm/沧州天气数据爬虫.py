# import requests
# import pandas as pd
# headers = {"User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"""}
# url = "https://tianqi.2345.com/Pc/GetHistory"
#
#
# def craw_table(year, month):
#     params = {"areaInfo[areaId]": 71629, "areaInfo[areaType]": 2, "date[year]": year, "date[month]": month}
#     response = requests.get(url, headers=headers, params=params)
#     data = response.json()["data"]
#     print(data)
#     df = pd.read_html(data)[0]
#     return df
# a = craw_table(2017,6)
# print(a)
# # df_list=[]
# # for y in range(2017, 2024):
# #     year = int(y)
# #     for m in range(1, 13):
# #         month = int(m)
# #         if year == 2023 and year+month >= 2029:
# #             pass
# #         elif year == 2017 and year+month <= 2021:
# #             pass
# #         else:
# #             df = craw_table(year, month)
# #
# #             df_list.append(df)
# # with open("沧州天气.txt", "w", encoding="utf-8") as f:
# #     for i in df_list:
# #         f.write(f"{i}\n")
# # pd.concat(df_list).to_excel("沧州17年到23年(5月17日).xlsx",index=False)

from pyecharts import options as opts
from pyecharts.charts import Bar

# with open("沧州天气日期.txt", "r", encoding='utf-8') as f:
#     df_list1 = f.read()
# x1 = df_list1.split("\n")
# y1 = df_list2.split("\n")
with open("total.txt", "r", encoding="utf-8") as f:
    total = f.read()
tt = total.split("\n")
list1 = []
y = []
x = []
for i in tt:
    if i[6] == "5" or i[6] == "6" or i[6] == "7" or i[6] == "8":
        list1.append(i)
for i in list1:
    temp_y = int(f"{i[-3]}{i[-2]}")
    y.append(temp_y)
    temp_x = f"{i[:13]}"
    x.append(temp_x)

print(y)
print(x)

c = (
    Bar(init_opts=opts.InitOpts(width='1400px', height='800px'))
    .add_xaxis(x)
    .add_yaxis("气温", y)
    .set_global_opts(title_opts=opts.TitleOpts(title="沧州夏季天气", subtitle=""))
    .render("沧州天气.html")
)





