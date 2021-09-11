from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By


def findelm (browser):
    wait = WebDriverWait(browser, 10)

    mailfind1 = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Simbirsoft Тестовое задание. Беликов')))
    mailfind1 = browser.find_elements_by_partial_link_text('Simbirsoft Тестовое задание. Беликов')
    print(mailfind1)
    list = len(mailfind1)
    print(list)

    elem = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Написать'))).click()

    sendmail = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ComposeRecipients-ToField > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')))
    sendmail.send_keys('Test1233211112@yandex.ru')

    mailsub = browser.find_element_by_xpath('/html/body/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[3]/div/div/input').send_keys('Simbirsoft Тестовое задание. Беликов')
    mailcon = browser.find_element_by_xpath(
        '/html/body/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div[2]/div[1]/div/div/div')
    mailcon.send_keys('Найдено ', list, ' писем с темой "Simbirsoft Тестовое задание. Беликов')

    mailsend = browser.find_element_by_xpath(
        '/html/body/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/button').click()

    pass