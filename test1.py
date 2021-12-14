import pandas as pd
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from lxml import html

# a = input("Введите адрес distKontrol - ")
def usb_tab(a):
    url = f'http://{a}'
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page)
    tab = soup.find_all('tableview-1163')
    print(soup)


# tableview-1161

a = '10.10.1.183'
driver = webdriver.Firefox(executable_path=r'C:\\DKCL\\geckodriver.exe') # Using Firefox to access web
link = driver.get(f'http://{a}.') # Open the website

driver.find_element_by_name('username').send_keys('admin') # Send Login
driver.find_element_by_name('password').send_keys('Ker0v0hmt') # Send password
driver.find_element_by_id('ext-comp-1017-login').click() # Click login
driver.implicitly_wait(10)  # Wait
driver.find_element_by_id('treeview-1022-record-17').click() # User Tab
driver.implicitly_wait(10)  # Wait
driver.find_element_by_id('ext-comp-1104-add').click()
driver.implicitly_wait(10)  # Wait
driver.find_element_by_id('menuitem-1117').click() # Create User
driver.implicitly_wait(10)  # Wait
driver.find_element_by_id('textfield-1146-inputEl').send_keys('v.panin')  # Name
driver.find_element_by_id('passwordfield-1149-inputEl').send_keys('abcdefg')  # Password
driver.find_element_by_id('passwordfield-1150-inputEl').send_keys('abcdefg')  # Confirm Password
driver.find_element_by_id('tab-1184-btnInnerEl').click() # USB Table
driver.implicitly_wait(10)  # Wait
tables = usb_tab(a)
# driver.find_element_by_id("tableview-1161-record-50").click() # USB element 1.1
driver.find_element_by_id("ext-comp-1143-ok").click() # Save button
driver.implicitly_wait(20)  # Wait
driver.find_element_by_id("button-1067").click() # Success
driver.find_element_by_id("button-1006").click() # Success OK






# ('tab-1232') # USB Ports