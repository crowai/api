from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Bot(object):
  def __init__(self):
    self.driver = webdriver.Firefox()

  def run(self):
    self.driver.get("")