from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_USERNAME_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")

    REGISTRATION_USERNAME_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    MESSAGES = (By.CSS_SELECTOR, "#messages strong")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    ITEMS = (By.CSS_SELECTOR, ".basket-items div.row")