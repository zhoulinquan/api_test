import requests
from urllib import parse
import json


url = 'http://v.juhe.cn/xhzd/query'
data = {'word': '', 'dtype': '','key':'d7a20bf63efef9bd829154fdf928d398'}
b = parse.urlencode(data).encode('utf-8')
response = requests.get(url, params = b)
a = response.json()
print(a)