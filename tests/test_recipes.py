import allure

from helpers.RandomHelpers import RandomHelpers


@allure.epic('Recipes')
class TestRecipes:

    @allure.title("Create new random recipe")
    def test_recipes(self, logged_user_recipes_page):
        recipes_page = logged_user_recipes_page
        create_recipe_page = recipes_page.open_new_recipe()
        recipe = RandomHelpers.get_random_recipe()
        create_recipe_page.fill_form(recipe)
        recipe_page = create_recipe_page.submit_form()
        recipe_page.assert_recipe_created(recipe)
