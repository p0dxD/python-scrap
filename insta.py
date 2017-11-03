import re
import sys

import urllib.request as ur
s = ur.urlopen("https://www.instagram.com/dnialvz/")
# s = ur.urlopen("https://www.instagram.com/explore/tags/"+sys.argv[1]+"/?hl=en")
size = 0 
for line in s.readlines():
	if re.match(b'.*src=\".*?\".*', line) is not None:
		for img in re.findall(b'src=\"https://.*?\"',line):
			f = open('/Users/joserodriguez/Desktop/test/'+str(size)+'.jpg', 'wb')
			f.write(ur.urlopen(img.decode("utf-8")[5:-1]).read())
			f.close()
			size += 1
from bs4 import BeautifulSoup
page = ur.urlopen('http://yahoo.com').read()
soup = BeautifulSoup(page, 'html.parser')
# print("PAGE:",soup.prettify())
print("PAGE:",soup.find('img'))