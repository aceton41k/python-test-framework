import allure

from pytest import mark


@mark.skip('No runnable')
@allure.title('No runnable')
def test_pw(page):
    pass


@allure.title('Failed test')
def test_failed(page):
    page.goto('https://www.youtube.com/')
    assert 1 == 2
