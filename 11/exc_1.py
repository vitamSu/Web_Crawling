import requests
from bs4 import BeautifulSoup
import pymysql
from pymysql.err import IntegrityError


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://movie.douban.com/top250"
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
soup = BeautifulSoup(resp.text, "html.parser")
movies_data = []


items = soup.select('div.article ol.grid_view li')
for item in items:
    # 排名
    rank = item.find("em").get_text(strip=True)
    # 电影名称
    title = item.find("span", class_="title").get_text(strip=True)
    # 评分
    rating = item.find("span", class_="rating_num").get_text(strip=True)
    # 引言（一句话简介）
    quote = item.find("p", class_="quote").get_text(strip=True)


    movies_data.append([rank,title,rating,quote])


for m in movies_data:
    print(m)
db = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "spider_db",
    "charset": "utf8mb4"
}
cursor = db.cursor
cursor.execute('USE spider_db')
sql = 'INSERT INTO douban_movies(id,title,rating.quote) VALUES(%s,%s,%s,%s)'
cursor.executemany(sql,m)
db.commit()
sql=''
results = cursor.fetchall()
