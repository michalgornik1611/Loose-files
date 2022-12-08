from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests

service = Service ('C:\\Users\\Lenovo\\Desktop\\chromedriv nowa wersja\\chromedriver.exe')
def get_driver():
    #Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument ('disable-infobars')
    options.add_argument('start-maximazed')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    nazwa = input("Podaj nazwę spółki: ")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(f'https://www.google.com/search?q={nazwa}&tbm=nws&sxsrf=ALiCzsYII8NyFN40IwvuS1-vTsJiVfXhWg:1664280787385&source=lnt&tbs=sbd:1&sa=X&ved=2ahUKEwjTyo2J-bT6AhXssIsKHSALB8UQpwV6BAgBECY&biw=1920&bih=969&dpr=1')


    return driver

print(get_driver())



