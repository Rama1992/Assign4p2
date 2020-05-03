import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class ehb_Test10(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_deletepark(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://ramaanantatmula.pythonanywhere.com/")
        login_button = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li/a').click()
        time.sleep(0.5)
        username = driver.find_element_by_id('id_username').send_keys("instructor")
        password = driver.find_element_by_id('id_password').send_keys("maverick1a")
        time.sleep(1.0)
        login = driver.find_element_by_xpath('/html/body/div/div/form/div/button').click()
        time.sleep(1.0)
        event_halls = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[1]/li[2]/a').click()
        deletepark_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/a[3]')
        webdriver.ActionChains(driver).move_to_element(deletepark_button).click(deletepark_button).perform()
        confirm_delete = driver.switch_to_alert().accept()
        time.sleep(1.0)
        try:
            logout = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li/a')
            assert True
        except NoSuchElementException:
            self.fail("Update failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
