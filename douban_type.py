import pandas as pd
from pyecharts import TreeMap

# 读取文件
df = pd.read_csv('douban.csv', header=0, names=["quote", "score", "info", "title", "people"])
(dom1, dom2, dom3, dom4) = ([], [], [], [])
# 获取每部电影类型数据
for i in df['info']:
    dom1.append(i.split('/')[2].replace('\xa0', '').replace(' 1978(中国大陆) ', ''))
# 获取电影类型类别
for j in dom1:
    res = j.split(' ')
    for re in res:
        if re not in dom2:
            dom2.append(re)
        else:
            pass
# 电影类型类别对应数量
for k in dom2:
    num = 0
    for j in dom1:
        res = j.split(' ')
        for re in res:
            if re == k:
                num += 1
    dom3.append(num)


def message():
    # 生成字典形式
    for p in range(len(dom2)):
        data = {}
        data['name'] = dom2[p] + ' ' + str(dom3[p])
        data['value'] = dom3[p]
        yield data


# 生成类型图
data = message()
for item in data:
    dom4.append(item)
treemap = TreeMap("豆瓣电影TOP250-电影类型图", title_pos='center', title_top='5', width=800, height=400)
treemap.add('电影类型', dom4, is_label_show=True, label_pos='inside', is_legend_show=False)
treemap.render('豆瓣电影TOP250电影类型图.html')