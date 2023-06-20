#!python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys as K
import time

browser = webdriver.Firefox()
browser.get('https://gamemora.com')

time.sleep(2)

#agreeElem = browser.find_element('id', 'ez-accept-all')
#agreeElem.click()

time.sleep(1)

htmlElem = browser.find_element('tag name', 'body')
gridElem = browser.find_element('class name', 'grid-container')
gridElem.click()

direction = ['\ue013','\ue014','\ue015','\ue012']
count = 0

while True:
    count += 1
    htmlElem.send_keys(direction[count % 4])
    time.sleep(2.5)

print
