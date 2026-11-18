from pydoc import html

import requests
from lxml import etree
url ='http://quotes.toscrape.com'
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
r = requests.get(url=url,headers=headers)

print(r.status_code)
html=etree.HTML(r.text)
elt=html.xpath('//div[@class="quote"]')
firsttag=elt[0]
for i,firsttag in enumerate (elt,1):#从1开始遍历firsttag
    a=firsttag.xpath('./span/text()')[0].strip()
    print(f"名言：{a}")
    b=firsttag.xpath('./span/small[@class="author"]/text()')[0].strip()
    q=firsttag.xpath(f'./span/a/@href')[0].strip()
    print(f'作者：{b} {url}{q}')
    c=','.join(firsttag.xpath('./div[@class="tags"]/a/text()'))
    print(f"标签：({c})")
    print('-'*40)