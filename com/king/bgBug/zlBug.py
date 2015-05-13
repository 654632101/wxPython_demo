# -*- encoding:utf-8 -*-
import logging
import urllib2
import re
import os, sys
from com.king.vo.gsxx import gsmm
from pyquery import PyQuery as pq
from com.king.db.orclDb import orclDb
import time
import cookielib

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
    cj = cookielib.LWPCookieJar()  
    cookie_support = urllib2.HTTPCookieProcessor(cj)  
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
    urllib2.install_opener(opener) 
    myResponse = urllib2.urlopen(myUrl) 
    logging.info(myResponse.geturl())
#     logging.info( myResponse.getcode())
#     logging.info( myResponse.info())
    myPage = myResponse.read()  # .decode("utf-8") 
    unicodePage = myPage  
    return unicodePage
def writeTxt(body):
    f = open(r'zpxx_test.txt', 'a')
    f.write(body)
    f.close()  
    
# zlUrl = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B2%88%E9%98%B3&kw=%E7%A8%8B%E5%BA%8F%E5%91%98&sm=0&p=1']

#zlUrl = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B2%88%E9%98%B3&kw=%E8%BD%AF%E4%BB%B6&isadv=0&sg=53a0936a01f040efb26d4acfe0642ffb&p=1']
zlUrl = ['http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500%3B160400%3B160000%3B160500%3B300100%3B160100%3B200300&jl=%E6%B2%88%E9%98%B3&sm=0&p=1&sf=0&st=99999&isadv=1']
      
zl_href = []
db_Store = orclDb()
db = db_Store.conDb()
# 获取智联招聘初始页的thml
while zlUrl: 
    try:
        url_x = zlUrl.pop()
        html = readHtml(url_x)
    except:
        logging.error('链接解析错误%s',url_x)
        continue
    next_flag = pq(html)
    flag = next_flag('.next-page').attr('href')
    if flag == None:
        continue
    logging.info('114 ==== > ' + flag)
    zlUrl.append(flag)
    logging.info('################################################################################')
    findZL(html)
    logging.info('返回明细超链接 ===> ')
flag_num = 0
while zl_href:
    logging.info('################################################################################')
    ur = zl_href.pop()
    logging.info('执行URL ： ' + ur)
    # 获取到返回的明细HTML
    try:
        ret_html = readHtml(ur)
    except:
        logging.error('链接解析错误%s',ur)
        continue
    # 转成pq对象
    cc = pq(ret_html)
    # 解析出公司名称
    gsmc = cc('.inner-left a').text().encode('utf-8')
    if gsmc == '':
        continue
    # 创建用户对象，进行设置对象
    flag_num +=1
    print '插入数量%s',flag_num
    gszpxx = gsmm()
    gszpxx.setgsmc(gsmc)
    
    logging.info('公司名称 ： ' + gsmc)
    # 解析公司信息
    writeTxt('公司名称 ： ' + gsmc + '|')
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
                    fote = xs.lstrip()
                    if fote == '职位月薪':
                        gszpxx.setzwyx(msxx[1].lstrip())
                    if fote == '工作地点':
                        gszpxx.setgzdd(msxx[1].lstrip())
                    if fote == '发布日期':
                        gszpxx.setfbrq(msxx[1].lstrip())
                    if fote == '工作性质':
                        gszpxx.setgzxz(msxx[1].lstrip())
                    if fote == '工作经验':
                        gszpxx.setgzjy(msxx[1].lstrip())
                    if fote == '最低学历':
                        gszpxx.setzdxl(msxx[1].lstrip())
                    if fote == '招聘人数':
                        gszpxx.setzprs(msxx[1].lstrip())
                    if fote == '职位类别':
                        gszpxx.setzwlb(msxx[1].lstrip())
                    if fote == '公司规模':
                        gszpxx.setgsgm(msxx[1].lstrip())
                    if fote == '公司性质':
                        gszpxx.setgsxz(msxx[1].lstrip())
                    if fote == '公司行业':
                        gszpxx.setgshy(msxx[1].lstrip())
                    if fote == '公司地址':
                        gszpxx.setgsdz(msxx[1].lstrip())
                    if fote == '公司主页':
                        gszpxx.setgszy(msxx[1].lstrip())
                logging.info(msnr)
                writeTxt(msnr + '|')
#             print '职位月薪是: ' + gszpxx.zwyx
#             print '工作地点是: ' + gszpxx.gzdd
#             print '发布日期是: ' + gszpxx.fbrq
#             print '工作性质是: ' + gszpxx.gzxz
#             print '工作经验是: ' + gszpxx.gzjy
    except:
        raise
    # 解析公司介绍
    logging.info('公司介绍 : %s', cc('.tab-inner-cont').eq(1).text().encode('utf-8'))
    writeTxt(cc('.tab-inner-cont').eq(1).text().encode('utf-8') + '|')
    gszpxx.setgsjs(cc('.tab-inner-cont').eq(1).text().encode('utf-8'))
    logging.info('职位描述: %s', cc('.tab-inner-cont').eq(0).text().encode('utf-8'))
    writeTxt(cc('.tab-inner-cont').eq(0).text().encode('utf-8') + '|')
    gszpxx.setzwms(cc('.tab-inner-cont').eq(0).text().encode('utf-8'))
    writeTxt('\n')
#     print '公司介绍是:' + gszpxx.gsjs
#     print '职位描述是:' + gszpxx.zwms
    insert_sql = 'insert into Tb_BUG_INFO (RID, BUG_TYPE, QUERY_INFO, GSMC, YX, GZDD, FBSJ, GZXZ, GZJY, ZDXL, ZPRS, ZWLB, GSGM, GSSZ, HY, ZY, DZ, GSJS, GWZZ, BUG_DATA)'
    insert_sql += "values (TB_BUG_SEQ.NEXTVAL, '智联', '互联网', :GSMC, :YX, :GZDD, :FBSJ, :GZXZ, :GZJY, :ZDXL, :ZPRS, :ZWLB, :GSGM, :GSSZ, :HY, :ZY, :DZ, :GSJS, :GWZZ, sysdate)"
    parms = [gszpxx.gsmc,gszpxx.zwyx,gszpxx.gzdd,gszpxx.fbrq,
            gszpxx.gzxz,gszpxx.gzjy,gszpxx.zdxl,gszpxx.zprs,
            gszpxx.zwlb,gszpxx.gsgm,gszpxx.gsxz,gszpxx.gshy,gszpxx.gszy,gszpxx.gsdz,gszpxx.gsjs,gszpxx.zwms]
    flag = db_Store.insertData(db, insert_sql, parms)
    if flag == 1:
        logging.info('插入成功！')
    else:
        logging.error('插入失败！ %s',flag)
    logging.info('################################################################################')
#     time.sleep(3)
db_Store.closeDb(db)