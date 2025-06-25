# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Setup: start browser
    driver = webdriver.Firefox()

    yield driver  # Provide the driver to the test

    # Teardown: close browser
    driver.quit()