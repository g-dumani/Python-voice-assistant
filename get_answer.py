import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import io
import re


options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('start-maximized') #
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Webdriver\chromedriver.exe')
driver.get("http://google.com/")


class Fetcher:
    def __init__(self, url):
        self.driver = webdriver.PhantomJS(executable_path="C:\\phantomjs-2.1.1-windows\\bin\\phantomjs")
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url
        print(self.url)


    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "gsfi")
            ))
        except:
            ("Failed, bro")

        soup = BeautifulSoup(self.driver.page_source, "lxml")
        answer = soup.find(class_="g")
        answer = driver.execute_script(
                "return document.elementFromPoint(arguments[0], arguments[1]);",
                350, 230).text
        #answer= soup.find_all(re.compile("^g"))

        #answer=soup.find(class_="Z0LcW")
        print(answer)






        #with open("test.html", "w+",encoding="utf-8") as f:
        #     f.write(str(soup.prettify()))


        #if not answer:
        #    answer = soup.find(class_="_m3b")


        #if not answer:
        #    answer = "I don't know."

        self.driver.quit()

        return answer
