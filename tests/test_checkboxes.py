from pages.checkbox_page import CheckboxPage

def test_checkboxes(driver):
    page = CheckboxPage(driver)
    page.load()

    page.check_first_box()
    page.uncheck_second_box()

    assert page.is_first_checked()
    assert not page.is_second_checked()