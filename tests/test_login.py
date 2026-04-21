from pages.login_page import LoginPage

def test_valid_login(custom_page):
    login = LoginPage(custom_page)

    login.navigate()
    login.login("tomsmith", "SuperSecretPassword!")

    assert False