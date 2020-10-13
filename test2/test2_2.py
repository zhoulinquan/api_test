import requests
from urllib import parse
import unittest


class test_sky(unittest.TestCase):
    def setUp(self):
        self.url = 'http://apis.juhe.cn/simpleWeather/query'

    def test_1(self):
        '''城市为空'''
        data = {'city':'','key':'4b65fdc25d09a36c154669a20219e024'}
        city = parse.urlencode(data).encode('utf-8')
        response = requests.get(self.url,params=city)
        a = response.json()
        assert a['reason'] == '城市不能为空或暂不支持该城市'
    def test_2(self):
        '''城市为重庆'''
        data = {'city':'重庆','key':'4b65fdc25d09a36c154669a20219e024'}
        city = parse.urlencode(data).encode('utf-8')
        response = requests.get(self.url,params=city)
        a = response.json()
        assert a['reason'] == '查询成功!'
        assert a['result']['city'] == '重庆'

if __name__ == '__main__':
    unittest.main()