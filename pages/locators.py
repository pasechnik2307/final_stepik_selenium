from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")

    REGISTRATION_USERNAME_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

# class ProductPageLocators():
#     ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
#     PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
#     PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
#     BASKET_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
#     MESSAGES = (By.CSS_SELECTOR, "#messages strong")
#
# class BasketPageLocators():
#     EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
#     ITEMS = (By.CSS_SELECTOR, ".basket-items div.row")