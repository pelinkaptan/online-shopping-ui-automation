import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.product_details_page_locators import ProductDetailsPageLocators
from pages.base_page import BasePage


class ProductDetails(BasePage):

    def add_product_to_cart(self):
        """
        Add product to shopping cart
        :return: Product name
        """
        try:
            product_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(ProductDetailsPageLocators.PRODUCT_NAME))
            add_to_basket = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(ProductDetailsPageLocators.ADD_TO_BASKET_BUTTON))
            add_to_basket.click()
            return product_name.text
        except Exception as e:
            logging.exception("CAUGHT AN ERROR" + str(e))
