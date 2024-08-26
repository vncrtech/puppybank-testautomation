from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_page_hdr = page.get_by_role(
            "heading", name="Welcome to Puppy Bank")
        self.login_img = page.get_by_role("img")
        self.username_txt = page.get_by_placeholder("Username")
        self.password_text = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button", name="Log in")
        self.register_btn = page.get_by_role("link", name="Register")
        self.about_the_app_lnk = page.get_by_role("link", name="About the App")
