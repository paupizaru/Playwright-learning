# Test Exercise N°15
# Interact with iframe

from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/iframe"

def test_interact_with_iframe(page:Page):
    page.goto(url)

    # Verify page title
    expect(page.get_by_role("heading", name="An iFrame containing the TinyMCE WYSIWYG Editor")).to_be_visible()


    # Locate the iFrame
    frame = page.frame_locator("#mce_0_ifr")

    # Inside the iframe, locate the editable text area
    editor = frame.locator("#tinymce")

    # # Clear any existing text
    # editor.click()
    # editor.press("Control+A") # Select all text
    # editor.press("Backspace") # Delete selected text
     
    # # Type new text
    # editor.type("Playwright test")

    # User JavaScript to set text directly
    editor.evaluate("element => element.innerHTML = 'Playwright test'")

    #Verify that the text is updated
    expect(editor).to_have_text("Playwright test")