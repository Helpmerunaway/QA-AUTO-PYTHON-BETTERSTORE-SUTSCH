import allure
import pytest
import requests
from tests.sutsch_ui.config import STAGE_LOGIN_USER_1
from tests.sutsch_api.class_api import Api


@allure.title(f'TEST: Получить все макеты пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_get_all_layouts_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение всех макетов полок
    Ожидаемый результат:
    Код ответа 200, контент найден в теле ответа.
    """
    url = Api.GET_ALL_LAYOUTS
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert '2880x158' or '3840_160' or '1920x158' in response.text, 'Макеты не найдены'


@allure.title(f'TEST: Получить макет полки пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_get_layout_by_id_user_1(test_get_cookie_user_1, test_create_layout_fixture):
    """
    Предусловия:
    Пользователь авторизован в системе. Плейлист создан.
    Шаги:
    1. Отправить GET запрос на получение макета полки
    Ожидаемый результат:
    Код ответа 200.
    """
    url = Api.GET_LAYOUT_ID + test_create_layout_fixture
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    response_body = response.json
    assert response.status_code == 200, f'ERROR! Status code must be 200 {response_body}'


@allure.title(f'TEST: Создать макет полки пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_post_create_new_layout_user_1(test_get_cookie_user_1, test_delete_layout_fixture):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить POST запрос на создание макета полки
    Ожидаемый результат:
    Код ответа 200, ID макета полки присутствует в теле ответа.
    Teardown:
    Макет удален
    """
    url = Api.POST_CREATE_LAYOUT
    payload = Api.POST_CREATE_LAYOUT_SCHEMA
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    layout_id = response.text
    new_layout_id = layout_id[6:9]
    print(new_layout_id)
    assert response.status_code == 200
    assert response.reason == 'OK'
    return new_layout_id


@allure.title(f'TEST: Удалить плейлист пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_delete_playlist_user_1(test_get_cookie_user_1, test_create_layout_fixture):
    """
    Предусловия:
    Пользователь авторизован в системе. Плейлист создан.
    Шаги:
    1. Отправить DELETE запрос на получение всех плейлистов
    Ожидаемый результат:
    Код ответа 200. Макет полки удален
    """
    print('Playlist id =', test_create_layout_fixture)
    url = Api.DELETE_PLAYLIST + test_create_layout_fixture
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("DELETE", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    print(f'Playlist {test_create_layout_fixture} deleted successfully')


@allure.title(f'TEST: Поиск макета полки по строке пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_search_playlist123_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить GET запрос на поиск макета полки
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует информация о найденном плейлисте
    """
    url = Api.GET_SEARCH_LAYOUT+'1337'
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert '2880x158' or '3840_160' or '1920x158' in response.text, 'Макеты не найдены'


# запрашивает неправильную схему (из плейлистов)
@allure.title(f'TEST: Изменить макет полки пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_put_layout_user_1(test_get_cookie_user_1, test_create_layout_fixture):
    """
    Предусловия:
    Пользователь авторизован в системе. Макет полки создан.
    Шаги:
    1. Отправить PUT запрос на изменение макета полки
    Ожидаемый результат:
    Код ответа 200.
    """
    url = Api.PUT_PLAYLIST + test_create_layout_fixture
    payload = Api.PUT_CHANGE_LAYOUT_SCHEMA
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200, 'Wrong SCHEMA'
    assert '2880x158' or '3840_160' or '1920x158' in response.text, 'Макеты не найдены'


@allure.title(f'TEST: Получить все ценники пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_all_price_tags_from_handbook_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить GET запрос на получение ценников
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует информация о найденных ценниках
    """
    url = Api.GET_LAYOUT_HANDBOOK_PRICE_TAG
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    assert response.reason == 'OK'
    print(response.text)
    assert '296x158px' in response.text, 'Ценники не найдены'