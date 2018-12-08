import pandas as pd
from pyecharts import Line

# 读取文件
df = pd.read_csv('douban.csv', header=0, names=["quote", "score", "info", "title", "people"])
(dom1, dom2, dom6, dom7) = ([], [], [], [])
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
# 对中国电影计数排序
df_last = df.loc[df['country'] == '中国']
place_message = df_last.groupby(['year'])
place_com = place_message['year'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom3 = place_com_last.sort_values('year', ascending=True)
# 对外国电影计数排序
df_last_1 = df.loc[df['country'] == '外国']
place_message = df_last_1.groupby(['year'])
place_com = place_message['year'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom4 = place_com_last.sort_values('year', ascending=True)
# 对所有电影计数排序,获取完整年份时间
place_message = df.groupby(['year'])
place_com = place_message['year'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom5 = place_com_last.sort_values('year', ascending=True)
# 横坐标
attr = ["{}".format(i) for i in dom5['year']]
# 中国电影纵坐标
for j in attr:
    for x, y in zip(dom3['year'], dom3['count']):
        if x == j:
            aaa = int(y)
            break
        else:
            aaa = int('0')
            continue
    dom6.append(aaa)
# 外国电影纵坐标
for j in attr:
    for x, y in zip(dom4['year'], dom4['count']):
        if x == j:
            aaa = int(y)
            break
        else:
            aaa = int('0')
            continue
    dom7.append(aaa)
# 生成折线图
line = Line("豆瓣电影TOP250-中外电影上映年份分布", title_pos='center', title_top='0', width=800, height=400)
line.add("中国", attr, dom6, line_color='red', legend_top='8%')
line.add("外国", attr, dom7, line_color='purple', legend_top='8%')
line.render("豆瓣电影TOP250中外上映年份分布.html")

