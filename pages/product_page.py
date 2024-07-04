import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Products:

    all_products = "inventory_item_name"
    all_product_price = "inventory_item_price"
    product_sort_container = "product_sort_container"

    def __init__(self, driver):
        self.driver = driver

    def get_all_product_name_from_A_to_Z(self):
        time.sleep(2)
        self.products_names = self.driver.find_elements(By.CLASS_NAME, self.all_products)
        self.products_price = self.driver.find_elements(By.CLASS_NAME, self.all_product_price)
        print("********ALL A to Z PRODUCTS***********")
        for self.product,self.price in zip(self.products_names, self.products_price):
            print("product names and price:",self.product.text, self.price.text)

    def handle_drop_down(self,visible_text_of_drop_down):
        self.drop_down = self.driver.find_element(By.CLASS_NAME, self.product_sort_container)
        select = Select(self.drop_down)
        select.select_by_visible_text(visible_text_of_drop_down)

    def get_all_products_name_and_price_Z_to_A(self):
        self.products_names = self.driver.find_elements(By.CLASS_NAME, self.all_products)
        self.products_price = self.driver.find_elements(By.CLASS_NAME, self.all_product_price)
        print("********ALL Z to A PRODUCTS***********")
        for self.product, self.price in zip(self.products_names, self.products_price):
            print("product names and price:", self.product.text, self.price.text)


    def get_all_products_name_and_price_low_to_high(self):
        self.products_names = self.driver.find_elements(By.CLASS_NAME, self.all_products)
        self.products_price = self.driver.find_elements(By.CLASS_NAME, self.all_product_price)
        print("********ALL Low to High PRODUCTS***********")
        for self.product, self.price in zip(self.products_names, self.products_price):
            print("product names and price:", self.product.text, self.price.text)

    def get_all_products_name_and_price_high_to_low(self):
        self.products_names = self.driver.find_elements(By.CLASS_NAME, self.all_products)
        self.products_price = self.driver.find_elements(By.CLASS_NAME, self.all_product_price)
        print("********ALL  High to Low PRODUCTS***********")
        for self.product, self.price in zip(self.products_names, self.products_price):
            print("product names and price:", self.product.text, self.price.text)



