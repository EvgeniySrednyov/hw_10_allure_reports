import allure
from selene import browser, have


def test_lambda_steps():
    allure.dynamic.title('Тест с лямбда-шагами')
    allure.dynamic.description('Проверка наличия issue в репозитории')
    allure.dynamic.description_html('<h3>Тут что то должно быть, но я не понял практический смысл :)</h3>')
    allure.dynamic.label('Evgeniy') #почему то не отображается
    allure.dynamic.severity('MAJOR') #почему то не отображается
    allure.dynamic.epic('Изучение Allure Reports')
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Проверка задач в репозитории')
    allure.dynamic.tag('web', 'auto', 'selene')
    allure.dynamic.id('TK-001') #почему то не отображается
    allure.dynamic.link('https://github.com', name='Тестируемый ресурс')
    allure.dynamic.parameter('Тип запуска', 'auto')
    allure.dynamic.issue('https://github.com/eroshenkoam/allure-example/issues/65', 'Искомая issue')
    allure.dynamic.testcase('https://github.com/EvgeniySrednyov/hw_10_allure_reports', 'Тест-кейсы')
    with allure.step('Открытие главной страницы'):
        browser.open('https://github.com/')

    with allure.step('Поиск репозитория eroshenkoam/allure-example'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переход в репозиторий eroshenkoam/allure-example'):
        browser.element('[href="/eroshenkoam/allure-example"]').click()

    with allure.step('Переход на вкладку Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверка наличия issue "с днем археолога!"'):
        browser.element('#issue_65_link').should(have.text('с днем археолога!'))


