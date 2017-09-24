
from selenium import webdriver
import os
import time

phantomjs_path = os.path.abspath("G:\phantomjs\\bin\phantomjs.exe")

class Web_Scraper():

    def get_html_one(self, BASE_URL):
        driver = webdriver.PhantomJS(executable_path=phantomjs_path)
        driver.set_window_size(1400, 1000)
        driver.get(BASE_URL)
        html = driver.page_source
        return html

    def get_html_topic(self, BASE_URL):
        driver = webdriver.PhantomJS(executable_path=phantomjs_path)
        driver.set_window_size(1400, 1000)
        driver.get(BASE_URL)
        SCROLL_PAUSE_TIME = 3

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        html = driver.page_source
        return html

url = "https://www.justdial.com/Ahmedabad/stock-broking"

Web = Web_Scraper()
html = Web.get_html_topic(url)

f=open('1.txt','w', encoding="utf-8")
f.write(html)
