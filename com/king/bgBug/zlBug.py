# -*- encoding:utf-8 -*-
import logging
import urllib2
import re
import os, sys
from pyquery import PyQuery as pq

LOG_FILENAME = "log_test.log"
logging.basicConfig(filename=LOG_FILENAME, level=logging.NOTSET, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def findZL(html):
    d = pq(html)
    logging.info('============================================================')
    zwmc = d(".zwmc")
#     logging.info( zwmc )
    a_href = pq(zwmc)
    logging.info('============================================================')
    logging.info('17=====>' + str(a_href))
    logging.info('============================================================')
    hr = a_href('a')
    logging.info('20====>' + str(hr))
    for li in hr:
        hre = pq(li)
        logging.info(hre.attr('href'))
        logging.info('25 ==== > ' + str(len(hre.attr('href'))))
        if str(len(hre.attr('href'))) > 50:
            zl_href.append(hre.attr('href'))
def readHtml(myUrl):       
    myResponse = urllib2.urlopen(myUrl) 
    logging.info(myResponse.geturl())
#     logging.info( myResponse.getcode())
#     logging.info( myResponse.info())
    myPage = myResponse.read()  # .decode("utf-8") 
    unicodePage = myPage  
    return unicodePage
def writeTxt(body):
    f = open(r'zpxx_1.txt', 'a')
    f.write(body)
    f.close()  
    
zlUrl = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B2%88%E9%98%B3&kw=%E7%A8%8B%E5%BA%8F%E5%91%98&sm=0&p=1']

#zlUrl = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=沈阳&kw=软件&isadv=0&sg=53a0936a01f040efb26d4acfe0642ffb&p=1']
         
zl_href = []
# 获取智联招聘初始页的thml
while zlUrl: 
    html = readHtml(zlUrl.pop())
    next_flag = pq(html)
    flag = next_flag('.next-page').attr('href')
    if flag == None:
        continue
    logging.info('114 ==== > ' + flag)
    zlUrl.append(flag)
    logging.info('################################################################################')
    findZL(html)
    logging.info('返回明细超链接 ===> ')
while zl_href:
    logging.info('################################################################################')
    ur = zl_href.pop()
    logging.info('执行URL ： ' + ur)
    # 获取到返回的明细HTML
    ret_html = readHtml(ur)
    # 转成pq对象
    cc = pq(ret_html)
    # 解析出公司名称
    gsmc = cc('.inner-left a').text().encode('utf-8')
    if gsmc == '':
        continue
    logging.info('公司名称 ： ' + gsmc)
    writeTxt('公司名称 ： ' + gsmc + '|')
    # 解析公司信息
    try:
        sts = cc('.terminal-ul')
        logging.info('获取的元素个数 : %s' , len(sts))
        for mx in sts:
            xx = pq(mx)
            xxx = xx('li')
            for x in xxx:
                msnr = pq(x).text().encode('utf-8')
                msxx = msnr.split('：')
                for xs in msxx:
                    print xs.lstrip()
                    print '===='
                logging.info(msnr)
                writeTxt(msnr + '|')
    except:
        raise
    # 解析公司介绍
    logging.info('公司介绍 : %s', cc('.tab-inner-cont').eq(1).text().encode('utf-8'))
    writeTxt(cc('.tab-inner-cont').eq(1).text().encode('utf-8') + '|')
    logging.info('职位描述: %s', cc('.tab-inner-cont').eq(0).text().encode('utf-8'))
    writeTxt(cc('.tab-inner-cont').eq(0).text().encode('utf-8') + '|')
    writeTxt('\n')
    logging.info('################################################################################')
