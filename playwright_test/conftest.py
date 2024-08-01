import pytest
from playwright.sync_api import sync_playwright
import allure


@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page  = context.new_page()
        yield page
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    page = item.funcargs.get('page')
    if page and report.when == 'call' and report.failed:
        screenshot_path = f"screenshots/{item.nodeid.replace('/', '_').replace(':', '_')}.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.JPG)
        print(f"Screenshot saved to {screenshot_path}")
