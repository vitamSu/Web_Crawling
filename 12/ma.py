import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv('douban_top250.csv',encoding='utf-8-sig')
df['短评'] = df['短评'].fillna('无短评')
df['年份'] = df['年份'].astype(str).str[:4]

#柱状图

top10 = df.head(10)
plt.figure(figsize=(8,4))
plt.bar(top10['电影名'],top10['评分'],color='skyblue')
plt.title('豆瓣TOP10评分排行')
plt.ylim(8.5,9.7)
plt.xticks(rotation=45)
plt.xlabel("电影名")
plt.ylabel("评分")
plt.tight_layout()
plt.show()
#年份折线图
year_counts = df['年份'].value_counts ().sort_index()
plt.figure(figsize=(10,4))
plt.plot(year_counts.index,year_counts.values,color = 'green',marker='o')
plt.title("豆瓣Top250 电影年份分布趋势")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#评分分布直方图
plt.figure(figsize=(6,4))
plt.hist(df['评分'],bins=10,color='orange',edgecolor='black',alpha=0.7)
plt.title("评分分布直方图")
plt.show()

#散点图
plt.figure(figsize=(6,4))
plt.scatter(df['评价人数'],df['评分'],alpha=0.5,color='purple')
plt.title("评价与评分关系")
plt.xlabel("评价人数")
plt.ylabel("评分")
plt.show()

#国家占比饼图
country_counts= df['国家'].value_counts().head(5)
plt.figure(figsize=(5,5))
#自动显示保留一位小数的百分比
plt.pie(country_counts.values,labels=country_counts.index,autopct='%1.1f%%')
plt.title("前5大国家/地区电影占比")
plt.show()

#多图布局

# 创建 2行2列 的画布，尺寸为 14x10
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. 左上图 (索引为 [0, 0])：折线图
axes[0, 0].plot(year_counts.index, year_counts.values, color='green', marker='o')
# 注意：在多图布局中，设置标题用 set_title()
axes[0, 0].set_title("电影年份分布趋势")
axes[0, 0].tick_params(axis='x', rotation=90)
axes[0,0].set_xlabel("年份")
axes[0,0].set_ylabel("电影数量")

# 2. 右上图 (索引为 [0, 1])：直方图
axes[0, 1].hist(df['评分'], bins=10, color='orange', edgecolor='black', alpha=0.7)
axes[0, 1].set_title("评分分布直方图")
axes[0, 1].set_xlabel("评分")


# 3. 左下图 (索引为 [1, 0])：散点图
axes[1, 0].scatter(df['评价人数'], df['评分'], alpha=0.5, color='purple')
axes[1, 0].set_title("评价人数与评分关系")

# 4. 右下图 (索引为 [1, 1])：饼图
axes[1, 1].pie(country_counts.values, labels=country_counts.index, autopct='%1.1f%%')
axes[1, 1].set_title("前5大国家占比")

# 自动调整子图间距并展示
plt.tight_layout()
plt.show()


