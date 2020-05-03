import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class ehb_Test3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_hallbooking(self):

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
        event_halls = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[1]/li[2]/a').click()
        viewdetails_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/a')
        webdriver.ActionChains(driver).move_to_element(viewdetails_button).click(viewdetails_button).perform()
        book_button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/a')
        webdriver.ActionChains(driver).move_to_element(book_button).click(book_button).perform()
        select_month = Select(driver.find_element_by_id('id_booked_on_date_month'))
        (select_month).select_by_visible_text('May')
        select_date = Select(driver.find_element_by_id('id_booked_on_date_day'))
        (select_date).select_by_visible_text('10')
        select_year = Select(driver.find_element_by_id('id_booked_on_date_year'))
        (select_year).select_by_visible_text('2020')
        time.sleep(1.0)
        reserve_button = driver.find_element_by_xpath('/html/body/div/div/div/form/button').click()
        try:
            booking_details = driver.find_element_by_xpath('/html/body/div/h3')
            assert True
        except NoSuchElementException:
            self.fail("reservation failed")
            assert False

def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()
