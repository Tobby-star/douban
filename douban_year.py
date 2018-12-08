import pandas as pd
from pyecharts import Bar

# 读取文件
df = pd.read_csv('douban.csv', header=0, names=["quote", "score", "info", "title", "people"])
# 清洗数据,获取电影年份,增加年份列
dom = []
for i in df['info']:
    dom.append(i.split('/')[0].replace('(中国大陆)', '').strip())
df['year'] = dom
# 计数排序
place_message = df.groupby(['year'])
place_com = place_message['year'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom1 = place_com_last.sort_values('year', ascending=True)
# 生成柱状图
v1 = dom1['year']
attr = dom1['count']
bar = Bar("豆瓣电影TOP250-电影上映年份分布", title_pos='center', title_top='18', width=800, height=400)
bar.add("", v1, attr, is_label_show=True, is_datazoom_show=True)
bar.render('豆瓣电影TOP250上映年份分布.html')
