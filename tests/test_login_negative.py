from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_invalid_login(custom_page):
    login = LoginPage(custom_page)

    login.navigate()
    login.login("wrong_user", "wrong_pass")

    expect(custom_page.locator(".flash.error")).to_be_visible()