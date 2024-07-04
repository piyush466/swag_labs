import time

from selenium.webdriver.common.by import By

from pages.login_page import Login
from selenium import webdriver

class Test_login:
    app_logo_text = ".app_logo"


    def test_user_login(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.login = Login(self.driver)
        self.login.enter_login_creds("standard_user", "secret_sauce")
        self.login.click_login_button()
        time.sleep(2)
        self.logo_text = self.driver.find_element(By.CSS_SELECTOR, self.app_logo_text)
        assert self.logo_text.text == "Swag Labs",  "Login Unsucessful"