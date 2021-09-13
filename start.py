from selenium import webdriver
import entermail
import findsend

# yandex mail
# login: Test1233211112
# password: 12#zxcASD1


browser = webdriver.Chrome()
#browser = webdriver.Firefox()
browser.get('https://ya.ru/')

entermail.entermail(browser)

findsend.findelm(browser)

#browser.quit()

