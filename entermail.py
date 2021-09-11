from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By


def entermail (browser):

    wait = WebDriverWait(browser, 5)

    mail = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/table/tbody/tr[1]/td/div/a/div'))).click()
    mail = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[2]/div/div/div[4]/a[2]'))).click()

    login = wait.until(EC.element_to_be_clickable((By.ID, 'passp-field-login')))
    login.send_keys('Test1233211112')
    login = wait.until(EC.element_to_be_clickable((By.ID, 'passp:sign-in'))).click()

    password = wait.until(EC.element_to_be_clickable((By.ID, 'passp-field-passwd')))
    password.send_keys('12#zxcASD1')
    password = wait.until(EC.element_to_be_clickable((By.ID, 'passp:sign-in'))).click()

    pass

