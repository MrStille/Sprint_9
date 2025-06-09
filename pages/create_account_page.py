import time

import allure
from selenium.webdriver.common.by import By

from Data import Data
from locators.create_account_page_locators import CreateAccountPageLocators
from locators.menu_locators import MenuLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage


class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_element_visible(MenuLocators.LINK_CREATE_ACCOUNT).click()
        self.wait_element_visible(CreateAccountPageLocators.FIRST_NAME)

    @allure.step("Fill create new account form")
    def fill_create_new_account_form(self, user):
        self.wait_element_visible(CreateAccountPageLocators.FIRST_NAME).send_keys(user["first_name"])
        self.wait_element_visible(CreateAccountPageLocators.LAST_NAME).send_keys(user["last_name"])
        self.wait_element_visible(CreateAccountPageLocators.USERNAME).send_keys(user["username"])
        self.wait_element_visible(CreateAccountPageLocators.EMAIL).send_keys(user["email"])
        self.wait_element_visible(CreateAccountPageLocators.PASSWORD).send_keys(user["password"])

    @allure.step("Send filled new account form")
    def click_create_new_account_button(self):
        self.wait_element_visible(CreateAccountPageLocators.CREATE_ACCOUNT_BUTTON).click()
        self.wait_element_has_text(LoginPageLocators.TITLE, "Войти на сайт")
        return LoginPage(self.driver)


