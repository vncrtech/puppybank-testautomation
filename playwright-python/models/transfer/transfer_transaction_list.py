from playwright.sync_api import Page


class TransferTransactionListPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.transfer_transaction_list_page_hdr = page.get_by_role(
            "heading", name="Transfer Transaction List")
        self.transfers_table_hdr = page.get_by_role(
            "heading", name="Transfers")
        self.create_new_btn = page.get_by_role("link", name="Create New")
