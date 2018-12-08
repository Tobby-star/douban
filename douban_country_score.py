import pandas as pd
from pyecharts import Boxplot

# 读取文件
df = pd.read_csv('douban.csv', header=0, names=["quote", "score", "info", "title", "people"])
(dom1, dom2) = ([], [])
# 清洗数据,获取电影年份及国家,增加年份列及国家列
for i in df['info']:
    country = i.split('/')[1].split(' ')[0].strip()
    if country in ['中国大陆', '台湾', '香港']:
        dom1.append('中国')
    else:
        dom1.append('外国')
    dom2.append(i.split('/')[0].replace('(中国大陆)', '').strip())
df['country'] = dom1
df['year'] = dom2
# 获取特定数据
df1 = df.loc[df['country'] == '中国']
df2 = df.loc[df['country'] == '外国']
# 生成箱形图
boxplot = Boxplot("豆瓣电影TOP250-中外电影评分情况", title_pos='center', title_top='18', width=800, height=400)
x_axis = ['中国', '外国']
y_axis = [df1['score'], df2['score']]
_yaxis = boxplot.prepare_data(y_axis)
boxplot.add("", x_axis, _yaxis, yaxis_min=8, yaxis_max=10)
boxplot.render("豆瓣电影TOP250中外评分情况.html")