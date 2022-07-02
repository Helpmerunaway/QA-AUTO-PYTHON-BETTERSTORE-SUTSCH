import allure
import pytest
import requests
import json
from tests.sutsch_ui.config import STAGE_LOGIN_USER_1
from tests.sutsch_api.class_api import Api


@allure.title(f'TEST: Получить все плейлисты пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_get_all_playlists_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение всех плейлистов
    Ожидаемый результат:
    Код ответа 200, контент найден в теле ответа.
    """
    url = Api.GET_ALL_GROUPS
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert '2880x158' or '3840_160' or '1920x158' in response.text, 'Плейлисты не найдены'


@allure.title(f'TEST: Получить плейлист пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_get_playlist_by_id_user_1(test_get_cookie_user_1, test_create_playlist_fixture):
    """
    Предусловия:
    Пользователь авторизован в системе. Плейлист создан.
    Шаги:
    1. Отправить POST запрос на получение рендера превью плейлиста
    Ожидаемый результат:
    Код ответа 200.
    """
    url = Api.GET_PLAYLIST + test_create_playlist_fixture
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    response_body = response.json
    assert response.status_code == 200, f'ERROR! Status code must be 200 {response_body}'


@allure.title(f'TEST: Создать плейлист пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_post_create_new_playlist_user_1(test_get_cookie_user_1, test_delete_playlist_fixture):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить POST запрос на создание плейлиста
    Ожидаемый результат:
    Код ответа 200, ID плейлиста присутствует в теле ответа.
    Teardown:
    Плейлист удален
    """
    url = Api.POST_CREATE_PLAYLIST
    payload = Api.PLAYLIST_PAYLOAD
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    playlist_id = response.text
    print(playlist_id)
    assert response.status_code == 200
    assert response.reason == 'OK'
    return playlist_id


@allure.title(f'TEST: Удалить плейлист пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_delete_playlist_user_1(test_get_cookie_user_1, test_create_playlist_fixture):
    """
    Предусловия:
    Пользователь авторизован в системе. Плейлист создан.
    Шаги:
    1. Отправить DELETE запрос на получение всех плейлистов
    Ожидаемый результат:
    Код ответа 200, ID плейлиста присутствует в теле ответа.
    Teardown:
    Плейлист удален
    """
    print('Playlist id =', test_create_playlist_fixture)
    url = Api.DELETE_PLAYLIST + test_create_playlist_fixture
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("DELETE", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    print(f'Playlist {test_create_playlist_fixture} deleted successfully')


@allure.title(f'TEST: Изменить плейлист пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
@pytest.mark.negative
def test_put_playlist_negative_user_1(test_get_cookie_user_1, test_create_playlist_fixture):
    """
    Предусловия:
    Пользователь авторизован в системе. Плейлист создан.
    Шаги:
    1. Отправить PUT запрос на изменение плейлиста
    Ожидаемый результат:
    Код ответа 400. В теле ответа сообщение "Валидные значения для sreensize...
    """
    url = Api.PUT_PLAYLIST + test_create_playlist_fixture
    payload = json.dumps({
        "name": "Группа Водки"
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    assert response.status_code == 400
    assert 'Валидные значения для sreensize: \\"1920x158\\", \\"2880x158\\", \\"3840x160\\' in response.text


@allure.title(f'TEST: Изменить плейлист пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_put_playlist_user_1(test_get_cookie_user_1, test_create_playlist_fixture):
    """
    Предусловия:
    Пользователь авторизован в системе. Плейлист создан.
    Шаги:
    1. Отправить PUT запрос на изменение плейлиста
    Ожидаемый результат:
    Код ответа 200.
    """
    url = Api.PUT_PLAYLIST + test_create_playlist_fixture
    payload = Api.PUT_CHANGE_PLAYLIST
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200


@allure.title(f'TEST: Получить рендер превью плейлиста пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_get_playlist_render_preview(test_get_cookie_user_1, test_create_playlist_fixture):
    """
    Предусловия:
    Пользователь авторизован в системе. Плейлист создан.
    Шаги:
    1. Отправить POST запрос на получение рендера превью плейлиста
    Ожидаемый результат:
    Код ответа 200.
    """
    url = Api.POST_RENDER_PLAYLIST + test_create_playlist_fixture
    payload = Api.GET_PLAYLIST_RENDER_PREVIEW
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    response_body = response.json
    assert response.status_code == 200, f'ERROR! Status code must be 200 {response_body}'
    assert response.reason == f'OK, ERROR! Reason must be OK {response.reason}'


@allure.title(f'TEST: Поиск плейлиста по строке пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_search_playlist123_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить GET запрос на поиск плейлиста
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует информация о найденном плейлисте
    """
    url = Api.GET_SEARCH_PLAYLIST+'NEW'
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert '2880x158' or '3840_160' or '1920x158' in response.text, 'Плейлисты не найдены'


@allure.title(f'TEST: Получить все изображения плейлистов пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_all_images_from_handbook_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить GET запрос на получение изображений плейлистов
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует информация о найденных изображениях
    """
    url = Api.GET_PLAYLIST_IMAGE
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert '2880x158' or '3840_160' or '1920x158' in response.text, 'Изображения не найдены'


@allure.title(f'TEST: Получить все видео плейлистов пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_all_video_from_handbook_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить GET запрос на получение видео плейлистов
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует информация о найденных видео
    """
    url = Api.GET_PLAYLIST_VIDEO
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert '2880x158' or '3840_160' or '1920x158' in response.text, 'Видео не найдены'


@allure.title(f'TEST: Получить все макеты полок плейлистов пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_all_layout_from_handbook_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить GET запрос на получение макетов полок плейлистов
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует информация о найденных макетах
    """
    url = Api.GET_PLAYLIST_LAYOUT
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert '2880x158' or '3840_160' or '1920x158' in response.text, 'Видео не найдены'
