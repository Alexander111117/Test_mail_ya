
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# login password yandex
#Test1233211112
#12#zxcASD

#Найдено Х писем с текстом "Simbirsoft Тестовое задание. Беликов"

#browser = webdriver.Firefox()

browser = webdriver.Chrome()
browser.get('https://ya.ru/')


mail = browser.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/div/a/div').click()
time.sleep(1)
mail1 = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[4]/a[2]').click()
time.sleep(1)

login = browser.find_element_by_id('passp-field-login')
time.sleep(1)
login.send_keys('Test1233211112')
time.sleep(1)

login = browser.find_element_by_id('passp:sign-in').click()
time.sleep(1)
login = browser.find_element_by_id('passp-field-passwd')
time.sleep(1)
login.send_keys('12#zxcASD')
time.sleep(1)
login = browser.find_element_by_id('passp:sign-in').click()
time.sleep(1)

wait = WebDriverWait(browser, 5)
mailfind = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Simbirsoft Тестовое задание. Беликов')))
mailfind1 = browser.find_elements_by_partial_link_text('Simbirsoft Тестовое задание. Беликов')
print(mailfind1)
list = len(mailfind1)
print(list)


wait = WebDriverWait(browser, 5)
elem = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,'Написать')))
elem.click()
time.sleep(1)

sendmail1 = browser.find_element_by_css_selector('.ComposeRecipients-ToField > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')
sendmail1.send_keys('Test1233211112@yandex.ru')
time.sleep(1)
action = ActionChains(browser)
action.send_keys(Keys.ENTER)
time.sleep(1)

mailsub = browser.find_element_by_xpath('/html/body/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[3]/div/div/input')
mailsub.send_keys('Simbirsoft Тестовое задание. Беликов')
time.sleep(1)
action = ActionChains(browser)
action.send_keys(Keys.ENTER)

mailcon = browser.find_element_by_xpath('/html/body/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[2]/div[1]/div/div/div')

mailcon.send_keys('Найдено ',list,' писем с темой "Simbirsoft Тестовое задание. Беликов')

mailsend = browser.find_element_by_xpath('/html/body/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/button').click()


time.sleep(1)
html = browser.find_element_by_tag_name('html')
html.send_keys('w')




