from playwright.sync_api import Page


class AboutPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.about_page_hdr = page.get_by_role(
            "heading", name="About Puppy Bank")
        self.getting_started_hdr = page.get_by_role(
            "heading", name="Getting Started")
        self.getting_started_bdy = page.locator(
            ".card-header:has(> h6:text('Getting Started')) + .card-body p")
        self.getting_started_img = page.locator(
            ".card-header:has(> h6:text('Getting Started')) + .card-body img")
        self.puppy_bank_features_hdr = page.get_by_role(
            "heading", name="Puppy Bank Features")
        self.puppy_bank_features_bdy = page.locator(
            ".card-header:has(> h6:text('Puppy Bank Features')) + .card-body p")
        self.puppy_bank_features_img = page.locator(
            ".card-header:has(> h6:text('Puppy Bank Features')) + .card-body img")
        self.why_made_hdr = page.get_by_role(
            "heading", name="Why it was made?")
        self.why_made_bdy = page.locator(
            ".card-header:has(> h6:text('Why it was made?')) + .card-body p")
        self.why_made_img = page.locator(
            ".card-header:has(> h6:text('Why it was made?')) + .card-body img")
        self.sources_hdr = page.get_by_role(
            "heading", name="Sources")
        self.sources_bdy = page.locator(
            ".card-header:has(> h6:text('Sources')) + .card-body p")
        self.explore_now_btn = page.get_by_role("link", name=" Explore Now")
