from tests.sutsch_ui.pages.devices_page import DevicesPage
import pytest
import allure
from tests.sutsch_ui.config import devices_link


@allure.title('TEST: Проверяем что открыта страница Устройства')
@pytest.mark.devices
def test_devices_page_is_open(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Открыть страницу "Устройства"
    2. URL страницы содержит /devices
    3. Заголовок содержит слово "Устройства"
    Ожидаемый результат:
    Пользователь находится на странице "Устройства"
    """
    page = DevicesPage(browser, devices_link)
    page.should_be_devices_page()


@allure.title('TEST: Доступ незарегистрированного пользователя к странице /devices')
@pytest.mark.devices
def test_devices_page_unauthorized_user(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу "Устройства"
    2. URL страницы содержит /devices
    Ожидаемый результат:
    Не авторизованный пользователь видит загрузчик"
    """
    page = DevicesPage(browser, devices_link)
    page.open()
    page.devices_page_open_by_unauthorized_user()


@allure.title('TEST: Проверка наличия элементов на странице /devices')
@pytest.mark.devices
def test_devices_page_check_elements(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу /auth
    2. Ввести логин в поле Login
    3. Ввести пароль в поле Password
    4. Нажать на кнопку "Войти"
    5. URL страницы содержит /devices
    6. Проверка наличия элементов, кнопок и полей на странице /devices
    Ожидаемый результат:
    Веб-элементы страницы присутствуют"
    """
    page = DevicesPage(browser, devices_link)
    page.open()
    page.check_menu_buttons()
    page.check_devices_page_header_buttons()
    page.check_devices_page_main_area_buttons()


@allure.title('TEST: Клик по кнопкам на странице /devices')
@pytest.mark.devices
def test_devices_page_clickable_buttons(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /devices
    2. Проверка результата при нажатии на соответствующую кнопку на странице /devices
    Ожидаемый результат:
    Пользователь попадает в соответствующий раздел меню"
    """
    page = DevicesPage(browser, devices_link)
    page.open()
    page.check_clickable_menu_buttons()
# кнопка dashboard недоступна 23.05.2022
# кнопка statistic недоступна 23.05.2022
