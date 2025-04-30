# Test Exercise N°15
# 
import os
from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/upload"

def test_file_upload(page:Page):
    page.goto(url, wait_until="domcontentloaded")

    expect(page.get_by_role("heading", name="File Uploader")).to_be_visible()

    # Get the file path
    current_dir = os.path.dirname(__file__)
    file_path =  os.path.abspath(os.path.join(current_dir, "..", "..", "files", "test_file.txt"))

#  # Debug prints
#     print("File path:", file_path)
#     print("¿Does the file exist?", os.path.exists(file_path))

    # Set file to input
    file_input = page.locator("input#file-upload")
    file_input.wait_for(state="visible")
    file_input.set_input_files(file_path)

    # Click Upload
    page.click("input#file-submit")

    # Assertions
    expect(page.locator("h3")).to_have_text("File Uploaded!")
    expect(page.locator("#uploaded-files")).to_have_text("test_file.txt")
