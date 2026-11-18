from pydoc import html

import requests
from lxml import etree
url ='http://quotes.toscrape.com/'
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
r = requests.get(url=url,headers=headers)

print(r.status_code)
html=etree.HTML(r.text)
elt=html.xpath('//div[@class="quote"]')[0]
a= elt.xpath('./span/text()')[0]
b=elt.xpath('./span/small[@class="author"]/text()')[0]
c=','.join(elt.xpath('./div[@class="tags"]/a/text()'))
print(a)
print(b)
print(c)