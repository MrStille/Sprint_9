import allure

from locators.create_recipe_locators import CreateRecipeLocators
from locators.menu_locators import MenuLocators
from locators.recipes_page_locators import RecipesPageLocators
from pages.base_page import BasePage
from pages.create_recipe_page import CreateRecipePage


class RecipesPage(BasePage):

    @allure.step("Click new recipe button")
    def open_new_recipe(self):
        self.wait_element_visible(MenuLocators.LINK_CREATE_RECIPE).click()
        return CreateRecipePage(self.driver)
