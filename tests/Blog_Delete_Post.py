import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Blog_ATS(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()

  def test_blog(self):
    user = "instructor"
    pwd = "instructor1a"
    driver = self.driver
    driver.maximize_window()
    driver.get("http://127.0.0.1:8000/admin")
    elem = driver.find_element_by_id("id_username")
    elem.send_keys(user)
    elem = driver.find_element_by_id("id_password")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    driver.get("http://127.0.0.1:8000")
    assert "Logged In"
    time.sleep(2)
    elem = driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
    time.sleep(2)
    elem = driver.find_element_by_id("id_title")
    elem.send_keys("This test post will get deleted by selenium")
    elem = driver.find_element_by_id("id_text")
    elem.send_keys("This is a test post of text with selenium that will then get deleted by selenium.")
    time.sleep(2)
    elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
    time.sleep(2)
    assert "Posted Blog Entry"
    driver.get("http://127.0.0.1:8000")
    time.sleep(2)
    driver.get("http://127.0.0.1:8000/admin")
    time.sleep(2)
    elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/th/a").click()
    time.sleep(2)
    elem = Select(driver.find_element_by_xpath('/html/body/div/div[3]/div/div/form/div[1]/label/select'))
    time.sleep(2)
    elem.select_by_index(1)
    time.sleep(2)
    elem = driver.find_element_by_xpath('//*[@id="action-toggle"]').click()
    time.sleep(2)
    elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button").click()
    time.sleep(2)
    elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[4]")
    elem.send_keys(Keys.RETURN)
    time.sleep(4)
    assert "Deleted All Blog Entries"
    driver.get("http://127.0.0.1:8000")
    time.sleep(3)

  def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
  unittest.main()
