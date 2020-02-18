from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def press_button_add_to_basket(self):
        # Нажимаем кнопку Add to basket
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        # Это можно было бы сделать с помощью split() и сравнения строк,
        # Но не вижу необходимости усложнять код
        assert product_name in message, "No product name in the message"

    def should_be_message_basket_total(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price in message_basket_total, "No product price in the message"














# from .base_page import BasePage
# from .locators import ProductPageLocators
#
# class ProductPage(BasePage):
#     def should_be_add_to_basket_button(self):
#         assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is missing."
#
#     def add_to_basket(self):
#         link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
#         link.click()
#
#     def should_be_see_messages(self):
#         assert self.is_element_present(*ProductPageLocators.MESSAGES), "Messages is missing."
#
#     def is_product_name_equals(self):
#         actual = self.browser.find_elements(*ProductPageLocators.MESSAGES)[0].text
#         expected = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
#         assert actual == expected, f"Product name in the message is wrong. Expected: {expected}, but actual: {actual}."
#
#     def is_price_equals(self):
#         actual = self.browser.find_elements(*ProductPageLocators.MESSAGES)[2].text
#         expected = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
#         assert actual == expected, f"Price in the message is wrong. Expected: {expected}, but actual: {actual}."
#
#     def should_not_be_success_message(self):
#         assert self.is_not_element_present(*ProductPageLocators.MESSAGES), \
#             "Success message is presented, but should not be"
#
#     def should_message_disappeared(self):
#         assert self.is_disappeared(*ProductPageLocators.MESSAGES), \
#             "Success message should be disappeared"