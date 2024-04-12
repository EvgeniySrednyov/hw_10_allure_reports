import allure
from selene import browser, have

@allure.title('Тест с декораторами')
@allure.description('Проверка наличия issue в репозитории')
@allure.description_html('<h3>Тут что то должно быть, но я не понял практический смысл :)</h3>')
@allure.label('Evgeniy') #почему то не отображается
@allure.severity('MAJOR') #почему то не отображается
@allure.epic('Изучение Allure Reports')
@allure.feature('Задачи в репозитории')
@allure.story('Проверка задач в репозитории')
@allure.tag('web', 'auto', 'selene')
@allure.id('TK-002') #почему то не отображается
@allure.link('https://github.com', name='Тестируемый ресурс')
@allure.issue('https://github.com/eroshenkoam/allure-example/issues/65', 'Искомая issue')
@allure.testcase('https://github.com/EvgeniySrednyov/hw_10_allure_reports', 'Тест-кейсы')
def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    go_to_issues_tab()
    check_for_issue_name('с днем археолога!')


@allure.step('Открытие главной страницы')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Поиск репозитория {repo}')
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type(repo).press_enter()


@allure.step('Переход в репозиторий {repo}')
def go_to_repository(repo):
    browser.element(f'[href="/{repo}"]').click()


@allure.step('Переход на вкладку Issues')
def go_to_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверка наличия issue {name}')
def check_for_issue_name(name):
    browser.element('#issue_65_link').should(have.text(name))