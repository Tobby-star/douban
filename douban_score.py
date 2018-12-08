import pandas as pd
from pyecharts import Bar

# 读取文件
df = pd.read_csv('douban.csv', header=0, names=["quote", "score", "info", "title", "people"])
(dom1, dom2) = ([], [])
# 计数排序
place_message = df.groupby(['score'])
place_com = place_message['score'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom3 = place_com_last.sort_values('score', ascending=True)
# 生成柱状图
attr = dom3['score']
v1 = dom3['count']
bar = Bar("豆瓣电影TOP250-电影评分分布", title_pos='center', title_top='18', width=800, height=400)
bar.add("", attr, v1, is_stack=True, is_label_show=True, yaxis_max=60)
bar.render("豆瓣电影TOP250评分分布.html")