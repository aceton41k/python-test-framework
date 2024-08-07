import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(play: Playwright) -> None:
    browser = play.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.youtube.com/")
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder("Search").type("playwright")
    page.get_by_placeholder("Search").press("Enter")
    page.wait_for_load_state("domcontentloaded")
    page.get_by_role("link", name="Playwright Beginner Tutorials Automation Step by Step · Playlist Verified").click()
    page.locator("video").click()
    page.get_by_label("YouTube Video Player").click()
    page.get_by_label("Clear search query").click()

    # ---------------------
    context.close()
    browser.close()

