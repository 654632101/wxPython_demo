#coding:gbk
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  


hosturl = 'http://kq.neusoft.com/index.jsp' 

posturl = 'http://kq.neusoft.com/login.jsp' 

puturl = 'http://kq.neusoft.com/record.jsp'


cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  

h = urllib2.urlopen(hosturl)  
html = h.read()
print html
reso = re.compile('<input type="text" name="(.+?)"')
Key_re = re.compile('<input type="hidden" name="neusoft_key" value="(.+?)"')
user_re = re.compile('<input type="text" class="textfield" name="(.+?)"')
password_re = re.compile('<input type="password" class="textfield" name="(.+?)"')
parms = re.findall(reso, html)
Key = re.findall(Key_re, html)
user = re.findall(user_re, html)
password = re.findall(password_re, html)
# print  parms
# print parms[0]
# print Key
# print user
# print password
my_username = 'p_l'
my_password = 'qwe!@#123'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
     'Referer' : 'http://kq.neusoft.com/index.jsp'}  
postData = {'login' : 'true',
      parms[0] : '',
      parms[1] : '',
      'neusoft_key' : Key[0],
      user[0] : my_username,
      password[0] : my_password
      }  

postData = urllib.urlencode(postData)  

print postData
request = urllib2.Request(posturl, postData, headers)  
# print request  
response = urllib2.urlopen(request)  
 
#��¼ϵͳ������ȡ���ص�ҳ���ı�
text = response.read() 
#��GBK��ʽ���ı��ļ�ת����utf8
utf_html = unicode(text, "gbk").encode("utf8")

#ͨ��������ʽ��ȡ��Ҫ���ı�Ԫ��
flag = re.compile('<td height="29" align="center" class="black12">(.+?)</td>')
#��ȡ������
flag_s = re.findall(flag, utf_html)

# print utf_html  
print flag_s
# print len(flag_s)
# print flag_s[1]
# print flag_s[4]
# print flag_s[6]
# print flag_s[9]


# if(flag_s == []):
#     print 'null'
#     putData = {'currentempoid':'1908494386'}
#     putData = urllib.urlencode(putData)  
#     
#     request_put = urllib2.Request(puturl, putData, headers) 
#     response_put = urllib2.urlopen(request_put)  
#     print response_put.read() 
# else:
#     print flag_s
#     print flag_s[4]
    
    
putData = {'currentempoid':'1908494386'}
putData = urllib.urlencode(putData)  
   
request_put = urllib2.Request(puturl, putData, headers) 
response_put = urllib2.urlopen(request_put)  
print response_put.read() 
      
