import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class ehb_Test8(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_deltebooking(self):

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
        booking_details = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[1]/li[3]/a').click()
        booking_delete = driver.find_element_by_xpath('/html/body/div/table/tbody[5]/tr/td[4]/a').click()
        confirm_delete = driver.switch_to_alert().accept()
        time.sleep(1.0)
        try:
            booking_details = driver.find_element_by_xpath('/html/body/div/h3')
            assert True
        except NoSuchElementException:
            self.fail("Update failed")
            assert False

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
