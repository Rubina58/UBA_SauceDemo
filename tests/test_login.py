from selenium import webdriver
import pytest
from pages.login import LoginPage
from pages.inventory_page import InventoryPage

class TestLogin:
    def test_invalidLogin(self,driver):
        login = LoginPage(driver)
        login.login("","")
        msg = login.error_login()
        print("Invalid Login",msg)
        assert msg == "Epic sadface: Username is required"

    def test_blankUsername(self,driver):
        login = LoginPage(driver)
        login.login("","secret_sauce")
        msg = login.error_login()
        print("Invalid Login",msg)
        assert msg == "Epic sadface: Username is required"

    def test_invalidPassword(self,driver):
        login = LoginPage(driver)
        login.login("standard_user","")
        msg = login.error_login()
        assert msg == "Epic sadface: Password is required"

    def test_invalidCredential(self,driver):
        login = LoginPage(driver)
        login.login("standard","user")
        msg = login.error_login()
        assert msg == "Epic sadface: Username and password do not match any user in this service"

    def test_placeholders(self,driver):
        page = LoginPage(driver)
        assert page.get_placeholder(page.username_input) == "Username"
        assert page.get_placeholder(page.password_input) == "Password"



    def test_validLogin(self,driver):
        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")
        inventory = InventoryPage(driver)
        assert "inventory.html" in inventory.get_current_url(), "Login failed or did not redirect to inventory page"