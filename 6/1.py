from pydoc import html

import requests
from lxml import etree
url ='http://quotes.toscrape.com/'
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
r = requests.get(url=url,headers=headers)

print(r.status_code)

a=etree.HTML(r.text)
print(a)
c= a.xpath('//h1/a/text()')[0]#标题
print(c)