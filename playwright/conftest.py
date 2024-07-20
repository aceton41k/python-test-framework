import pytest
from playwright.sync_api import Page, sync_playwright
import allure


@pytest.fixture(scope='function')
def page():
    # Запускаем Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()  # Вы можете использовать 'firefox' или 'webkit' вместо 'chromium'
        context = browser.new_context()
        page = page = context.new_page()
        yield page
        # Закрываем браузер после теста
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Получаем доступ к тестовому контексту
    page = item.funcargs.get('page')  # Предполагаем, что у вас есть фикстура 'page'
    if page and report.when == 'call' and report.failed:
        # Создаем скриншот
        screenshot_path = f"screenshots/{item.nodeid.replace('/', '_').replace(':', '_')}.png"
        page.screenshot(path=screenshot_path)
        # Прикрепляем скриншот к отчету Allure
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.JPG)
        print(f"Screenshot saved to {screenshot_path}")
