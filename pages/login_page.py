import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    email_id = "user-name"
    password_id = "password"
    login_button_id = "login-button"
    app_logo_text = ".app_logo"

    def __init__(self, driver):
        self.driver = driver


    def enter_login_creds(self,email,password):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, self.login_button_id).click()





