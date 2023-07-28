from pyecharts import options as opts
from pyecharts.charts import Bar

with open("沧州天气日期.txt", "r", encoding='utf-8') as f:
    df_list1 = f.read()
with open("沧州天气气温.txt", "r", encoding='utf-8') as f:
    df_list2 = f.read()

x = df_list1.split("\n")
y1 = df_list2.split("\n")
y = []
# print(x)
# print(y)
for i in y1:
    y.append(int(i))

c = (
    Bar(init_opts=opts.InitOpts(width='1400px', height='800px'))
    .add_xaxis(x)
    .add_yaxis("气温", y)
    .set_global_opts(title_opts=opts.TitleOpts(title="沧州天气", subtitle=""))
    .render("沧州天气.html")
)

