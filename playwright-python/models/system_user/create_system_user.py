from playwright.sync_api import Page


class CreateSystemUserPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.create_system_user_page_hdr = page.get_by_role(
            "heading", name="Create System User")
        self.create_system_user_img = page.locator("#content div").filter(
            has_text="Create System User").get_by_role("img")
        self.username_txt = page.locator("#id_username")
        self.username_hlp = page.locator("#id_username + .help")
        self.password_txt = page.locator("#id_password1")
        self.password_hlp = page.locator("#id_password1 + .help")
        self.repeat_password_txt = page.locator("#id_password2")
        self.repeat_password_hlp = page.locator("#id_password2 + .help")
        self.confirm_btn = page.get_by_role("button", name=" Confirm")
        self.back_to_list_lnk = page.get_by_role("link", name="Back to list →")
