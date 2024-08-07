import allure

from pytest import mark


@mark.skip('No runnable')
@allure.title('No runnable')
def test_pw(page):
    pass
