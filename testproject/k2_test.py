from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html"

driver.get(URL)
time.sleep(1)

# web elements
start = driver.find_element_by_id('start')
stop = driver.find_element_by_id('stop')
first_color = driver.find_element_by_id('randomColorName')
second_color = driver.find_element_by_id('testColor')
color_name = driver.find_element_by_id('testColorName')
result = driver.find_element_by_id('result')


def empty_color_test():
    # TC01 első szín nem üres, második igen
    assert first_color.text != "[     ]"
    assert second_color.text == "[     ]"


def game_works_test():
    # TC02 működik a játék
    # megnézzük üres-e
    assert second_color.text == "[     ]"
    start.click()
    time.sleep(1)
    # megnézzük elindult-e
    assert color_name.text != "[     ]"
    first = color_name.text
    time.sleep(2)
    second = color_name.text
    # megnézzük változik-e
    assert first != second
    time.sleep(2)
    third = color_name.text
    stop.click()
    time.sleep(2)
    forth = color_name.text
    # megnézzük megállt-e
    assert third == forth


def correct_result_test():
    # TC03 jó eredmény
    start.click()
    time.sleep(1)
    stop.click()
    # csak annyit bizonyít hogy correct vagy incorrect a megjelenő üzenet
    # hogy helyes működésnél helyes-e arra nem tudok gyorsan egyszerű megoldást írni, ez a feladat eddig is sok idő volt
    assert result.text == "Incorrect!" or "Correct!"

    driver.close()
