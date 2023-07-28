import re
import requests
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

country_list = []
gdp_list = []


def get_gdp():
    res = requests.get('http://127.0.0.1:8000/gdp.html')
    data = res.content.decode('utf-8')
    data = data.split('\n')
    for row in data:
        result1 = re.match('.*<a href=""><font>(.*)</font></a>.*',
                           row)  # <td>&nbsp;&nbsp;<a href=""><font>波兰</font></a></td>
        if result1:
            country_list.append(result1.group(1))
        result2 = re.match('.*￥(.*)亿元.*', row)  # <td class="rank_prev"><font>￥41194.3686亿元</font></td>
        if result2:
            gdp_list.append(float(result2.group(1)))

    # print(country_list)
    # print(gdp_list)
    # 把以上得到的结果转换为[(),(),()]
    data = list(zip(country_list, gdp_list))

    c = (
        Pie()
            .add("", data)
            .set_global_opts(title_opts=opts.TitleOpts(title="2020全球GDP"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .render("GDP2020.html")
    )


if __name__ == '__main__':
    get_gdp()
