import urllib
import urllib.error
import urllib.request
import urllib.parse

url = ' https://movie.douban.com/top250'
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req, timeout=5)
status_code = response.getcode()
html_bytes = response.read()
content_len = len(html_bytes)
print(f"{content_len},{status_code}\n{html_bytes},")