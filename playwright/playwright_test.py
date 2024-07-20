import typing
from typing import List

import allure
import pytest
from playwright.sync_api import sync_playwright
from pytest import mark


@mark.skip('Не запускаем')
def test_pw():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://yandex.ru')
        page.screenshot(path=f'example-{p.chromium.name}.png')
        browser.close()


@allure.title("Youtube search")
def test_yt_search(page):
    page.goto('https://www.youtube.com/')
    assert page.query_selector("//ytd-topbar-logo-renderer[@id='logo']") is not None
    page.locator("//input[@id='search']").type('playwright', timeout=1000)
    page.locator("//button[@id='search-icon-legacy']").first.click(timeout=1000)
    page.wait_for_load_state('networkidle')
    results = page.locator("//a[@id='video-title111111111111111111111111111']").all()
    assert len(results) > 10


def test_blank():
    just_step(5, 'hello')
    assert 1 == 1


def test_failed():
    """
    Падающий тест
    """
    assert 1 == 2


def just_step(arg1: int, arg2: str):
    print(arg1)
    print(arg2)
    pass
