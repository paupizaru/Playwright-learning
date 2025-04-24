import re 
from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/windows"

def test_new_window(page:Page):
    page.goto(url)
    expect(page).to_have_title("The Internet")

    # Open new window and wait
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="Click Here").click()

    new_page = popup_info.value

    # Assertions in the new window
    expect(new_page).to_have_title("New Window")
    expect(new_page.locator("h3")).to_have_text("New Window")

