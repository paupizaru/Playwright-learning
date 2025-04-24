# Test Exercise N°5
# Assert dropdown

from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/dropdown"

def test_dropdown(page:Page):
    page.goto(url)

    expect(page).to_have_title("The Internet")

    dropdown = page.locator("select#dropdown")

    # Select value 1
    dropdown.select_option("1")
    expect(dropdown).to_have_value("1")