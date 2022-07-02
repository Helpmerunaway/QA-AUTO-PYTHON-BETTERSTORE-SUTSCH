import allure
import pytest
import requests
import json

from playlist_name import playlist_name
from tests.sutsch_api.class_api import Api
from tests.sutsch_ui.config import STAGE_LOGIN_USER_1
from tests.sutsch_ui.randomizer_eng import generated_password_eng, generated_password_rus


@allure.title(f'TEST: Получить все полки пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_get_shelf_without_group_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение всех полок
    Ожидаемый результат:
    Код ответа 200, полки найдены в теле ответа.
    """
    url = Api.GET_ALL_SHELF_WITHOUT_GROUP
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert '"id":302' or '"id":305' or '"id":307' in response.text


@allure.title(f'TEST: Получить все полки с ошибками пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_get_shelf_with_status_error_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение всех полок с ошибками
    Ожидаемый результат:
    Код ответа 200, полки найдены в теле ответа.
    """
    url = Api.GET_ALL_SHELF_WITH_ERROR
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'


@allure.title(f'TEST: Получить полку 302 пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_get_shelf_302(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение полки 302
    Ожидаемый результат:
    Код ответа 200, полка найдена в теле ответа.
    """
    url = Api.GET_SHELF + '302'
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert "B0:02:47:28:6D:86" in response.text, "Wrong response. Mac address must be B0:02:47:28:6D:86"


@allure.title(f'TEST: Получить полку 1444 пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
@pytest.mark.negative
def test_get_shelf_1444_negative_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение полки 1444
    Ожидаемый результат:
    Код ответа 400, полки не существует.
    """
    url = Api.GET_SHELF + '1444'
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    assert response.reason == 'Bad Request'
    assert "Нет полки с id = 1444" in response.text, "Wrong response. Must be: Нет полки с таким id"


@allure.title(f'TEST: Получить полку 327 пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_get_shelf_327_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение полки 327
    Ожидаемый результат:
    Код ответа 200, полка найдена в теле ответа.
    """
    url = Api.GET_SHELF + '327'
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert "A0:9F:10:2D:F1:32" in response.text, "Wrong response. Mac address must be A0:9F:10:2D:F1:32"


@allure.title(f'TEST: Изменить полку 327 пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_put_update_shelf_327_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить PUT запрос на изменение полки 327
    Ожидаемый результат:
    Код ответа 200, полка найдена в теле ответа.
    """
    url = Api.GET_SHELF + '327'
    payload = json.dumps({
        "name": str(playlist_name),
        "tags": [
            str(generated_password_eng),
            str(generated_password_rus)
        ],
        "description": "Полка у колбасы"
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200
    assert response.reason == 'OK'

