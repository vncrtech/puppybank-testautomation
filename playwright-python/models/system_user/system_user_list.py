from playwright.sync_api import Page


class SystemUserListPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.system_user_list_page_hdr = page.get_by_role(
            "heading", name="System User List")
        self.system_users_table_hdr = page.get_by_role(
            "heading", name="System Users")
        self.create_new_btn = page.get_by_role("link", name="Create New")
