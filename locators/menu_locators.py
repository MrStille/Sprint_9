from selenium.webdriver.common.by import By


class MenuLocators:
    LINK_CREATE_ACCOUNT = (By.XPATH, "//a[@href='/signup']")
    LINK_LOGIN = (By.XPATH, "//a[@href='/signin']")
    LINK_LOGOUT = (By.XPATH, "//a[text()='Выход']")

    """For logged in users"""
    LINK_CREATE_RECIPE = (By.XPATH, "//a[@href='/recipes/create']")
    
