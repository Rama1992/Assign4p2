import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class ehb_Test6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addpark(self):

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
        addpark_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/div/div/a/img')
        webdriver.ActionChains(driver).move_to_element(addpark_button).click(addpark_button).perform()
        park_name = driver.find_element_by_id('id_name').send_keys("Rajahmundry hall")
        park_state = driver.find_element_by_id('id_state').send_keys("AP")
        park_city = driver.find_element_by_id('id_city').send_keys("Rajahmundry")
        park_capacity = driver.find_element_by_id('id_capacity').send_keys("100")
        park_image = driver.find_element_by_id('id_image').send_keys("https://seemymarriage.com/wp-content/uploads/2016/07/5-0cc644ef-6ffb-47a0-9cb9-a3579647fa64.png")
        park_description = driver.find_element_by_id('id_description').send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vestibulum hendrerit est aliquam ornare. Quisque quis congue nunc. Duis viverra vel nisi nec efficitur. Quisque in est eros. Donec maximus tellus at semper suscipit. Ut eu lorem eleifend, consectetur turpis eu, efficitur urna. Suspendisse eget laoreet mi. Vestibulum magna lorem, imperdiet ut posuere quis, rhoncus sit amet lectus. Maecenas cursus magna eu massa rutrum gravida. Curabitur eget ex non odio scelerisque mollis. Vivamus at nisi sagittis, maximus lacus ac, placerat diam. Suspendisse pellentesque faucibus augue, id feugiat nisl dignissim vel. Cras efficitur, diam in vulputate commodo, ex magna convallis justo, sed elementum enim ex quis mi. Aenean vel metus dolor. Nullam in venenatis magna.  Etiam dolor diam, tempus a varius nec, interdum at erat. Integer suscipit eros diam, fermentum bibendum lectus laoreet nec. Donec neque libero, commodo vitae suscipit eu, dapibus in tortor. Donec volutpat pulvinar ante sed dignissim. Vivamus nisi nulla, pulvinar et malesuada sed, vehicula quis dui. Donec eleifend elit ipsum, et pellentesque mi gravida non. Fusce at lorem tincidunt, elementum libero non, hendrerit justo. Fusce non purus viverra, semper lacus in, rhoncus ex. Aenean molestie viverra diam non blandit. Ut ac varius orci. Curabitur pellentesque risus non ex tincidunt, vel feugiat neque consequat. Curabitur diam nunc, dictum at nulla et, sollicitudin aliquam nulla. Morbi pharetra neque nec rhoncus tempus. Integer egestas odio metus, pretium iaculis diam laoreet vel.")
        park_phone = driver.find_element_by_id('id_phone_number').send_keys("4028136004")
        time.sleep(1.0)
        save_button = driver.find_element_by_xpath('/html/body/div/form/button').click()
        try:
            home = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[1]/li[1]/a')
            assert True
        except NoSuchElementException:
            self.fail("Add park failed")
            assert False

def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()
