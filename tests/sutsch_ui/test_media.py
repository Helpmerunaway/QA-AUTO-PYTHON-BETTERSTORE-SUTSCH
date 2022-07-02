from .pages.media_page import MediaPage
import pytest
import allure
from tests.sutsch_ui.config import media_link


@allure.title('TEST: Проверяем та ли это страница: /media')
@pytest.mark.media
def test_media_page_is_open(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Открыть страницу "Медиа"
    2. URL страницы содержит /media
    3. Заголовок содержит слово "Медиа"
    Ожидаемый результат:
    Пользователь находится на странице "Медиа"
    """
    page = MediaPage(browser, media_link)
    page.open()
    page.should_be_media_page()


@allure.title('TEST: Доступ незарегистрированного пользователя к странице /media')
@pytest.mark.media
def test_media_page_unauthorized_user(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу "Медиа"
    2. URL страницы содержит /media
    Ожидаемый результат:
    Не авторизованный пользователь попадает на страницу авторизации"
    """
    page = MediaPage(browser, media_link)
    page.open()
    page.media_page_open_by_unauthorized_user()


@allure.title('TEST: Проверка наличия элементов на странице /media')
@pytest.mark.media
def test_media_page_check_elements(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу /auth
    2. Ввести логин в поле Login
    3. Ввести пароль в поле Password
    4. Нажать на кнопку "Войти"
    5. URL страницы содержит /media
    6. Проверка наличия элементов, кнопок и полей на странице /media
    Ожидаемый результат:
    Веб-элементы страницы присутствуют"
    """
    page = MediaPage(browser, media_link)
    page.open()
    page.check_menu_buttons()
    page.check_media_page_header_buttons()
    page.check_media_page_main_area_buttons()


@allure.title('TEST: Клик по кнопкам на странице /media')
@pytest.mark.media
def test_media_page_clickable_buttons(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /media
    2. Проверка результата при нажатии на соответствующую кнопку на странице /media
    Ожидаемый результат:
    Пользователь попадает в соответствующий раздел меню"
    """
    page = MediaPage(browser, media_link)
    page.open()
    page.check_clickable_menu_buttons()


@allure.title('TEST: Проверка загрузки медиа-файла cat0.png')
@pytest.mark.media
def test_download_media_file_0(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Клик по кнопке медиа
    2. Клик по кнопке Загрузить файлы
    3. Клик по кнопке Выберите файл или просто перетащите
    4. Выбрать файл cat0.png
    4. Клик по кнопке загрузить
    5. Обновить страницу
    Ожидаемый результат:
    Медиа-файл присутствует на странице"
    """
    page = MediaPage(browser, media_link)
    page.open()
    page.upload_media_file_0()


@allure.title('TEST: Проверка удаления медиа-файла cat0.png')
@pytest.mark.delete
def test_delete_media_file_cat1(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Клик по кнопке медиа
    2. Клик на чекбокс напротив медиа-файла cat0
    3. Клик по кнопке Удалить
    4. Клик на кнопку "Да" в модальном окне "Вы уверены?"
    5. Обновить страницу
    Ожидаемый результат:
    Медиа-файл отсутствует на странице"
    """
    page = MediaPage(browser, media_link)
    page.open()
    page.delete_cat0()


@allure.title('TEST: Проверка загрузки медиа-файлов (5 шт)')
@pytest.mark.media
def test_download_media_files_5(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Клик по кнопке медиа
    2. Клик по кнопке Загрузить файлы
    3. Клик по кнопке Выберите файл или просто перетащите
    4. Выбрать файлы cat1.png - cat5.png
    4. Клик по кнопке загрузить
    5. Обновить страницу
    Ожидаемый результат:
    Медиа-файл присутствует на странице"
    """
    page = MediaPage(browser, media_link)
    page.open()
    page.upload_media_files_1_5()


@allure.title('TEST: Проверка удаления медиа-файлов cat1 - cat5')
@pytest.mark.media
def test_delete_media_files_cat5(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Клик по кнопке медиа
    2. Клик на чекбокс напротив медиа-файлов cat1 - cat5
    3. Клик по кнопке Удалить
    4. Клик на кнопку "Да" в модальном окне "Вы уверены?"
    5. Обновить страницу
    Ожидаемый результат:
    Медиа-файлы отсутствуют на странице"
    """
    page = MediaPage(browser, media_link)
    page.open()
    page.delete_cats1_5()


@allure.title('TEST: Проверка работы поиска')
@pytest.mark.media
def test_check_search_input(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе и находится на странице Медиа
    Шаги:
    1. Клик на форму "Поиск по названию"
    2. Ввести "Card"
    5. В форме "Поиск по названию" будет присутствовать Card
    Ожидаемый результат:
    Среди медиа-файлов будет найден Card_poster_2880x158_Web"
    """
    page = MediaPage(browser, media_link)
    page.open()
    page.check_search_field()
