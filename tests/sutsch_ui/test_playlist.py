from tests.sutsch_ui.pages.playlist_page import PlaylistPage
import pytest
import allure
from tests.sutsch_ui.config import playlist_link


@allure.title('TEST: Должна быть страница Плейлисты')
@pytest.mark.playlist
def test_playlist_page_is_open(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Открыть страницу "Плейлисты"
    2. URL страницы содержит /playlist
    3. Заголовок содержит слово "Плейлисты"
    Ожидаемый результат:
    Пользователь находится на странице "Плейлисты"
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.should_be_playlist_page()


@allure.title('TEST: Доступ неавторизованного пользователя к странице /playlist')
@pytest.mark.playlist
def test_playlist_page_unauthorized_user(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу "Плейлист"
    2. URL страницы содержит /playlist
    Ожидаемый результат:
    Неавторизованного пользователя переводят на страницу авторизации"
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.playlist_page_open_by_unauthorized_user()


@allure.title('TEST: Проверка наличия элементов на странице /playlist')
@pytest.mark.playlist
def test_playlist_page_check_elements(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /playlist
    2. Проверка наличия элементов, кнопок и полей на странице /playlist
    Ожидаемый результат:
    Веб-элементы страницы присутствуют"
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.check_menu_buttons()
    page.check_playlist_page_header_buttons()
    page.check_playlist_page_main_area_buttons()


@allure.title('TEST: Клик по кнопкам на странице /playlist')
@pytest.mark.playlist
def test_playlist_page_clickable_buttons(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /playlist
    2. Проверка результата при нажатии на соответствующую кнопку на странице /playlist
    Ожидаемый результат:
    Пользователь попадает в соответствующий раздел меню"
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.check_clickable_menu_buttons()


@allure.title('TEST: Создание пустого плейлиста')
@pytest.mark.playlist
def test_playlist_create_new_playlist_empty(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. URL страницы содержит /playlist
    2. Клик на кнопку Создать плейлист
    3. Клик на кнопку Далее
    4. Клик на кнопку Далее
    5. Клик на кнопку Запустить
    Ожидаемый результат:
    Пустой плейлист не создан. Пользователь остался на странице Новый плейлист
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.create_new_empty_playlist()


@allure.title('TEST: Создание нового плейлиста с валидным данными')
@pytest.mark.playlist
def test_playlist_create_new_playlist_mts_card_maket_1920(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги общие:
    1. URL страницы содержит /playlist
    2. Клик на кнопку Создать плейлист
    Шаг Настроить плейлист:
    3. Клик по чекбоксу разрешение для экрана превью 1920х158
    4. Клик по полю Название плейлиста и ввод 1920x158_mts_lime_maket + текущая_дата
    5. В выпадающем списке Тип плейлиста выбрать Обычный
    6. Клик по полю Тэги и ввод 1920
    7. Клик на кнопку Добавить
    7. Клик на кнопку +Контент выбор в выпадающем списке тип Изображения
    8. Клик по полю Контент для проигрывания и ввод 1920_158_mts.png
    9. Клик на кнопку +Контент выбор типа Видео
    10. Клик по полю Контент для проигрывания и ввод Лайм_1920x158_12sec.mp4
    11. Клик на кнопку +Контент выбор Макет полки
    12. Клик по полю Контент для проигрывания и ввод Макет 1337
    13. Клик по кнопке Далее
    Шаг Выбрать устройства
    14. Клик по списку Малый стенд
    15. Выбрать чекбокс полок CS01_2300314490466
    16. Клик по кнопке Далее
    Шаг График воспроизведения:
    17. Клик на кнопку Ежедневно
    18. Клик на кнопку На весь день
    18. Клик по кнопке Запустить
    Ожидаемый результат:
    Плейлист создан и отображается на странице Плейлисты"
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.create_valid_new_playlist_1920_step_1_customize_playlist()
    page.create_valid_new_playlist_1920_step_2_choose_devices()
    page.create_valid_new_playlist_1920_step_3_play_schedule()


@allure.title('TEST: Предпросмотр плейлиста')
@pytest.mark.playlist
def test_playlist_open_new_playlist_mts_card_maket_1920(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Плейлист 1920x158_mts_lime_maket создан
    Шаги:
    1. Нажать на кнопку открыть плейлист
    Ожидаемый результат:
    Появляется модальное окно с превью плейлиста 1920x158_mts_lime_maket
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.open_playlist_1920_mts_lime_maket()


@allure.title('TEST: Сохранение плейлиста')
@pytest.mark.playlist
def test_playlist_get_video_src_playlist_mts_card_maket_1920(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Плейлист 1920x158_mts_lime_maket создан
    Шаги:
    1. Нажать на кнопку открыть плейлист
    2. Сделать скриншот с превью плейлиста
    3. Получить video src плейлиста
    Ожидаемый результат:
    Появляется модальное окно с превью плейлиста 1920x158_mts_lime_maket. В теле ответа src видео плейлиста
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.get_video_src_playlist_1920_mts_lime_maket()
# парсинг ссылки на плейлист


@allure.title('TEST: Переключение на сеточное отображение и предпросмотр плейлиста')
@pytest.mark.playlist
def test_switch_to_grid_view_and_preview_playlist_mts_card_maket_1920(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе и находится на странице Плейлисты
    Плейлист 1920x158_mts_lime_maket создан
    Шаги:
    1. Нажать на кнопку сеточное отображение
    2. Клик дважды по созданному плейлисту
    3. Получить video src плейлиста
    Ожидаемый результат:
    Появляется модальное окно с превью плейлиста 1920x158_mts_lime_maket. В теле ответа scr видео плейлиста
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.preview_playlist_on_grid_view()


@allure.title('TEST: Получение и проверка ID Плейлиста')
@pytest.mark.playlist
def test_get_playlist_id_and_check_on_edit_page_mts_card_maket_1920(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе и находится на странице Плейлисты
    Плейлист 1920x158_mts_lime_maket создан
    Шаги:
    1. Получить ID плейлиста
    2. Нажать на кнопку изменить плейлист
    Ожидаемый результат:
    ID плейлиста на странице Плейлисты совпадает с ID в URL
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.get_playlist_id_1920_mts_lime_maket()


@allure.title('TEST: Редактирование плейлиста')
@pytest.mark.playlist
def test_playlist_edit_new_playlist_mts_card_maket_1920_add_tag_play_changed(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Плейлист 1920x158_mts_lime_maket создан
    Шаги:
    1. Нажать на кнопку изменить плейлист
    2. Клик по полю Добавьте тэги
    3. Ввод тэга PLAY_CHANGED
    4. Клик по кнопке Добавить
    5. Клик по кнопке Далее (шаг 2)
    6. Клик по кнопке Далее (шаг 3)
    7. Клик по кнопке Запустить
    Ожидаемый результат:
    У плейлиста 1920x158_mts_lime_maket_ поле тэги присутствует тэг PLAY_CHANGED
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.edit_playlist_1920_mts_lime_maket()


@allure.title('TEST: Удаление созданного плейлиста')
@pytest.mark.playlist
def test_delete_playlist_mts_card_maket_1920(browser, test_auth_ui):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Плейлист 1920x158_mts_lime_maket создан
    Шаги:
    1. Нажать на кнопку открыть плейлист
    Ожидаемый результат:
    Появляется модальное окно с превью плейлиста 1920x158_mts_lime_maket
    """
    page = PlaylistPage(browser, playlist_link)
    page.open()
    page.delete_playlist_1920_mts_lime_maket()




