
# scrapy
import sys
from tkinter import *
from bs4 import BeautifulSoup
import urllib.request as ur
import re
import random
import mechanicalsoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
account = "THEIRACCOUNT"
password = "PASSWORD"
youraccount = "YOURACCOUNT"
imagepath = '/Users/joserodriguez/Documents/python/test/'

words = ["wow", "very nice!", "😲", "f4f?", "xd", "XD","😀","😳"]
class Error(Exception):
    '''Base class for exceptions in this module.'''
    pass

#raised for different exeptions
class TimeoutException(Error):
    '''Exception raised for errors in the input.'''
    pass  

def my_element(delay, by, element):
	global driver
	try:
		myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((by, element)))
		print("Page is ready!")
		return myElem
	except TimeoutException:
		print("Loading took too much time!")

def fill_item():
	global driver
	driver = webdriver.Firefox()
	driver.get("https://www.instagram.com/")
	delay = 20 # seconds
	myElem = my_element(delay,By.CLASS_NAME, '_b93kq')

	elem = driver.find_element_by_class_name('_b93kq').click()
	elem = driver.find_element_by_name("username")
	elem.clear()
	elem.send_keys(youraccount)
	elem = driver.find_element_by_name("password")
	elem.clear()
	elem.send_keys(password)
	elem.send_keys(Keys.RETURN)

	myElem = my_element(delay+10, By.CLASS_NAME, '_avvq0')
	elem = driver.find_element_by_class_name('_avvq0')
	elem.clear()
	elem.send_keys(account)
	elem.click()

	myElem = my_element(delay+10, By.CLASS_NAME, '_gimca')
	elem = driver.find_element_by_class_name('_gimca').click()

	test = driver.page_source
	soup = get_page_elemts_from_source(test)

	like = False
	comment = False

	for a in soup.find_all('a', href=True):
		if a.get('href').startswith('/p/'):
			print("Test: ",a.get('href'))
			driver.get("https://www.instagram.com"+a.get('href'))
			if(like):
				myElem = my_element(delay+10, By.CLASS_NAME, '_eszkz')
				elem = driver.find_element_by_class_name('_eszkz').click()
			elif(comment):
				#_bilrf
				myElem = my_element(delay+10, By.CLASS_NAME, '_p6oxf')
				elem = driver.find_element_by_class_name('_p6oxf').click()
				elem = driver.find_element_by_class_name('_bilrf')
				elem.send_keys(words[random.randint(0,len(words)-1)])
				elem.send_keys(Keys.RETURN)


def images(soup):
	size = 0 
	for img in soup.find_all('img'):	
		if img.get('src').startswith('http'):
			f = open(imagepath+str(size)+'.jpg', 'wb')
			f.write(ur.urlopen(img.get('src')).read())
			f.close()
			size += 1

def get_page_elements(url):
	print("here")
	page = ur.urlopen(url).read()
	soup = BeautifulSoup(page, 'html.parser')
	print("returning")
	return soup

def get_page_elemts_from_source(source):
	soup = BeautifulSoup(source, 'html.parser')
	print("returning")
	return soup

#GUI
def get_images():
    global e
    url = e.get()
    #parse
    page = ur.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    # images(soup)
    fill_item()

def main():
	global e
	#GUI
	root = Tk()
	root.title('Name')
	e = Entry(root)
	e.delete(0, END)
	e.insert(0, "https://www.instagram.com/explore/tags/frontpage/?hl=en")
	e.pack()
	e.focus_set()
	b = Button(root,text='Get images',command=get_images)
	b.pack(side='bottom')
	root.mainloop()

main()
