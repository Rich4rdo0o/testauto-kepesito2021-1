from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html"

driver.get(URL)
time.sleep(1)

# web elements
a_side = driver.find_element_by_id('a')
b_side = driver.find_element_by_id('b')
c_side = driver.find_element_by_id('result')
calc = driver.find_element_by_id('submit')

# test data
a = ["2", ""]
b = ["3", ""]
c = ["10", "NaN"]


def correct_load_test():
    # TC01 helyes megjelenés betöltéskor
    assert a_side.text == ""
    assert b_side.text == ""
    assert c_side.text == ""

    # betöltéskor a, b üresen jelenik meg, c nem látható


def calculator(x, y, z):
    a_side.send_keys(x)
    b_side.send_keys(y)
    calc.click()
    time.sleep(0.5)
    assert c_side.text == z


def correct_data_test():
    # TC02 kitöltés tesztadattal
    calculator(a[0], b[0], c[0])


def empty_data_test():
    # TC03 üres kitöltés
    a_side.clear()
    b_side.clear()
    calculator(a[1], b[1], c[1])

    driver.close()
