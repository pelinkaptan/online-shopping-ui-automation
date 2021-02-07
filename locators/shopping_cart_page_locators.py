"""Shopping Cart Page Locators"""
from selenium.webdriver.common.by import By


class ShoppingCartPageLocators:
    ITEM_TITLE = (By.CSS_SELECTOR, "p[class^='pb-item']")
