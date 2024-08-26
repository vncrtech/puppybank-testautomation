from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.sidebar_dashboard_lnk = page.get_by_role(
            "link", name=" Dashboard")
        self.sidebar_about_lnk = page.get_by_role("link", name=" About")
        self.sidebar_system_users_lnk = page.get_by_role(
            "link", name=" System Users ")
        self.sidebar_system_users_list_lnk = page.get_by_role(
            "link", name=" System Users ")
        self.sidebar_new_system_user_lnk = page.get_by_role(
            "link", name="New System User")
        self.sidebar_puppy_accounts_lnk = page.get_by_role(
            "link", name=" Puppy Accounts ")
        self.sidebar_puppy_account_list_lnk = page.get_by_role(
            "link", name="Puppy Account List")
        self.sidebar_new_puppy_account_lnk = page.get_by_role(
            "link", name="New Puppy Account")
        self.sidebar_deposit_lnk = page.get_by_role("link", name=" Deposit ")
        self.sidebar_deposit_transaction_list_lnk = page.get_by_role(
            "link", name="Deposit Transaction List")
        self.sidebar_new_deposit_lnk = page.get_by_role(
            "link", name="New Deposit")
        self.sidebar_withdraw_lnk = page.get_by_role(
            "link", name=" Withdraw ")
        self.sidebar_withdraw_transaction_list_lnk = page.get_by_role(
            "link", name="Withdraw Transaction List")
        self.sidebar_new_withdraw_lnk = page.get_by_role(
            "link", name="New Withdraw")
        self.sidebar_transfer_lnk = page.get_by_role(
            "link", name=" Transfer ")
        self.sidebar_transfer_transaction_list_lnk = page.get_by_role(
            "link", name="Transfer Transaction List")
        self.sidebar_new_transfer_lnk = page.get_by_role(
            "link", name="New Transfer")
