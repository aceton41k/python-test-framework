import pytest
from playwright.sync_api import sync_playwright
import allure


@pytest.fixture(scope='function')
def page():
    locale = 'en_US'
    headless = True
    video = False
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless,
                                    args=[
                                        # '--enable-logging=stderr',
                                        # '--v=1',
                                        f'--lang={locale}'
                                    ],
                                    env={
                                        # 'PLAYWRIGHT_LOG': 'debug'
                                    }
                                    )
        if video:
            context = browser.new_context(
                record_video_dir='videos/',  # Директория для хранения видео
                record_video_size={'width': 1280, 'height': 720}  # Размер видео
            )
        else:
            context = browser.new_context()
        page = context.new_page()
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
