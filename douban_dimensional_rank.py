import pandas as pd
from pyecharts import Scatter

# 读取文件
df = pd.read_csv('douban.csv', header=0, names=["quote", "score", "info", "title", "people"])
(dom2, dom3) = ([], [])
# 生成电影排名列表
dom1 = ["{}".format(i) for i in range(1, 251)]
# 生成电影评分列表
for i in df['score']:
    dom2.append(i)
# 生成电影评价人数列表
for i in df['people']:
    dom3.append(i.replace('人评价', ''))
# 生成数据列表
data = [list(i) for i in zip(dom1, dom2, dom3)]
# 生成散点图
x_lst = [v[0] for v in data]
y_lst = [v[1] for v in data]
extra_data = [v[2] for v in data]
sc = Scatter("豆瓣电影TOP250-排名评分人数三维度", title_pos='center', title_top='5', width=800, height=400)
sc.add("", x_lst, y_lst, yaxis_max=9.7, yaxis_min=8.2, extra_data=extra_data, is_visualmap=True, visual_dimension=2, visual_orient="horizontal", visual_type="size", visual_range=[50000, 1300000], visual_text_color="#000", visual_range_size=[5, 30])
sc.render('豆瓣电影TOP250排名三维度.html')
