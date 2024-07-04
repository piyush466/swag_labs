import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

from pages.product_page import Products
from test_cases.test_verify_login import Test_login
from test_cases import test_data

class Test_products:

    def test_get_products_name(self,setup):
        self.driver = setup
        Test_login().test_user_login(self.driver)
        self.products = Products(self.driver)
        self.products.get_all_product_name_from_A_to_Z()
        self.products.handle_drop_down(test_data.select_z_to_a)
        self.products.get_all_products_name_and_price_Z_to_A()
        self.products.handle_drop_down(test_data.select_low_to_high)
        self.products.get_all_products_name_and_price_low_to_high()
        self.products.handle_drop_down(test_data.select_high_to_low)
        self.products.get_all_products_name_and_price_high_to_low()





