from playwright.sync_api import Page


class TransferTransactionPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.transfer_transaction_page_hdr = page.get_by_role(
            "heading", name="Transfer Transaction")
        self.transfer_transaction_user_img = page.locator("#content div").filter(
            has_text="Transfer Transaction").get_by_role("img")
        self.transaction_date = page.locator("#id_transaction_date")
        self.transaction_reference = page.locator("#id_transaction_reference")
        self.status = page.locator("#id_status")
        self.transfer_amount = page.locator("#id_transfer_amount")
        self.currency = page.locator("#id_currency")
        self.from_puppy = page.locator("#id_from_puppy")
        self.to_puppy = page.locator("#id_to_puppy")
        self.confirm_btn = page.get_by_role("button", name=" Confirm")
        self.back_to_list_lnk = page.get_by_role("link", name="Back to list →")
