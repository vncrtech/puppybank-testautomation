from playwright.sync_api import Page


class RegistrationPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.registration_page_hdr = page.get_by_role(
            "heading", name="Create a User!")
        self.registration_page_img = page.get_by_role("img")
        self.username_txt = page.locator("#id_username")
        self.username_hlp = page.locator("#id_username + .help")
        self.password1_txt = page.locator("#id_password1")
        self.password1_hlp = page.locator("#id_password1 + .help")
        self.password2_txt = page.locator("#id_password2")
        self.password2_hlp = page.locator("#id_password2 + .help")
        self.register_user_btn = page.get_by_role(
            "button", name="Register User")
        self.already_have_an_account_lnk = page.get_by_role(
            "link", name="Already have an account?")
