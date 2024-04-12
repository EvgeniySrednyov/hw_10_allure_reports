from selene import browser, have


def test_github():
    browser.open('https://github.com/')

    browser.element('.search-input').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()
    browser.element('[href="/eroshenkoam/allure-example"]').click()
    browser.element('#issues-tab').click()

    browser.element('#issue_65_link').should(have.text('с днем археолога!'))


