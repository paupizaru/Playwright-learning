# Test Exercise N°11
# JS alert

from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/javascript_alerts"

def test_js_alert(page:Page):
    page.goto(url)
    expect(page).to_have_title("The Internet")

    # Wait for dialog and accept
    def handle_dialog(dialog):
        assert dialog.type == "alert"
        assert dialog.message == "I am a JS Alert"
        dialog.accept()

    page.once("dialog", handle_dialog)

    # Click the button
    page.get_by_role("button", name="Click for JS Alert").click()

    # Assert final text
    result = page.locator("#result")
    expect(result).to_have_text("You successfully clicked an alert")