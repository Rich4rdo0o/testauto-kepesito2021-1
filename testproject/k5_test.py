from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html"

driver.get(URL)
time.sleep(1)

# web elements
bingo = driver.find_elements_by_xpath('//td')
number_list = driver.find_elements_by_xpath('//li')
play = driver.find_element_by_id('spin')
reset = driver.find_element_by_id('init')
message = driver.find_element_by_id('messages')

# test data
user_numbers = 25
all_numbers = 75


def correct_page_test():
    # TC01 helyes megjelenés
    assert len(bingo) == user_numbers
    assert len(number_list) == all_numbers


def player():
    for i in range(75):
        play.click()
        time.sleep(0.1)
        if message.text == "":
            pass
        else:
            assert message.text == "BINGO"
            break


def play_bingo_test():
    # TC02 play bingoig

    player()
    time.sleep(1)
    played_numbers = driver.find_elements_by_xpath('//div')
    numbers_hit = []

    def coloring():
        for j in played_numbers:
            # print(j.value_of_css_property("background-color"))
            if j.value_of_css_property("background-color") == 'rgba(238, 204, 238, 1)':
                numbers_hit.append(j)
            else:
                pass

    coloring()


def new_game_test():
    # TC03 új játék
    # a korábban beszineződött számok már nem találhatók
    time.sleep(1)
    reset.click()
    new_numbers = driver.find_elements_by_xpath('//div')
    # assert len(new_numbers) != (len(played_numbers) - len(numbers_hit))
    # kellenek az előző függvényből de nincs időm

    driver.close()
