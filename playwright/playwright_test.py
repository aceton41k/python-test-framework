import allure
from playwright.sync_api import sync_playwright, expect
from pytest import mark

import recorder_test


@mark.skip('No runnable')
def test_pw(page):
    with sync_playwright() as p:
        page.goto('https://google.com')


@allure.title("Youtube search")
@allure.story("YT-1235")
def test_yt_search(page):
    page.goto('https://www.youtube.com/')
    expect(page.locator("//ytd-topbar-logo-renderer[@id='logo']")).to_be_visible(timeout=5000)
    search_input = page.locator("//input[@id='search']")
    search_input.wait_for(state='visible', timeout=5000)
    search_input.type('playwright')
    search_button = page.locator("//button[@id='search-icon-legacy']")
    search_button.wait_for(state='visible', timeout=5000)
    search_button.click(timeout=10000, delay=1000)
    page.wait_for_load_state('networkidle')
    page.wait_for_load_state('domcontentloaded')
    results = page.locator("//a[@id='video-title']")
    assert len(results.all()) > 5


def test_blank():
    just_step(5, 'hello')
    assert 1 == 1


@allure.title('Failed test')
def test_failed(page):
    page.goto('https://www.youtube.com/')
    page.wait_for_load_state('networkidle')
    assert 1 == 2


@allure.step
def just_step(arg1: int, arg2: str):
    print(arg1)
    print(arg2)
    pass
