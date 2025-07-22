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
