import pytest
import os
import sys
sys.path.append(os.getcwd())
from selenium import webdriver
from selenium.webdriver import ChromeOptions

from Data import Data
from helpers.RandomHelpers import RandomHelpers
from pages.create_account_page import CreateAccountPage


@pytest.fixture(scope='function')
def random_new_user():
    return {
        "first_name": "T" + RandomHelpers.generate_random_string(14),
        "last_name": "B" + RandomHelpers.generate_random_string(14),
        "username": "user" + RandomHelpers.generate_random_string(14),
        "email": RandomHelpers.get_email(),
        "password": Data.COMMON_PASSWORD,
    }

@pytest.fixture
def driver():
    options = ChromeOptions()
    driver = webdriver.Remote(
        command_executor="https://selenoid:4444/wd/hub",
        options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def driver_chrome():
    driver = webdriver.Chrome()
    driver.get(Data.SITE_URL)
    yield driver
    driver.quit()

@pytest.fixture()
def create_account_page(driver):
    return CreateAccountPage(driver)


@pytest.fixture(scope='function')
def logged_user_recipes_page(create_account_page):
    user = {
        "first_name": "T" + RandomHelpers.generate_random_string(14),
        "last_name": "B" + RandomHelpers.generate_random_string(14),
        "username": "user" + RandomHelpers.generate_random_string(14),
        "email": RandomHelpers.get_email(),
        "password": Data.COMMON_PASSWORD,
    }
    create_account_page.fill_create_new_account_form(user)
    login_page = create_account_page.click_create_new_account_button()
    login_page.fill_form_and_login(user)
    recipes_page = login_page.assert_user_logged_in()
    return recipes_page
