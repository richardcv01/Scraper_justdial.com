
from selenium import webdriver
import os


phantomjs_path = os.path.abspath("G:\phantomjs\\bin\phantomjs.exe")

class Web_Scraper():

    def get_html(self, BASE_URL):
        driver = webdriver.PhantomJS(executable_path=phantomjs_path)
        driver.set_window_size(1400, 1000)
        driver.get(BASE_URL)
        html = driver.page_source
        return html

url = "https://www.justdial.com/Ahmedabad/Stock-Broking-Maninagar/079PXX79-XX79-170321181502-P4W1_BZDET?xid=QWhtZWRhYmFkIHN0b2NrIGJyb2tpbmc="


