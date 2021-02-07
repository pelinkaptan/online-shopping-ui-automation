"""Boutique Detail Page Locators"""
from selenium.webdriver.common.by import By


class BoutiqueDetailPageLocators:
    PRODUCT = (By.CSS_SELECTOR, "div[class^='boutique-product']")
