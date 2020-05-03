import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class ehb_Test7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_editbooking(self):

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
        booking_edit = driver.find_element_by_xpath('/html/body/div/table/tbody[1]/tr/td[3]/a').click()
        select_month = Select(driver.find_element_by_id('id_booked_on_date_month'))
        (select_month).select_by_visible_text('December')
        update_button = driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()
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
