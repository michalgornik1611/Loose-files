from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import yagmail
import os

service = Service ('C:\\Users\\Lenovo\\Desktop\\chromedriv nowa wersja\\chromedriver.exe')
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument ('disable-infobars')
    options.add_argument('start-maximazed')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://stooq.pl/')
    return driver

def clean_text(text):
    output = float (text[:-1])
    return output

def send_mail():
    sender = os.getenv('email_sender')
    receiver = os.getenv('email_sender')
    subject = 'WIG20 wzrósł o 1%'
    contents = 'Indeks WIG20 wzrósł właśnie o ponad 1.00%'
    yag = yagmail.SMTP(user=sender, password=os.getenv('password'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print ('Email Sent!')

def main():
    driver=get_driver()
    time.sleep(1)
    element = driver.find_element(by = 'xpath', value = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table[6]/tbody/tr/td[1]/table/tbody/tr[2]/td[1]/table/tbody/tr/td[2]/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[3]/span')
    text = str(clean_text(element.text))

    if (float(text) > 1.00):
        send_email(str(text))

main()
