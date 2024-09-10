from playwright.sync_api import Page


class CreatePuppyAccountPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.create_system_user_page_hdr = page.get_by_role(
            "heading", name="Create Puppy Account")
        self.create_system_user_img = page.locator("#content div").filter(
            has_text="Create Puppy Account").get_by_role("img")
        self.account_number_txt = page.locator("#id_account_number")
        self.account_balance_txt = page.locator("#id_account_balance")
        self.first_name_txt = page.locator("#id_account_balance")
        self.last_name_txt = page.locator("#id_last_name")
        self.address_txt = page.locator("#id_address")
        self.mobile_number_txt = page.locator("#id_mobile_number")
        self.email_address_txt = page.locator("#id_email_address")
        self.confirm_btn = page.get_by_role("button", name=" Confirm")
        self.back_to_list_lnk = page.get_by_role("link", name="Back to list →")
