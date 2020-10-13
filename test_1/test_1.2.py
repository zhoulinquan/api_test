import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
data = {}
data['query'] = 'i love you'

data['transtype'] = 'translang'
data['simple_means_flag'] = '3'
data['sign'] = '127170.332787'
data['token'] = 'fcf4d6e9ac6f9de95a71523fc15259ce'
data['domain'] = 'common'
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
print(html)