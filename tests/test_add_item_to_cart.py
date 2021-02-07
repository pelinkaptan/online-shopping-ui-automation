import time

import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.boutique_detail_page import BoutiqueDetail
from pages.product_details_page import ProductDetails
from helpers.config_helper import ConfigHelper
from locators.home_page_locators import HomePageLocators
from locators.boutique_detail_page_locators import BoutiqueDetailPageLocators

config = ConfigHelper().config_load()


class TestAddItemToCart(unittest.TestCase):
    # set browser from the following options: chrome or firefox
    BROWSER = 'chrome'

    def setUp(self):
        if self.BROWSER == 'chrome':
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

        elif self.BROWSER == 'firefox':
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        else:
            raise Exception('Unknown browser type')

        self.driver.maximize_window()
        self.driver.get(config['baseUrl'])
        HomePage(self.driver).wait_page_loading()
        HomePage(self.driver).close_homepage_pop_up()

    def tearDown(self):
        self.driver.close()

    def test_add_item_to_cart(self):
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        boutique_detail_page = BoutiqueDetail(self.driver)
        product_details = ProductDetails(self.driver)

        # NAVIGATE TO LOGIN PAGE
        home_page.click_element_by_locator(HomePageLocators.ACCOUNT_USER_ICON)
        home_page.wait_page_loading()

        # Assert user is on login page
        assert ('giris' in self.driver.current_url)

        # LOGIN
        login_page.login(config['testEmail'], config['testPassword'])
        time.sleep(10)
        home_page.wait_home_page_loaded()
        time.sleep(5)
        home_page.close_pop_up()
        time.sleep(5)

        # Assert user is on homepage
        assert ('/butik/liste/' in self.driver.current_url)

        # CHECK MISSING BOUTIQUE IMAGES
        missing_boutique_images = home_page.check_missing_boutique_images_in_all_categories()
        print(missing_boutique_images)

        # CLICK RANDOM BOUTIQUE
        home_page.click_random_boutique()
        # Assert user is on boutique detail page
        boutique_detail_page.wait_page_loading()
        assert ('/butikdetay' in self.driver.current_url)

        # CHECK MISSING ITEM IMAGES

        broken_item_img_urls = boutique_detail_page.check_missing_images_in_a_boutique()
        print(broken_item_img_urls)

        # Click random item on boutique detail page
        boutique_detail_page.click_random_element_by_locator(BoutiqueDetailPageLocators.PRODUCT)
        boutique_detail_page.wait_page_loading()

        # Add product to shopping cart
        product_name = product_details.add_product_to_cart()
        print("Selected item is: ", product_name)

        # Navigate to shopping cart

        time.sleep(5)
        home_page.click_element_by_locator(HomePageLocators.SHOPPING_CART_ICON)

        assert ('sepetim' in self.driver.current_url)


if __name__ == "__main__":


 unittest.main()
