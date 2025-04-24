# Test Exercise N°9
# Broken images

from playwright.sync_api import Page, expect

url = "https://the-internet.herokuapp.com/broken_images"

def test_assert_images(page:Page):
    page.goto(url)
    expect(page).to_have_title("The Internet")

    # Set uo locator and assert count
    images = page.locator("img")
    expect(images).to_have_count(4)

    # Assert iteration to check if img is broken
    for i in range(3):
        img = images.nth(i)
        width = img.evaluate("el => el.naturalWidth")
        src = img.get_attribute("src")
        print(f"Image {i} - src: {src} - width: {width}")

        # assert width !=0, f"Broken image found on index {i}"
        if width == 0:
            broken_found = True

    assert broken_found, "There was not found any broken image (and there should be at least one)"
