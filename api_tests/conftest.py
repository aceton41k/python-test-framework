import pytest
import allure
import requests

from logging_http_adapter import LoggingHTTPAdapter


@pytest.fixture(scope='session')
def http_adapter():
    adapter = LoggingHTTPAdapter()
    session = requests.Session()
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.adapter = adapter
    return session


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        session = item.funcargs.get('http_adapter', None)
        if session and hasattr(session, 'adapter'):
            adapter = session.adapter
            with allure.step("Request Info"):
                if adapter.request_info:
                    request_info = adapter.format_info(adapter.request_info)
                    allure.attach(
                        body=request_info,
                        name='Request Info',
                        attachment_type=allure.attachment_type.TEXT
                    )
            with allure.step("Response Info"):
                if adapter.response_info:
                    response_info = adapter.format_info(adapter.response_info)
                    allure.attach(
                        body=response_info,
                        name='Response Info',
                        attachment_type=allure.attachment_type.TEXT
                    )
