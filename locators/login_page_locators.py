from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL  = (By.XPATH, '//input[@name="email"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, "//button")
    TITLE = (By.XPATH, "//h1[starts-with(@class,'styles_title')]")