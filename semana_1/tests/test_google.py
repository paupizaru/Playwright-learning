# Testing google #

# Import re module for regular expressions 
# Import
import re
from playwright.sync_api import Page, expect

# Define the url outside in case of need to use it multiple times
url = "https://www.google.cl"


# Define the test as a function()
def test_has_title(page: Page):
    #We tell the page to load the specified url.
    page.goto(url)

    #We expect to find the worg "Google" in the title of the loaded page.
    expect(page).to_have_title(re.compile("Google"))
 
def test_search(page: Page):
    #This is for start tracing the steps of the test, taking snapshots
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto(url)

    expect(page).to_have_title(re.compile("Google"))

    #We tell the page to fill the input with the specified selector with the word "Playwright"
    page.fill('#APjFqb',"Playwright")

    #We press "Enter" in our keyboard to simulate the search.
    page.keyboard.press("Enter")

    #This is to stop tracing and where the snapshots are going to be stored.
    page.context.tracing.stop(path="trace.zip")

