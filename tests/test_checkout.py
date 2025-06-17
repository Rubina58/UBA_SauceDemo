from pages.login import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
import pytest

class TestCheckout:
    @pytest.mark.regression
    def test_checkout_with_items(self,driver):
        login = LoginPage(driver)
        login.validLogin("standard_user")
        inventory = InventoryPage(driver)
        inventory.add_product_to_cart_by_title("Sauce Labs Backpack")
        inventory.add_product_to_cart_by_title("Sauce Labs Bike Light")
        checkout = CheckoutPage(driver)
        checkout.checkout()
        checkout.fill_checkout_form("Ram", "Shrestha", "123")



