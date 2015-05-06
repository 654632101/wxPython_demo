# -*- encoding:utf-8 -*-
import urllib2
import re
import os, sys
import time
from pyquery import PyQuery as pq

reload(sys)
sys.setdefaultencoding("utf-8")
 
def find58(html):
    d = pq(html)
    print '============================================================'
    ht = d("#infolist .tbimg")
    hh = pq(ht)
    hx = hh('a')
    href_list = []
    print len(hx)
    for hr in hx:
        sh = pq(hr)
        href_s = sh.attr('href')
#         print len(href_s)
#         print href_s
        if len(href_s) > 40:
            href_list.append(href_s)
    return href_list
def mx_58(html_mx):
    htm = pq(html_mx)
    msxx = htm('.maincon').text()
    print msxx 
    print '========================================================================='
    hhh = htm('ul').outerHtml().encode('utf-8')
    print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    mx = pq(hhh)
    lpmx = mx('li')
    print len(mx('li'))
    for mxxx in lpmx:
        x = pq(mxxx).text()
        print x
        writeTxt(x + '|')
    writeTxt(msxx)
    writeTxt('\n')
    print '========================================================================='
     
def readHtml(myUrl):       
    myResponse = urllib2.urlopen(myUrl) 
    print myResponse.geturl()
#     print myResponse.getcode()
#     print myResponse.info()
    myPage = myResponse.read()#.decode("utf-8") 
    unicodePage = myPage  
    return unicodePage
def writeTxt(body):
    f = open(r'fcxx.txt', 'a')
    f.write(body)
    f.close()  
falg_stop = 0 
# myUrl = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B2%88%E9%98%B3&kw=%E7%A8%8B%E5%BA%8F%E5%91%98&sm=0&sg=3505c0909b57409895a65a9dbf8b05e9&p=1'
# myUrl = 'http://sy.58.com/zhaozu/?PGTID=14281538140150.007925275512721375&ClickID=1'
# myUrl = 'http://sy.58.com/zhaozu/pn5/?PGTID=14284231663580.009569545356729825&ClickID=1'
def statusBug(unicodePage):
    f = open(r'pm.txt', 'w')
    f.write(unicodePage)
    f.close()
    # print unicodePage
    href_ss = find58(unicodePage)
    print '停止 300秒！'
    global falg_stop
    if falg_stop == 1:
        time.sleep(300)
    while href_ss:
        falg_stop = 1
        print href_ss.pop()
        htm = readHtml(href_ss.pop())
    #     print htm
        print '################################################################################'
        mx_58(htm)
        # 注释掉58爬虫程序
next_url = 'http://sy.58.com'
myUrl = 'http://sy.58.com/zhaozu/pn6/'
stop_flag = 0
bug_url = ['http://sy.58.com/zhaozu/pn51']
while bug_url:
    unicodePage = readHtml(bug_url.pop())
    next_flag = pq(unicodePage)
    fl = next_flag('.next').attr('href')
    print fl
    print next_url + str(fl)
    bug_url.append(next_url + str(fl))
    statusBug(unicodePage)
    stop_flag = 1


zlUrl = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B2%88%E9%98%B3&kw=%E7%A8%8B%E5%BA%8F%E5%91%98&sm=0&p=1'
# myUrl = 'http://sy.58.com/zhaozu/?PGTID=14281538140150.007925275512721375&ClickID=1'
# myUrl = 'http://sy.58.com/zhaozu/pn5/?PGTID=14284231663580.009569545356729825&ClickID=1'


# print '##################################################################################'
# # reg = re.compile('"pin_id":(.*?),.+?"file":{"farm":"farm1", "bucket":"hbimg",.+?"key":"(.*?)",.+?"type":"image/(.*?)"', re.S)
# reg = re.compile('<td class="zwmc">([\S\s]*?)</td>', re.S)
# groups = re.findall(reg, unicodePage)
# print groups
# a_reg = re.compile('<a style="font-weight: bold" href="([\S\s]*?)" target="_blank">', re.S)
# print len(groups)
# a_href =[]
# for line in groups:
#     print line
#     hellof = re.findall(a_reg, line)
#     print '##################################################################################'
#     print hellof
#     a_href.append(hellof)
# print a_href
# print '##################################################################################'
# while a_href:
#     print '##################################################################################'
#     print a_href.pop()

# def get59TC(myUrl):
#     unicodePage = readHtml(myUrl)
#     next_flag = pq(unicodePage)
#     fl = next_flag('.next')#.attr('href')
#     print fl
#     f = open(r'pm.txt', 'w')
#     f.write(unicodePage)
#     f.close()
#     # print unicodePage
#     href_ss = find58(unicodePage)
#     while href_ss:
#         print href_ss.pop()
#         htm = readHtml(href_ss.pop())
#     #     print htm
#         print '################################################################################'
#         mx_58(htm)
