import time
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
#浏览器初始化
option = webdriver.ChromeOptions()
option.binary_location='D:\\zxl\\aa\\Book-env\\data\\Chrome\\Application\\chrome.exe'
option.add_experimental_option('detach',True)
#浏览器对象
driver=webdriver.Chrome(options=option)

#打开网站
driver.get(url='https://www.ryjiaoyu.com/')

time.sleep(5)
#定位元素

book_imgs_tag=driver.find_elements(By.XPATH,'//*[@id="block-102"]/ul/li/div/a/img')
book_imgs_title=driver.find_elements(By.XPATH,'//*[@id="block-102"]/ul/li/div/a[title]')
print(len(book_imgs_tag))
print(len(book_imgs_title))
i=1
for book_tag in book_imgs_tag:
    img_url=book_tag.get_attribute('src')
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        ,'Referer':'https://www.ryjiaoyu.com/'
    }

    rspn=requests.get(url=img_url,headers=header,timeout=15)
    img_name = f'./temp/{i}.png'
    with open(img_name,'wb') as f:
        f.write(rspn.content)
    print(f'保存到{img_name}')
    i=i+1




