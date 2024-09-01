from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime
import time

service = Service(r"C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service)
def login_again(webname):
    #8link
    if webname == '8link':
        try:
            driver.get("https://8link.io/login")
            time.sleep(1)
            username_field = driver.find_element('id','email')
            username_field.send_keys('nhatkiemxuyenmu@gmail.com')
            password_field = driver.find_element('id','inputPassword5')
            password_field.send_keys('pipipop0')
            checkbox = driver.find_element(By.ID, 'myCheckbox')
            if not checkbox.is_selected():
                checkbox.click()
            password_field.send_keys(Keys.ENTER)
        except:
            print('web 8link dang nhap loi')
    #yeumoney
    if webname == 'yeumoney':
        try:
            driver.get("https://yeumoney.com/auth/signin.php")
            time.sleep(1)
            username_field = driver.find_element('id','email')
            username_field.send_keys('nhatkiemxuyenmu@gmail.com')
            password_field = driver.find_element('id','matkhau')
            password_field.send_keys('pipipop0')
            password_field.send_keys(Keys.ENTER)
        except:
            print('web yeumoney dang nhap loi')
    #1short
    if webname == '1short':
        try:
            driver.get("https://1short.io/auth/login")
            time.sleep(1)
            username_field = driver.find_element('id','login-email')
            username_field.send_keys('vuotlinktele@gmail.com')
            password_field = driver.find_element('id','login-password')
            password_field.send_keys('pipipop0')
            password_field.send_keys(Keys.ENTER)
        except:
            print('web 1short dang nhap loi')
    #uptolink.cloud 
    if webname == 'uptolink.cloud':
        try:
            driver.get("https://uptolink.cloud/auth/signin")
            time.sleep(1)
            username_field = driver.find_element('id','username')
            username_field.send_keys('vuotlinktele@gmail.com')
            password_field = driver.find_element('id','password')
            password_field.send_keys('pipipop0')
            password_field.send_keys(Keys.ENTER)
        except:
            print('web uptolink.cloud dang nhap loi')

def check_link(link):
    if '8link' in link:
        link = link.replace("https://8link", "")
        link = link.replace(".io/", "")
        link = link.replace(".vip/", "")
        link = link.replace(".pro/", "")
        link = link.replace(".one/", "")
        link = link.replace(".app/", "")
        link = link.replace(".click/", "")
        link = 'https://partner.8link.io/shortened-url/'+link
        driver.get(link)
        time.sleep(1)
        view = driver.find_elements(By.CSS_SELECTOR,'p.mb-2')
        return str(view[2].text)
    if 'yeumoney' in link:
        link = link.replace("https://yeumoney.com/","")
        link = 'https://yeumoney.com/quangly/?thongke_link='+link
        driver.get(link)
        time.sleep(1)
        view = driver.find_element(By.CSS_SELECTOR,'.text-right.text-success')
        return str(view.text)
    if '1short' in link:
        driver.get('https://1short.io/client/dashboard')
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source,'html.parser')
        soup = soup.find_all('h2',class_='font-weight-bolder')[1]
        return str(soup.text)
    if 'uptolink.cloud' in link:
        driver.get('https://uptolink.cloud/member/dashboard')
        time.sleep(1)
        view = driver.find_elements(By.CSS_SELECTOR,'tr')[int(datetime.now().strftime("%d"))]
        view = view.text.split(" ")
        return str(view[1])
    if 'uptolink.io' in link:
        driver.get('https://uptolink.io.vn/member/dashboard')
        time.sleep(1)
        view = driver.find_elements(By.CSS_SELECTOR,'tr')[int(datetime.now().strftime("%d"))]
        view = view.text.split(" ")
        return str(view[1])
    return '0'

