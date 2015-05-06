#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# author :insun
# http://yxmhero1989.blog.163.com/blog/static/112157956201311994027168/
import urllib, urllib2, re, sys, os
reload(sys)
 
 
# url = 'http://huaban.com/favorite/'
if(os.path.exists('beauty') == False):
    os.mkdir('beauty')
 
def get_huaban_beauty():
    pin_id = 48145457
    limit = 20  # 他默认允许的limit为100
    page = 1
    while pin_id != None:
#         url = 'http://huaban.com/favorite/beauty/?max=' + str(pin_id) + '&limit=' + str(limit) + '&wfl=1'
        url = 'http://huaban.com/search/?q=%E9%AD%94%E5%85%BD%E4%B8%96%E7%95%8C%E5%8E%9F%E7%94%BB&i4ignua0&page='+str(page) + '&per_page=20&wfl=1'
        page += 1
        print url
        try:
            i_headers = {"User-Agent": "Mozilla/5.0(Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1)\
            Gecko/20090624 Firefox/3.5", \
            "Referer": 'http://baidu.com/'}
            user = 'p_l'
            passwd = '456'
            proxyserver = 'proxy.neuedu.com:8080'
            proxy = 'http://%s:%s@%s' % (user, passwd, proxyserver)
#             opener = urllib2.build_opener(urllib2.ProxyHandler({'http':proxy}))
#             urllib2.install_opener(opener)
            
#             req = urllib2.Request(url, headers=i_headers)
            html = urllib2.urlopen(url).read()
#             print html
            reg = re.compile('"pin_id":(.*?),.+?"file":{"farm":"farm1", "bucket":"hbimg",.+?"key":"(.*?)",.+?"type":"image/(.*?)"', re.S)
            groups = re.findall(reg, html)
            print str(pin_id) + " Start to catch " + str(len(groups)) + " photos"
            if groups == None:
                print 'over'
                return
            else:
                for att in groups:
                    print att
                    pin_id = att[0]
                    att_url = att[1] + '_fw658'
                    img_type = att[2]
                    img_url = 'http://img.hb.aicdn.com/' + att_url
                   
                    if(urllib.urlretrieve(img_url, 'beauty/wow/' + att_url + '.' + img_type)):
                        print img_url + '.' + img_type + ' download success!'
                    else:
                        print img_url + '.' + img_type + ' save failed'
                        
                    print pin_id
        except:
            print 'error occurs'
 
 
get_huaban_beauty()
