import allure

@allure.epic('Login')
class TestLogin:

    @allure.title("Create account and login")
    def test_login(self, create_account_page, random_new_user):
        create_account_page.fill_create_new_account_form(random_new_user)
        login_page = create_account_page.click_create_new_account_button()
        login_page.fill_form_and_login(random_new_user)
        login_page.assert_user_logged_in()






