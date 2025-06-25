from pages.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login(driver):
    """Login should succeed with valid credentials."""
    login_page = LoginPage(driver)
    login_page.load()

    login_page.set_username("tomsmith")
    login_page.set_password("SuperSecretPassword!")
    login_page.click_login()

    # Wait for the success message to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    assert "You logged into a secure area!" in login_page.get_flash_message()



def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()

    login_page.set_username("invalid_user")
    login_page.set_password("invalid_pass")
    login_page.click_login()

    # Wait for the error message to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    assert "Your username is invalid!" in login_page.get_flash_message()