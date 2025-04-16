# Test Exercise N°1
# Go to Google and verify that has title.

# Import re module for regular expressions 
import re
from playwright.sync_api import Page, expect

# Define the url outside
url = "https://www.google.cl"


# Define the test
def test_has_title(page: Page):
    # We tell the page to load the specified url.
    page.goto(url)

    # We expect to find the word "Google" in the title of the loaded page.
    expect(page).to_have_title(re.compile("Google"))