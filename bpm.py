from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard, time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import sys, os
from webdriver_manager.chrome import ChromeDriverManager


def open_webapp():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('user-data-dir=/Chrome/Profile 2/')
    #chrome_options.add_argument('load-extension=/keys')
    chrome_options.add_extension('keys/Archive.zip')
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    driver.get("https://www.easports.com/fifa/ultimate-team/web-app/")
    return driver

def open(driver,i):
    while True:
        try:
            if 'BRONZE' in driver.find_element_by_xpath('//*[@id="StoreHub"]/div[1]/div/a[5]').text:
                i+=1
                #print 'Pack #' + str(i)
                keyboard.press_and_release('b')
                break
        except TimeoutException as e:
            print 'Bronze timeout!'
        except Exception as e:
            print e
    while True:
        try:
            if 'ITEMS' in driver.find_element_by_xpath('//h2').text:
                keyboard.press_and_release('x')
                break
        except TimeoutException as e:
            print 'send to club timeout!'
        except Exception as e:
            pass
    time.sleep(2)
    try:
        if driver.find_element_by_xpath('//div[@class="name untradeable"]'):
            driver.find_element_by_xpath('/html/body/section/section/section/div[2]/section/div/section[2]/div/div/div[2]/div[2]/button[2]/span[1]').click()
            print 'Coins!'
    except NoSuchElementException as e:
        pass
    time.sleep(1)
    try:
        if driver.find_element_by_xpath('//div[@class="small player item common ut-item-loaded"]'):
            keyboard.press_and_release('t')
    except NoSuchElementException as e:
        pass
    time.sleep(1)
    keyboard.press_and_release('a')
    time.sleep(2)
    keyboard.press_and_release('backspace')

def auto_listen(driver,i):

    while True:
        open(driver,i)

if __name__ == '__main__':
    i=0
    driver = open_webapp()
    print 'waiting for a keypress'
    while True:
        if keyboard.is_pressed('space'):
            print 'space pressed, starting BPM'
            auto_listen(driver,i)
