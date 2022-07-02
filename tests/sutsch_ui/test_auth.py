from tests.sutsch_ui.pages.login_page import LoginPage
import pytest
import allure
from tests.sutsch_ui.pages.devices_page import DevicesPage
from tests.sutsch_ui.config import auth_link, devices_link


@allure.title('TEST: Должна быть страница авторизации')
@pytest.mark.login
def test_login_page_is_open(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу "Авторизация"
    2. URL страницы содержит /auth
    3. Заголовок содержит слово "Авторизация"
    Ожидаемый результат:
    Пользователь находится на странице "Авторизация"
    """
    page = LoginPage(browser, auth_link)
    page.open()
    page.should_be_login_page()


@allure.title('TEST: Присутствие веб-элементов на странице')
@pytest.mark.login
def test_login_page_check_elements(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу /auth
    2. URL страницы содержит /auth
    3. Проверка наличия элементов, кнопок и полей на странице /devices
    Ожидаемый результат:
    Веб-элементы страницы присутствуют"
    """
    page = LoginPage(browser, auth_link)
    page.open()
    page.should_be_login_page_elements()


@allure.title('TEST: Проверка кнопок на странице авторизации')
@pytest.mark.login
def test_login_page_click_on_buttons(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу /auth
    2. Проверка результата при нажатии на соответствующую кнопку на странице /auth
    Ожидаемый результат:
    Пользователь попадает в соответствующий раздел меню"
    """
    page = LoginPage(browser, auth_link)
    page.open()
    page.click_on_buttons()


@allure.title('TEST: Авторизация пользователя в системе')
@pytest.mark.login
def test_login_user(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу /auth
    2. Ввести логин в поле Login
    3. Ввести пароль в поле Password
    4. Нажать на кнопку "Войти"
    Ожидаемый результат:
    Пользователь попадает на страницу "Устройства". Имя пользователя отображается на странице.
    """
    page = LoginPage(browser, auth_link)
    page.open()
    page.do_login_user_2()


@allure.title('TEST: Авторизация пользователя Игорь Лебедев в системе')
@pytest.mark.login
def test_login_user_2(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу /auth
    2. Ввести логин пользователя Игорь Лебедев в поле Login
    3. Ввести пароль пользователя Игорь Лебедев в поле Password
    4. Нажать на кнопку "Войти"
    Ожидаемый результат:
    Пользователь попадает на страницу "Устройства". Имя пользователя отображается на странице.
    """
    page = LoginPage(browser, auth_link)
    page.open()
    page.do_login_user_2()


@allure.title('TEST: Авторизация с неверным паролем')
@pytest.mark.login
def test_login_fake_password(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу /auth
    2. Ввести логин в поле Login
    3. Ввести невалидный пароль в поле Password
    4. Нажать на кнопку "Войти"
    Ожидаемый результат:
    Всплывающее окно оповещает об ошибке "Неверный логин или пароль". Пользователь остается на странице авторизации.
    """
    page = LoginPage(browser, auth_link)
    page.open()
    page.fake_password()


@allure.title('TEST: Авторизация с неверным емейлом')
@pytest.mark.login
def test_login_fake_email(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу /auth
    2. Ввести невалидный логин в поле Login
    3. Ввести пароль в поле Password
    4. Нажать на кнопку "Войти"
    Ожидаемый результат:
    Всплывающее окно оповещает об ошибке "Неверный логин или пароль". Пользователь остается на странице авторизации.
    """
    page = LoginPage(browser, auth_link)
    page.open()
    page.fake_email()


@allure.title('TEST: Выход пользователя из системы')
@pytest.mark.login
def test_logout_user(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу /auth
    2. Ввести логин в поле Login
    3. Ввести пароль в поле Password
    4. Нажать на кнопку "Войти"
    5. Пользователь авторизуется в системе на странице "Устройства". Имя пользователя отображается на странице.
    6. Нажать на кнопку "Выйти"
    Ожидаемый результат:
    Пользователь попадает на страницу "Авторизация"
    """
    page = LoginPage(browser, auth_link)
    page.open()
    page.do_login_user_2()
    page = DevicesPage(browser, devices_link)
    page.open()
    page.logout_user()



