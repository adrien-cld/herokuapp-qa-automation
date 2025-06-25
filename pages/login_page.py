from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/login"

    def load(self):
        self.driver.get(self.url)

    def set_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, "radius").click()

    def get_flash_message(self):
        return self.driver.find_element(By.ID, "flash").text