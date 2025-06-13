import time
from pages.login import LoginPage
from pages.inventory_page import InventoryPage


class TestInventoryPage:
    def test_inventory_page(self,driver):
        login = LoginPage(driver)
        login.validLogin("standard_user")
        inventory = InventoryPage(driver)
        assert "inventory" in inventory.get_current_url(), "Not on inventory page"
        time.sleep(3)
        product_count = inventory.get_inventory_item_count()
        assert product_count == 6, f"Expected 6 products, but found {product_count}"
        title = inventory.get_product_title()
        assert title != "", "Product title is missing"
        product_title = "Sauce Labs Backpack"
        result = inventory.add_product_to_cart_by_title(product_title)
        time.sleep(3)
        assert result, f"Product '{product_title}' was not found or could not be added to cart"

    def test_logout(self,driver):
        login = LoginPage(driver)
        login.validLogin("standard_user")
        inventory = InventoryPage(driver)
        inventory.logout()


