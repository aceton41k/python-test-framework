from playwright.sync_api import expect


def test_todos(page):
    url = 'https://demo.playwright.dev/todomvc/#/'
    page.goto(url)
    expect(page).to_have_url(url)
    locator = page.get_by_placeholder('What needs to be done?')
    expect(locator).to_be_empty()
    locator.fill("task1")
    locator.press("Enter")
    locator.fill("task2")
    locator.press("Enter")
    expect(page.get_by_test_id('todo-item')).to_have_count(2)
    checkbox = page.locator("li").filter(has_text="task1").get_by_label("Toggle Todo")
    checkbox.click()
    expect(page.locator("li:has-text('task1')")).to_have_class("completed")
