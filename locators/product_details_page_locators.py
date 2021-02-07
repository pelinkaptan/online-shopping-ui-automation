"""Product Details Page Locators"""
from selenium.webdriver.common.by import By


class ProductDetailsPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'add-to-bs-tx')
    BASKET_ITEM_COUNT = (By.CLASS_NAME, 'basket-item-count')
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1[class^='pr-new-br']")
