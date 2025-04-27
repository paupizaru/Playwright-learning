# Test Exercise N°14
# Open a new tab and switch focus

from playwright.sync_api import Page, BrowserContext, expect

url = "https://the-internet.herokuapp.com/windows"

def test_open_new_tab_and_switch(page:Page, context:BrowserContext):
    page.goto(url)
    expect(page).to_have_title("The Internet")

    # Verify we are on the correct page
    expect(page.get_by_role("heading", name="Opening a new window")).to_be_visible()

    # Use context.expect_page() before clicking
    with context.expect_page() as new_page_info:
        # Click the link that opens a new tab
        page.get_by_role("link", name="Click Here").click()
    new_page = new_page_info.value
    
    # Verify the new tab content
    expect(new_page.get_by_role("heading", name="New Window")).to_be_visible()

    # Go back to the original page
    page.bring_to_front()
    expect(page.get_by_role("heading", name="Opening a new window"))