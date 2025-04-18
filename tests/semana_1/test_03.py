# Test Exercise N°3
# Click a button and then assert that there is a visible text.

import re
from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/add_remove_elements/"

def test_click_and_assert_text(page: Page):
    page.goto(url)

    expect(page).to_have_title(re.compile("The Internet"))
    
    # Set locator and verify 'Add Element' button is visible
    add_locator = page.get_by_role("button", name="Add Element")
    expect(add_locator).to_be_visible()

    # Click 'Add Element' and verify 'Delete' appears
    add_locator.click()

    # Set locator and verify 'Delete' button is visible
    delete_locator = page.get_by_role("button", name="Delete")
    expect(delete_locator).to_be_visible()

    # Click 'Delete' and verify 'Delete' dissappears
    delete_locator.click()
    expect(delete_locator).not_to_be_visible()
    expect(delete_locator).to_have_count(0)  