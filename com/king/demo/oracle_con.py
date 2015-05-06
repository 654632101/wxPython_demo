import re 
import lxml
import pyquery
from lxml import etree
d=pyquery("<html></html>")
print d.html();
co = re.compile('abc\w*')
stra = 'abcderg'
print re.findall(co, stra)

html  = '<input type="text" class="textfield" name="ffff" id="nt1414720869978"  />'
cso = re.compile('<input type="text" class="textfield" name="(.+?)"')

print re.findall(cso,html)