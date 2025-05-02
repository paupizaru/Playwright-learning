# Test Exercise N° 17 
# Fill a simple form

from playwright.sync_api import Page, expect

url = "https://www.selenium.dev/selenium/web/web-form.html"

def test_simple_form(page:Page):
    page.goto(url)
    expect(page).to_have_title("Web form")

    text_input = page.get_by_role("textbox", name="Text input")
    submit = page.get_by_role("button", name="Submit")

    expect(text_input).to_be_visible()
    text_input.fill("Playwright testing.")

    expect(submit).to_be_visible()
    submit.click()

    expect(page).to_have_title("Web form - target page")
    expect(page.get_by_role("heading", name="Form submitted")).to_be_visible()
    expect(page.get_by_text("Received!")).to_be_visible()