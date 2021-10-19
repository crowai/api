import requests

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import time

API_URL = "http://localhost:5000/api/v1/sentiments"

class Bot(object):
  def __init__(self):
    self.caps = DesiredCapabilities().FIREFOX
    self.caps["pageLoadStrategy"] = "eager"
    self.driver = webdriver.Firefox(desired_capabilities=self.caps)

    self.running = True

  def run(self):
    pass

  def scrapeStockTwits(self):
    URL = "https://stocktwits.com/symbol/BTC.X"
    self.driver.get(URL)
    time.sleep(1)
    self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/div/div/div[1]/div[2]/div/div/div[1]/div[2]")\
      .click()

    sentimentContainer = self.driver.find_element_by_class_name("infinite-scroll-component")
    sentimentCount = len(sentimentContainer.find_elements_by_xpath("./div"))

    while self.running:
      sentiments = sentimentContainer.find_elements_by_xpath("./div")
      
      if len(sentimentContainer.find_elements_by_xpath("./div")) > sentimentCount:
        for i in range(len(sentimentContainer.find_elements_by_xpath("./div")) - sentimentCount):
          try:
            movement = sentiments[i].find_element_by_xpath(f"/html/body/div[3]/div/div/div[3]/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div/div[{ i+1 }]/div/div/article/div/div[2]/div[1]/span[1]/span/a").text
          except NoSuchElementException:
            pass

          author = sentiments[i].find_element_by_xpath(f"/html/body/div[3]/div/div/div[3]/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div/div[{ i+1 }]/div/div/article/div/div[2]/div[1]/span[1]/span/a/span").text
          content = sentiments[i].find_element_by_xpath(f"/html/body/div[3]/div/div/div[3]/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div/div[{ i+1 }]/div/div/article/div/div[2]/div[2]/div/div/div").text

          r = requests.post(API_URL, data = {
            "content": content,
            "author": author,
            "source": URL
          })
          if r.status_code != 201:
            print("Sentiment POST failed.")
          else:
            print("Successfully POSTED new sentiment.")

      sentimentCount = len(sentimentContainer.find_elements_by_xpath("./div"))

      time.sleep(5)