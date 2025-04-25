# Test Exercise N°12
# JavaScript Prompt - Input & Accept

from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/javascript_alerts"

def test_js_prompt_input(page:Page):
    page.goto(url)
    
    # Set prompt text
    prompt_text = "Playwright test"

    # Handle prompt
    def handle_prompt(dialog):
        assert dialog.type == "prompt"
        dialog.accept(prompt_text)

    page.once("dialog", handle_prompt)

    # Click prompt
    page.get_by_role("button", name="Click for JS prompt").click()

    # Assert result
    result = page.locator("#result")
    expect(result).to_have_text(f"You entered: {prompt_text}")
