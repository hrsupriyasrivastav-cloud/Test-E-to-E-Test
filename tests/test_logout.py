from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_logout(custom_page):
    login = LoginPage(custom_page)

    login.navigate()
    login.login("tomsmith", "SuperSecretPassword!")

    login.logout()

    expect(custom_page.locator(".flash.success")).to_contain_text("logged out")
    