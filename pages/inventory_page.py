from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.productTitle = (By.CLASS_NAME, "inventory_item_name")
        self.productRow =(By.CLASS_NAME, "inventory_item")
        self.menuButton = (By.ID, "react-burger-menu-btn")
        self.logoutButton = (By.ID, "logout_sidebar_link")

    def get_current_url(self):
        return self.driver.current_url

    def get_product_title(self):
        return self.driver.find_element(*self.productTitle).text

    def get_inventory_item_count(self):
        return len(self.driver.find_elements(*self.productRow))

    def add_product_to_cart_by_title(self, product_title):

        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in products:

            title = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if title == product_title:
                add_button = product.find_element(By.CSS_SELECTOR, "button.btn_inventory")
                add_button.click()
                return True
        return False

    def logout(self):
        self.click(self.menuButton)
        self.click(self.logoutButton)
