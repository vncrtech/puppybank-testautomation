from playwright.sync_api import Page


class WithdrawTransactionListPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.withdraw_transaction_list_page_hdr = page.get_by_role(
            "heading", name="Withdraw Transaction List")
        self.withdraws_table_hdr = page.get_by_role(
            "heading", name="Withdrawals")
        self.create_new_btn = page.get_by_role("link", name="Create New")
