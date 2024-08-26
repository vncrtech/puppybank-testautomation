from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.dashboard_page_hdr = page.get_by_role("heading", name="Dashboard")
        self.aggregate_deposit_crd = page.locator(
            ".card:has( .text-xs:text('Aggregate Deposit'))")
        self.aggregate_deposit_value_lbl = page.locator(
            ".card .text-xs:text('Aggregate Deposit') + div")
        self.aggregate_withdraw_crd = page.locator(
            ".card:has( .text-xs:text('Aggregate Withdraw'))")
        self.aggregate_withdraw_value_lbl = page.locator(
            ".card .text-xs:text('Aggregate Withdraw') + div")
        self.aggregate_transfer_crd = page.locator(
            ".card:has( .text-xs:text('Aggregate Transfer'))")
        self.aggregate_transfer_value_lbl = page.locator(
            ".card .text-xs:text('Aggregate Transfer') + div")
        self.aggregate_number_of_transactions_crd = page.locator(
            ".card:has( .text-xs:text('Number of Transactions'))")
        self.aggregate_number_of_transactions_value_lbl = page.locator(
            ".card .text-xs:text('Number of Transactions') + div")
        self.cashflow_chart = page.get_by_text("Cash Flow Not actual data.")
        self.transaction_mix_chart = page.get_by_text(
            "Transaction Mix Not actual")
