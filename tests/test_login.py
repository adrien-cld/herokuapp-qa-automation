from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login(driver):
    """Login should succeed with valid credentials."""
    print("Starting test: valid login")
    login_page = LoginPage(driver)

    print("Loading login page...")
    login_page.load()

    print("Entering valid username and password...")
    login_page.set_username("tomsmith")
    login_page.set_password("SuperSecretPassword!")

    print("Clicking login button...")
    login_page.click_login()

    print("Waiting for success message...")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    message = login_page.get_flash_message()
    print(f"Success message received: {message}")
    assert "You logged into a secure area!" in message


def test_invalid_login(driver):
    print("Starting test: invalid login")
    login_page = LoginPage(driver)

    print("Loading login page...")
    login_page.load()

    print("Entering invalid username and password...")
    login_page.set_username("invalid_user")
    login_page.set_password("invalid_pass")

    print("Clicking login button...")
    login_page.click_login()

    print("Waiting for error message...")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    message = login_page.get_flash_message()
    print(f"Error message received: {message}")
    assert "Your username is invalid!" in message