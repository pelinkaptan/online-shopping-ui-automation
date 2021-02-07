import logging

from locators.shopping_cart_page_locators import ShoppingCartPageLocators
from pages.base_page import BasePage


class ShoppingCart(BasePage):

    def get_item_titles_in_shopping_cart(self):
        """
        Gets item titles in shopping cart
        :return: item titles in shopping cart
        """
        try:
            all_item_titles = self.driver.find_elements(*ShoppingCartPageLocators.ITEM_TITLE)
            item_titles = [item_title for item_title in all_item_titles][0]

            return item_titles

        except Exception as e:
            logging.exception("CAUGHT AN ERROR" + str(e))
