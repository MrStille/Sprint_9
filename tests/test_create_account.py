import allure

@allure.epic('Create account')
class TestCreateAccount:

    @allure.title("Create new Account")
    def test_create_new_account(self, random_new_user, create_account_page):
        create_account_page.fill_create_new_account_form(random_new_user)
        create_account_page.click_create_new_account_button()
        print(random_new_user)
