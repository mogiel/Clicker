from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

# keyboard

#
# with keyboard.pressed(Key.cmd):
#     keyboard.press('s')
#     keyboard.release('s')
#
#
# sleep(1)
#
# keyboard.type('Google chrome')
# sleep(0.5)
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)
# sleep(1)
# keyboard.type('unreal3')
# sleep(1)
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)


# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
#
# browser = webdriver.Chrome()
# browser.get('http://google.com/')
#
# with keyboard.pressed(Key.cmd):
#     keyboard.press(Key.up)
#     keyboard.release(Key.up)
#
# posts_loaded = expected_conditions.presence_of_element_located((By.ID, 'L2AGLb'))
# WebDriverWait(browser, 5).until(posts_loaded)
# posts_loaded.click()

# browser.stop_client()
# sleep(2)
# browser.close()


# value1 = 3
# value2 = 4
# action = 'dodaj a + b'
#
# action_mapper = {
#     'dodaj a + b': lambda a, b: a + b,
#     'odejmij': lambda a, b: a - b,
#     'pomnóż': lambda a, b: a * b,
#     'podziel': lambda a, b: a / b,
# }
#
# print(action_mapper.get(action, 'dodaj')(value1, value2))
