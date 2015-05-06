#coding=utf-8
import urllib2  
import cookielib  
import time

city = ['shenyang','dalian','anshan','benxi','dandong','jinzhou','yingkou','fuxin','liaoyang','panjin','tieling','chaoyang','huludao']
def queryPm(city_name):
    pm_url = "http://www.pm25.in/api/querys/pm2_5.json?city=" + city_name + "&token=5j1znBVAsnSf5xQyNQyq"
    cj = cookielib.LWPCookieJar()  
    cookie_support = urllib2.HTTPCookieProcessor(cj)  
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
    urllib2.install_opener(opener)  
    h = urllib2.urlopen(pm_url)  
    html = h.read()
    print html
    writeTxt(html)
    
def CirculeGo():
    while True:
        print time.ctime()
        print len(city)
        for ci in city:
            city_name = ci
            queryPm(city_name)
        time.sleep(60*60)

def writeTxt(body):
    f = open(r'pm.txt','a')
    f.write('\n' + body)
    f.close()

CirculeGo()