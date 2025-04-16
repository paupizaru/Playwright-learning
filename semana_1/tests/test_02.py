# Test Exercise N°2
# Go to Google and search for a word.

# Import re module for regular expressions 
import re
from playwright.sync_api import Page, expect

# Define the url outside
url = "https://www.google.cl"

def test_search(page: Page):
    # This is to start tracing the steps of the test, taking snapshots
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto(url)

    expect(page).to_have_title(re.compile("Google"))

    # We tell the page to fill the input with the specified selector with the word "Playwright"
    page.fill('#APjFqb',"Playwright")

    # We press "Enter" in our keyboard to recreate the search.
    page.keyboard.press("Enter")

    # This is to stop tracing and also where the snapshots are going to be stored.
    page.context.tracing.stop(path="trace.zip")

