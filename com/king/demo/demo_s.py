# coding:gbk
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
from com.king.demo.demo import utf_html

class LoginKq():
    def __init__(self, user_name, pass_word):
       
        self.hosturl = 'http://kq.neusoft.com/index.jsp' 

        self.posturl = 'http://kq.neusoft.com/login.jsp' 
        
        self.puturl = 'http://kq.neusoft.com/record.jsp'
        
        self.headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
                     'Referer' : 'http://kq.neusoft.com/index.jsp'} 
        
        self.my_username = user_name
        self.my_password = pass_word
        
    def login(self):
        cj = cookielib.LWPCookieJar()  
        cookie_support = urllib2.HTTPCookieProcessor(cj)  
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
        urllib2.install_opener(opener)  
        h = urllib2.urlopen(self.hosturl)  
        html = h.read()

        reso = re.compile('<input type="text" name="(.+?)"')
        Key_re = re.compile('<input type="hidden" name="neusoft_key" value="(.+?)"')
        user_re = re.compile('<input type="text" class="textfield" name="(.+?)"')
        password_re = re.compile('<input type="password" class="textfield" name="(.+?)"')
        parms = re.findall(reso, html)
        Key = re.findall(Key_re, html)
        user = re.findall(user_re, html)
        password = re.findall(password_re, html)

        postData = {'login' : 'true',
              parms[0] : '',
              parms[1] : '',
              'neusoft_key' : Key[0],
              user[0] : self.my_username,
              password[0] : self.my_password
              }  
        
        postData = urllib.urlencode(postData)  
        
#         print postData
        request = urllib2.Request(self.posturl, postData, self.headers)  
        # print request  
        response = urllib2.urlopen(request)  
 
        # 登录系统，并读取返回的页面文本
        text = response.read() 
        # 把GBK格式的文本文件转换成utf8
        # utf_html = unicode(text, "gbk").encode("utf8")
        utf_html = text
        # 通过正则表达式获取需要的文本元素
        flag = re.compile('<td height="29" align="center" class="black12">(.+?)</td>')
        # 获取成数组
        flag_s = re.findall(flag, utf_html)
#         print flag_s[1]
#         return flag_s
    def Dk(self):
        print 'here DK(self)'
#         putData = {'currentempoid':'1908494386'}
#         putData = urllib.urlencode(putData)  
#            
#         request_put = urllib2.Request(self.puturl, putData, self.headers) 
#         response_put = urllib2.urlopen(request_put)  
#         print response_put.read() 
    
    

      
