import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class ehb_Test9(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_editpark(self):

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
        editpark_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/div/a[2]')
        webdriver.ActionChains(driver).move_to_element(editpark_button).click(editpark_button).perform()
        park_name = driver.find_element_by_id('id_name').send_keys(" India")
        time.sleep(1.0)
        update_button = driver.find_element_by_xpath('/html/body/div/form/button').click()
        try:
            logout = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li/a')
            assert True
        except NoSuchElementException:
            self.fail("edit park failed")
            assert False

def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()
