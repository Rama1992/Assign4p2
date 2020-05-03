import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class ehb_Test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_register(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://ramaanantatmula.pythonanywhere.com/")
        login_button = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li/a').click()
        register_now = driver.find_element_by_xpath('/html/body/div/div/div/small/a').click()
        time.sleep(0.5)
        register_username = driver.find_element_by_id('id_username').send_keys("SAI")
        register_email = driver.find_element_by_id('id_email').send_keys("ranantatmula@unomaha.edu")
        register_address = driver.find_element_by_id('id_address').send_keys("cross winds")
        register_city = driver.find_element_by_id('id_city').send_keys("omaha")
        register_state = driver.find_element_by_id('id_state').send_keys("NE")
        register_zipcode = driver.find_element_by_id('id_zipcode').send_keys("68106")
        register_phone = driver.find_element_by_id('id_phone_number').send_keys("4028136004")
        register_password = driver.find_element_by_id('id_password').send_keys("test@123")
        repeat_password = driver.find_element_by_id('id_password2').send_keys("test@123")
        time.sleep(1.0)
        register = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/form/div[10]/button').click()
        time.sleep(1.0)
        try:
            hello_text = driver.find_element_by_xpath('/html/body/div/div/h1')
            assert True
        except NoSuchElementException:
            self.fail("register Failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
