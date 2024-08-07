import allure
from playwright.sync_api import Page, Locator, expect


class BasePage:
    page = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Navigate to {url}')
    def goto(self, url: str):
        self.page.goto(url)

    @allure.step('Find locator')
    def locator(self, locator: str) -> Locator:
        return self.page.locator(locator)

    @allure.step('Expect {locator}')
    def expect(self, locator: Locator):
        return expect(locator)
