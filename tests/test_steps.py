import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s




def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        s('.header-search-button').click()
        s('#query-builder-test').type('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие ишью с номером 76'):
        s(by.partial_text('#76')).should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issues_tab()
    should_see_with_number('#76')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')
@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').type(repo)
    s('#query-builder-test').submit()

@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step('Открываем таб issues')
def open_issues_tab():
    s('#issues-tab').click()

@allure.step('Проверяем наличие ишью с номером {number}')
def should_see_with_number(number):
    s(by.partial_text(number)).should(be.visible)
