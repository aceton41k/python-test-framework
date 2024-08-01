import allure
from playwright.sync_api import sync_playwright
from pytest import mark


@mark.skip('No runnable')
def test_pw(page):
    with sync_playwright() as p:
        page.goto('https://google.com')


@allure.title("Youtube search")
@allure.story("YT-1235")
def test_yt_search(page):
    page.goto('https://www.youtube.com/')
    assert page.query_selector("//ytd-topbar-logo-renderer[@id='logo']") is not None
    page.locator("//input[@id='search']").type('playwright', timeout=1000)
    page.locator("//button[@id='search-icon-legacy']").first.click(timeout=1000)
    page.wait_for_load_state('networkidle')
    results = page.locator("//a[@id='video-title']").all()
    assert len(results) > 10


def test_blank():
    just_step(5, 'hello')
    assert 1 == 1


@allure.title('Failed test')
def test_failed(page):
    page.goto('https://www.youtube.com/')
    page.wait_for_load_state('networkidle')
    assert 1 == 2


def just_step(arg1: int, arg2: str):
    print(arg1)
    print(arg2)
    pass
