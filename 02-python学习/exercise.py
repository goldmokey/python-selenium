#coding=utf-8
import time,requests

session = requests.Session()
url = 'http://test.cscec3b.com.cn'

print session.get(url)