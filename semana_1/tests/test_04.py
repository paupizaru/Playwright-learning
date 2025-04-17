# Test Exercise N°4
# Checkbox toggle

import re
from playwright.sync_api import Page, expect 

url = "https://the-internet.herokuapp.com/checkboxes"

def test_checkbox_toggle(page:Page):
    page.goto(url)
    expect(page).to_have_title("The Internet") 

    # Set the locators
    checkboxes = page.get_by_role("checkbox")
    checkbox1 = checkboxes.nth(0)
    checkbox2 = checkboxes.nth(1)

    # Verify status
    expect(checkbox1).not_to_be_checked()
    expect(checkbox2).to_be_checked()

    checkbox1.check()
    checkbox2.uncheck()

    # Verify status
    expect(checkbox1).to_be_checked()
    expect(checkbox2).not_to_be_checked()