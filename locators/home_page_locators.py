"""Home Page Locators"""
from selenium.webdriver.common.by import By


class HomePageLocators:
    ACCOUNT_USER_ICON = (By.CSS_SELECTOR, "div[class^='link account-user']")
    SHOPPING_CART_ICON = (By.CSS_SELECTOR, "a[class^='link account-basket']")
    BOUTIQUE_CATEGORY = (By.CSS_SELECTOR, "li[class^='tab-link']")
    BOUTIQUE = (By.CSS_SELECTOR, "article[class^='component-item']")
    SLICK_LIST = (By.CSS_SELECTOR, "div[class^='slick-list']")
    NOTIFICATION_POPUP_CLOSE_BTN = (By.CLASS_NAME, "modal-close")
    FANCY_BOX = (By.CLASS_NAME, "fancybox-item.fancybox-close")
