from playwright.sync_api import Page


class DepositTransactionListPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.deposit_transaction_list_page_hdr = page.get_by_role(
            "heading", name="Deposit Transaction List")
        self.deposits_table_hdr = page.get_by_role(
            "heading", name="Deposits")
        self.create_new_btn = page.get_by_role("link", name="Create New")
