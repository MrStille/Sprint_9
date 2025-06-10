import allure

from locators.login_page_locators import LoginPageLocators
from locators.menu_locators import MenuLocators
from pages.base_page import BasePage
from pages.recipes_page import RecipesPage


class LoginPage(BasePage):

    @allure.step("Fill login form")
    def fill_form_and_login(self, user) :
        self.wait_element_visible(LoginPageLocators.EMAIL).send_keys(user["email"])
        self.wait_element_visible(LoginPageLocators.PASSWORD).send_keys(user["password"])
        self.wait_element_visible(LoginPageLocators.LOGIN_BUTTON).click()
    @allure.step("Assert user logged in")
    def assert_user_logged_in(self):
        self.wait_element_visible(MenuLocators.LINK_LOGOUT)
        url = self.driver.current_url
        assert url == 'https://foodgram-frontend-1.prakticum-team.ru/recipes'
        return RecipesPage(self.driver)

