from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_menu = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")
        self.continueShopping_button = (By.ID, "continue-shopping")
        self.checkoutInput_firstName = (By.NAME, "firstName")
        self.checkoutInput_lastName = (By.NAME, "lastName")
        self.checkoutInput_postal = (By.NAME, "postalCode")
        self.checkout_continue = (By.ID, "continue")


    def checkout(self):
        self.click(self.checkout_menu)
        cart_items = self.driver.find_elements(*self.cart_items)
        item_count = len(cart_items)

        if item_count > 0:
            self.click(self.checkout_button)
        else:
            self.click(self.continue_shopping_button)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.send_keys(self.checkoutInput_firstName, first_name)
        self.send_keys(self.checkoutInput_lastName, last_name)
        self.send_keys(self.checkoutInput_postal, postal_code)
        self.click(self.checkout_continue)