import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

API_URL = "http://localhost:5000/api/v1/"

class Bot(object):
  def __init__(self):
    self.driver = webdriver.Firefox()

  def run(self):
    pass

  def scrapeStockTwits(self):
    URL = "https://stocktwits.com/symbol/BTC.X"
    self.driver.get(URL)
    time.sleep(2)
    self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/div/div/div[1]/div[2]/div/div/div[1]/div[2]")\
      .click()

    requests.post(API_URL, content="", author="")