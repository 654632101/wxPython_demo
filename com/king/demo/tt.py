#!/usr/bin python
#-*-coding:utf-8 -*-
import cookielib
import urllib
import urllib2

user = 'p_l'
passwd = '456'
proxyserver = 'proxy.neuedu.com:8080'
proxy = 'http://%s:%s@%s' % (user, passwd, proxyserver)
print proxy
opener = urllib2.build_opener( urllib2.ProxyHandler({'http':proxy}) )
urllib2.install_opener( opener )

# sContent = urllib2.urlopen('http://huaban.com/search/?q=人体结构')
sContent = urllib2.urlopen('http://huaban.com/search/?q=%E4%BA%BA%E4%BD%93%E7%BB%93%E6%9E%84&i3jrjhyb&page=2&per_page=20&wfl=1')
print sContent.read()