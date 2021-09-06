from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html"

driver.get(URL)
time.sleep(1)

# web elements
table = driver.find_element_by_xpath('/html/body/div/div/p[3]')
letter = driver.find_element_by_id('chr')
operation = driver.find_element_by_id('op')
number = driver.find_element_by_id('num')
calc = driver.find_element_by_id('submit')
result = driver.find_element_by_id('result')


def all_test():
    # TC01 helyes betöltődés
    # assert table.text == '!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

    # TC02 érvényes művelet
    ascii(letter.text)
    assert operation.text == "+" or "-"
    # assert number.text == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9"

    # TC03 helyes működés
    calc.click()
    # fügvénnyel megvizsgálni, először a műveleti jelet
    # utána annak függvényében hogy megfelelő irányba megfelelő karakterszámmal tolódik el a kiinduló értékhez képest az eredmény

    driver.close()
