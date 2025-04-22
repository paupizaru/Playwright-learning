import re
from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/add_remove_elements/"

def test_add_remove_elements(page:Page):
    page.goto(url)
    expect(page).to_have_title("The Internet")

    # Set up add_element locator and click it 3 times
    add_element = page.get_by_role("button", name="Add Element")
    add_element.click()
    add_element.click()
    add_element.click()

    # Expect to find the 3 Delete buttons
    delete_buttons = page.locator("button", has_text="Delete")
    expect(delete_buttons).to_have_count(3)

    # Delete the last one and expect to find 2
    delete_buttons.last.click()
    expect(delete_buttons).to_have_count(2)