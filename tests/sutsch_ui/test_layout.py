from tests.sutsch_ui.pages.layout_page import LayoutPage
import pytest
import allure
from tests.sutsch_ui.config import auth_link, layout_link



@allure.title('TEST: Должна быть страница Макеты полки')
@pytest.mark.layout
def test_layout_page_is_open(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Открыть страницу "Макеты полки"
    2. URL страницы содержит /layout
    3. Присутствует кнопка "Создать макет"
    Ожидаемый результат:
    Пользователь находится на странице "Макеты полки"
    """
    page = LayoutPage(browser, layout_link)
    page.open()
    page.should_be_layout_page()


@allure.title('TEST: Доступ неавторизованного пользователя к странице /layout')
@pytest.mark.layout
def test_layout_page_unauthorized_user(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу "Макеты полки"
    2. URL страницы содержит /layout
    Ожидаемый результат:
    Неавторизованного пользователя переводят на страницу авторизации"
    """
    page = LayoutPage(browser, layout_link)
    page.open()
    page.layout_page_open_by_unauthorized_user()


@allure.title('TEST: Проверка наличия элементов на странице /layout')
@pytest.mark.layout
def test_layout_page_check_elements(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /layout
    2. Проверка наличия элементов, кнопок и полей на странице /layout
    Ожидаемый результат:
    Веб-элементы страницы присутствуют"
    """
    page = LayoutPage(browser, layout_link)
    page.open()
    page.check_menu_buttons()
    page.check_layout_page_header_buttons()
    page.check_layout_page_main_area_buttons()


@allure.title('TEST: Клик по кнопкам на странице /layout')
@pytest.mark.layout
def test_layout_page_clickable_buttons(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /layout
    2. Проверка результата при нажатии на соответствующую кнопку на странице /layout
    Ожидаемый результат:
    Пользователь попадает в соответствующий раздел меню"
    """
    page = LayoutPage(browser, layout_link)
    page.open()
    page.check_clickable_menu_buttons()


@allure.title('TEST: Создание пустого макета полки')
@pytest.mark.layout
def test_layout_create_empty_layout(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /layout
    2. Клик на кнопку Создать макет
    3. Клик на Сохранить
    Ожидаемый результат:
    Пустой макет не создан. Пользователь видит алерт Ошибка! Укажите название макета.
    """
    page = LayoutPage(browser, layout_link)
    page.open()
    page.create_new_layout_empty()


@allure.title('TEST: Создание нового валидного макета полки')
@pytest.mark.layout
def test_layout_create_new_valid_layout(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /layout
    2. Клик на кнопку Создать макет
    3. Заполнить поле "Название макета"
    4. Выбрать "Шаблон ценников" из выпадающего списка
    5. Клик и заполнить поле - 11  "Количество, шт."
    6. Выбрать 2880x158 в поле "Для каких устройств" из выпадающего списка
    7. Клик по полю "Добавьте тэги"
    8. Ввести тэг "new_maket" в поле "Тэги"
    9. Клик на кнопку "Добавить"
    10. Клик на кнопку "Сохранить"
    Ожидаемый результат:
    Созданный макет отображается на странице "Макеты полки".
    """
    page = LayoutPage(browser, layout_link)
    page.open()
    page.create_new_layout_maket_date_time()


@allure.title('TEST: Открыть новый макет полки')
@pytest.mark.layout
def test_layout_open_new_valid_layout(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /layout
    2. Клик на кнопку "Открыть"
    3. Сделать скриншот экрана предпросмотра
    4. Проверка названия макета "Maket "
    4. Клик на кнопку "Закрыть"
    Ожидаемый результат:
    Открывается страница предпросмотра. Данные о макете верные.
    """
    page = LayoutPage(browser, layout_link)
    page.open()
    page.open_new_layout_maket_date_time()


@allure.title('TEST: Изменить новый макет полки')
@pytest.mark.layout
def test_layout_edit_new_valid_layout(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /layout
    2. Клик на кнопку "Изменить"
    3. Кликнуть по полю "Добавить тэги"
    4. Ввести "MODIFIED"
    5. Клик по кнопке "Добавить"
    6. Клик по кнопке "Сохранить"
    Ожидаемый результат:
    Новый тэг отображается у редактированного макета в колонке "Тэги"
    """
    page = LayoutPage(browser, layout_link)
    page.open()
    page.edit_new_layout_maket_date_time()


@allure.title('TEST: Удалить новый макет полки')
@pytest.mark.layout
def test_layout_delete_new_valid_layout(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /layout
    2. Клик на чекбокс созданного макета
    3. Клик на кнопку "Удалить"
    4. Клик на кнопку "Да" в модальном окне "Вы уверены?"
    Ожидаемый результат:
    Макет не отображается на странице "Макеты полки"
    """
    page = LayoutPage(browser, layout_link)
    page.open()
    page.delete_maket_from_layouts()
