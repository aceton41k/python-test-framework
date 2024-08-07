import allure
from playwright.sync_api import Page

from ui.page.base_page import BasePage


class YouTubePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = self.locator("//input[@id='search']")
        self.search_button = self.locator("//button[@id='search-icon-legacy']")
        self.logo = self.locator("//ytd-topbar-logo-renderer[@id='logo']")

    def go_home(self):
        self.goto('https://youtube.com')
        self.expect(self.logo).to_be_visible(timeout=5000)

    @allure.step('Search')
    def search(self, query):
        self.search_input.wait_for(state='visible', timeout=5000)
        self.search_input.type(query)
        self.search_button.wait_for(state='visible', timeout=5000)
        self.search_button.click(timeout=10000, delay=1000)
        self.page.wait_for_load_state('networkidle')

    @allure.step('Check search results')
    def check_search_results(self):
        results = self.locator("//a[@id='video-title']")
        assert len(results.all()) > 5
