import pandas as pd
from pyecharts import Bar

# 读取文件
df = pd.read_csv('douban.csv', header=0, names=["quote", "score", "info", "title", "people"])
(dom1, dom2) = ([], [])
# 清洗数据,建立评价人数列
for i in df['people']:
    dom1.append(i.replace('人评价', ''))
df['people_last'] = dom1
# 清洗数据,建立电影名称列(取第一个)
for j in df['title']:
    dom2.append(j.split('/')[0].strip())
df['title_last'] = dom2
# 切换为整型
df["people_last"] = df["people_last"].astype("int")
# 计数排序,取前10
dom3 = df[['title_last', 'people_last']].sort_values('people_last', ascending=False)[0:10]
# 生成柱状图
attr = dom3['title_last']
v1 = dom3['people_last']
bar = Bar("豆瓣电影TOP250-评论人数TOP10", title_pos='center', title_top='18', width=800, height=400)
bar.add("", attr, v1, is_convert=True, xaxis_min=700000, yaxis_rotate=0, yaxis_label_textsize=10, is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=True, is_legend_show=False, label_pos='right', is_yaxis_inverse=True, is_splitline_show=False)
bar.render("豆瓣电影TOP250评论人数TOP10.html")