from playwright.sync_api import Page


class WithdrawTransactionPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.withdraw_transaction_page_hdr = page.get_by_role(
            "heading", name="Withdraw Transaction")
        self.withdraw_transaction_user_img = page.locator("#content div").filter(
            has_text="Withdraw Transaction").get_by_role("img")
        self.transaction_date = page.locator("#id_transaction_date")
        self.transaction_reference = page.locator("#id_transaction_reference")
        self.status = page.locator("#id_status")
        self.withdraw_amount = page.locator("#id_withdraw_amount")
        self.currency = page.locator("#id_currency")
        self.puppy = page.locator("#id_puppy")
        self.confirm_btn = page.get_by_role("button", name=" Confirm")
        self.back_to_list_lnk = page.get_by_role("link", name="Back to list →")
