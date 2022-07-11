from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import signal
import os
from time import sleep

options = Options()
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(r'C:\Users\user\Downloads\クレイピング入門\chromedriver3.exe',options=options)

try:
    year = '2022'
    month = '7' #int(input('予約する月は？'))

    yeardic = {'2022': 1158,'2023': 1160,'2024':1172}
    monthid = str(int(month) + int(yeardic[year]))
    browser.get("https://scs.cl.sophia.ac.jp/campusweb/campussmart.do?locale=ja_JP")
    sleep(1)
    elem_name = browser.find_element_by_name('userName')
    elem_name.send_keys('A2078***')
    elem_pw = browser.find_element_by_name('password')
    elem_pw.send_keys('*****')
    elem_login = browser.find_element_by_class_name('ui-button')
    elem_login.click()
    sleep(1)
    elem_dl = browser.find_element_by_id('tab-dc')
    elem_dl.click()
    sleep(1)

    elem_dl = browser.find_element_by_xpath('//*[@id="menulist"]/li[2]/div')
    elem_dl.click()
    sleep(3)


    
    # テーブル内容取得
    tableElem = browser.find_element_by_id("fileTable"+ monthid)
    trs = tableElem.find_elements(By.TAG_NAME, "tr")
    leng = [2,3]
    for i in range(1,len(trs)):
        tds = trs[i].find_elements(By.TAG_NAME, "td")
        text = tds[1].get_attribute("textContent")
        if '使用可能' in text or '教室' in text:
            url = str(tds[1].find_element(By.TAG_NAME, "a").get_attribute("href"))
            browser.get(url)
        else:
            continue
    sleep(5)

finally:
    os.kill(browser.service.process.pid,signal.SIGTERM)