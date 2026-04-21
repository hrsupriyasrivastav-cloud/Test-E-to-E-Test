class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_btn = page.locator("button[type='submit']")
        self.success_msg = page.locator(".flash.success")

    def navigate(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()

    def is_login_successful(self):
        return self.success_msg.is_visible()
    
    
