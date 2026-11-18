import json
import requests
url='https://weread.qq.com/web/bookListInCategory/newbook?maxIndex=20&rank1'
headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

r=requests.get(url=url,headers=headers,timeout=90)
print(r.status_code)
print(r.text)
print(f'相应格式{r.headers.get("Content-Type")}')
data=json.loads(r.text)
oneBook=data['books'][0]
print(oneBook)
print(
        f''{oneBook['title']}

)