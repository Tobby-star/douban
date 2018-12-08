import pandas as pd
from pyecharts import Bar

# 读取文件
df = pd.read_csv('douban.csv', header=0, names=["quote", "score", "info", "title", "people"])
dom1 = []
# 生成电影国家列表
for i in df['info']:
    country = i.split('/')[1].split(' ')[0].strip()
    dom1.append(country)
df['country'] = dom1
# 计数排序
place_message = df.groupby(['country'])
place_com = place_message['country'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom2 = place_com_last.sort_values('count', ascending=False)[0:10]
# 生成柱状图
attr = dom2['country']
v1 = dom2['count']
bar = Bar("豆瓣电影TOP250-国家/地区电影数TOP10", title_pos='center', title_top='18', width=800, height=400)
bar.add("", attr, v1, is_convert=True, xaxis_min=0, yaxis_label_textsize=12, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=True, is_legend_show=False, label_pos='right', is_yaxis_inverse=True, is_splitline_show=False)
bar.render("豆瓣电影TOP250国家地区TOP10.html")