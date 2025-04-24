# Test Exercise N°6
# Dynamic loading

from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/dynamic_loading/1"

def test_wait(page:Page):
    page.goto(url)
    expect(page).to_have_title("The Internet")

    page.get_by_role("button", name="Start").click()
    
    # Wait for the text to be visible
    page.get_by_text("Hello World!").wait_for(state="visible")

    # Assertion
    expect(page.get_by_text("Hello World!")).to_be_visible()
