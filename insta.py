import sys
from tkinter import *
from bs4 import BeautifulSoup
import urllib.request as ur
import re
import mechanicalsoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def click_item():
	print("in here")
	driver = webdriver.Firefox()
	driver.get("https://www.python.org")
	assert "Python" in driver.title
	elem = driver.find_element_by_class("a")
	elem.clear()
	# elem.send_keys("pycon")
	# elem.send_keys(Keys.RETURN)
	assert "No results found." not in driver.page_source
	# driver.close()
	print("done")

def images(soup):
	size = 0 
	for img in soup.find_all('img'):	
		if img.get('src').startswith('http'):
			f = open('/Users/joserodriguez/Documents/python/test/'+str(size)+'.jpg', 'wb')
			f.write(ur.urlopen(img.get('src')).read())
			f.close()
			size += 1


#GUI
def get_images():
    global e
    url = e.get()
    #parse
    page = ur.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    images(soup)
    click_item()

def main():
	global e
	#GUI
	root = Tk()
	root.title('Name')
	e = Entry(root)
	e.delete(0, END)
	e.insert(0, "https://www.instagram.com/(username)")
	e.pack()
	e.focus_set()
	b = Button(root,text='Get images',command=get_images)
	b.pack(side='bottom')
	root.mainloop()

main()
