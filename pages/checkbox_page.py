from selenium.webdriver.common.by import By

class CheckboxPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"
    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)

    def check_first_box(self):
        checkbox = self.get_checkboxes()[0]
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_second_box(self):
        checkbox = self.get_checkboxes()[1]
        if checkbox.is_selected():
            checkbox.click()

    def is_first_checked(self):
        return self.get_checkboxes()[0].is_selected()

    def is_second_checked(self):
        return self.get_checkboxes()[1].is_selected()