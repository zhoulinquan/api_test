import requests
from urllib import parse
import unittest
import json

class test_dic(unittest.TestCase):
    def setUp(self):
        self.url = 'http://v.juhe.cn/xhzd/query'

    def test_1(self):
        '''字典为空'''
        data = {'word':'','dtype':'','key':'d7a20bf63efef9bd829154fdf928d398'}
        data1 = parse.urlencode(data).encode('utf-8')
        response = requests.get(self.url,params = data1)
        a = response.json()
        assert a['reason'] == "请输入需要查询的汉字"
    def test_2(self):
        '''字典为五'''
        data = {'word':'五','dtype':'','key':'d7a20bf63efef9bd829154fdf928d398'}
        data1 = parse.urlencode(data).encode('utf-8')
        response = requests.get(self.url,params = data1)
        a = response.json()
        assert a['reason'] == "返回成功"
        assert a['result']['zi'] == '五'
    def test_3(self):
        '''字典为六'''
        data = {'word':'六','dtype':'','key':'d7a20bf63efef9bd829154fdf928d398'}
        data1 = parse.urlencode(data).encode('utf-8')
        response = requests.get(self.url,params = data1)
        a = response.json()
        assert a['reason'] == "返回成功"
        assert a['result']['zi'] == '六'

if __name__ == '__main__':
    unittest.main()