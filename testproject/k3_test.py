from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html"

driver.get(URL)
time.sleep(1)

# web elements
title = driver.find_element_by_id('title')
error = driver.find_element_by_xpath('//span')

# test data
name = ['abcd1234', 'teszt233@', 'abcd', ]
message = ["", "Only a-z and 0-9 characters allewed", "Title should be at least 8 characters; you entered 4."]


def filler(a, b):
    title.send_keys(a)
    time.sleep(1)
    assert error.text == b
    title.clear()


def correct_test():
    # TC01 helyes kitöltés
    filler(name[0], message[0])


def bad_character_test():
    # TC02 illegális karakter
    filler(name[1], message[1])


def short_character_test():
    # TC03 rövid bemenet
    filler(name[2], message[2])

    driver.close()
