# Test Exercise N°7
# Fail login

import re
from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/login"

def test_fail_login(page:Page):
    page.goto(url)
    expect(page).to_have_title("The Internet")

    username = page.locator("#username")
    password = page.locator("#password")
    login = page.locator("button[type='submit']")

    # Type invalid credentials
    username.fill("wrongusername")
    password.fill("wrongpassword")
    login.click()

    # Error message
    error_message = page.locator(".flash.error")
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text(re.compile("Your username is invalid!"))

    # Check url
    expect(page).to_have_url(url)