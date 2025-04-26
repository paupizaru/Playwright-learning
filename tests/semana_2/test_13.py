# Test Exercise N°13
# Sliders

from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/horizontal_slider"

def test_sliders(page:Page):
    page.goto(url)
    expect(page).to_have_title("The Internet")

    slider = page.locator("input[type='range']")
    result = page.locator("#range")

    # Click the slider to focus
    slider.click()

    # Keep pressing ArrowRight until the result shows "4"
    while True:
        current_value = result.inner_text()
        if current_value == "4":
            break
        slider.press("ArrowRight")

    # Verify the slider value
    expect(result).to_have_text("4")
