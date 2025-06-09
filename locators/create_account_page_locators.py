from selenium.webdriver.common.by import By


class CreateAccountPageLocators:
    FIRST_NAME = (By.XPATH, '//input[@name="first_name"]')
    LAST_NAME = (By.XPATH, '//input[@name="last_name"]')
    USERNAME  = (By.XPATH, '//input[@name="username"]')
    EMAIL  = (By.XPATH, '//input[@name="email"]')
    PASSWORD  = (By.XPATH, '//input[@name="password"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button")