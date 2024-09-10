from playwright.sync_api import Page


class PuppyAccountListPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.puppy_account_list_page_hdr = page.get_by_role(
            "heading", name="Puppy Account List")
        self.puppy_account_table_hdr = page.get_by_role(
            "heading", name="Puppies")
        self.create_new_btn = page.get_by_role("link", name="Create New")
