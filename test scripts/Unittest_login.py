import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ehb_Test2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://ramaanantatmula.pythonanywhere.com/")
        login_button = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li/a').click()
        time.sleep(0.5)
        username = driver.find_element_by_id('id_username').send_keys("rama")
        password = driver.find_element_by_id('id_password').send_keys("test@123")
        time.sleep(1.0)
        login = driver.find_element_by_xpath('/html/body/div/div/form/div/button').click()
        time.sleep(1.0)
        try:
            logout = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li/a')
            assert True
        except NoSuchElementException:
            self.fail("Login Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
