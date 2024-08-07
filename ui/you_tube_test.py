import allure
import pytest
from playwright.sync_api import Page

from ui.page.you_tube_page import YouTubePage


@pytest.mark.usefixtures("page")
class TestYouTube:
    @pytest.fixture(autouse=True)
    def setup_steps(self, page: Page):
        self.yt = YouTubePage(page)

    @allure.title("Youtube search")
    @allure.story("YT-1235")
    def test_yt_search(self):
        self.yt.go_home()
        self.yt.search('playwright')
