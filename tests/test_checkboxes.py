from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

def test_checkboxes(driver):
    print("Opening the checkboxes page...")
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    print("Locating checkbox elements...")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    print(f"Found {len(checkboxes)} checkboxes.")
    assert len(checkboxes) == 2

    print("Unchecking the second checkbox if it is checked...")
    if checkboxes[1].is_selected():
        checkboxes[1].click()
    assert not checkboxes[1].is_selected()
    print("Second checkbox is now unchecked")

    print("Checking the first checkbox if it is not checked...")
    if not checkboxes[0].is_selected():
        checkboxes[0].click()
    assert checkboxes[0].is_selected()
    print("First checkbox is now checked")


def test_checkboxes_invalid_state(driver):
    print("Opening the checkboxes page...")
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    print("Locating checkbox elements...")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    print(f"Found {len(checkboxes)} checkboxes.")
    assert len(checkboxes) == 2

    print("Asserting incorrect checkbox states intentionally...")
    print("This test is designed to fail: we wrongly assume both checkboxes are unchecked.")

    is_checked_0 = checkboxes[0].is_selected()
    is_checked_1 = checkboxes[1].is_selected()
    print(f"Checkbox 0 selected: {is_checked_0}")
    print(f"Checkbox 1 selected: {is_checked_1}")

    assert not is_checked_0, "Expected checkbox 0 to be unchecked"
    assert not is_checked_1, "Expected checkbox 1 to be unchecked"