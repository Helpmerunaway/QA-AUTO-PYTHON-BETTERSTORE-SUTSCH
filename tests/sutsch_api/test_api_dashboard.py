import allure
import pytest
import requests
from playlist_name import fixture_playlist_name
from tests.sutsch_ui.config import STAGE_LOGIN_USER_1
from tests.sutsch_api.class_api import Api


@allure.title(f'TEST: Получить данные для дашборда пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_all_dashboard_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить GET запрос на получение данных для дашборда
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует информация об устройствах
    """
    url = Api.GET_ALL_DATA_DASHBOARD
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert 'total' and 'online' and 'offline' in response.text, 'Устройства не найдены'


@allure.title(f'TEST: Получить данные плейлиста для дашборда пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_playlist_dashboard_user_1(test_get_cookie_user_1, test_create_playlist_fixture):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить GET запрос на получение данных плейлиста для дашборда
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует информация об плейлисте
    """
    url = Api.GET_PLAYLIST_ID_DASHBOARD + test_create_playlist_fixture
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert f'{fixture_playlist_name}' in response.text, 'Плейлист не найден'


@allure.title(f'TEST: Получить тэги полок и групп для поиска пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_tags_for_search_by_shelf_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить GET запрос на получение тэгов полок и групп
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует информация об устройствах
    """
    url = Api.GET_DASHBOARD_SEARCH_TAGS
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert 'Amlogic' and 'rockchip' and 'Droidlogic' in response.text, 'Устройства не найдены'