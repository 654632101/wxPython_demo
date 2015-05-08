# coding:utf-8
import cookielib  
import urllib2
import urllib
import os 
from com.king.captcha import cap
import Image
import cStringIO
path = os.getcwd()
print path

cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener) 
urllib2.urlopen('http://gsxt.lngs.gov.cn/saicpub/entPublicitySC/entPublicityDC/sEntDetail.action')
print '初始化页面'

# 获取返回的cookie
cookies = ''
cookvale = ''
session_id = ''
for index, ck in enumerate(cj):
    if ck.name == 'COOKIE':
        cookvale = ck.value
    else:
        session_id = ck.value
    cookies = cookies + ck.name + '=' + ck.value + ';'
cookie = cookies[:-1]
print cookie


headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'',
        'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2',
        'Referer':''
        }
imgData = {'tdate':'33333'}
imgData = urllib.urlencode(imgData)
req = urllib2.Request('http://gsxt.lngs.gov.cn/saicpub/commonsSC/loginDC/securityCode.action', imgData, headers)
repo = urllib2.urlopen(req)
file('D:\\workspace\\py_demo\\com\\king\\bgBug\\pic\\test.jpg', 'wb').write(repo.read())
print '下载验证图片......'

img = cap.binary(path + '/pic/test.jpg')
num = cap.recognize(img)
print num

postData = {'authCode':num,
            'solrCondition':'辽宁永乐科技产业发展有限公司'}
print postData
postData = urllib.urlencode(postData)   
request = urllib2.Request('http://gsxt.lngs.gov.cn/saicpub/entPublicitySC/entPublicityDC/lngsSearchFpc.action', postData, headers)
# response = urllib2.urlopen(request) 
sss = opener.open(request)
print sss.read()
# print response.read()
