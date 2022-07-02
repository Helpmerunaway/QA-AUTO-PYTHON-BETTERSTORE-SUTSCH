import allure
import pytest
import requests
import json
from tests.sutsch_ui.config import STAGE_API, CAT_PATH, STAGE_LOGIN_USER_1
from tests.sutsch_api.class_api import Api


@allure.title(f'TEST: Получить все медиа файлы пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_get_media_files_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение медиа-файлов
    Ожидаемый результат:
    Код ответа 200, контент найден в теле ответа.
    """
    url = Api.GET_MEDIA_FILES
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert 'Клубника' in response.text, 'Контент не найден'
    assert 'Syoss' in response.text, 'Контент не найден'


@allure.title(f'TEST: Добавить медиа файл (негативный) пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_post_add_media_files_negative_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить POST запрос на добавление медиа-файлов
    Ожидаемый результат:
    Код ответа 400.
    """
    url = Api.POST_ADD_MEDIA_FILE
    payload = json.dumps({
        "file1": CAT_PATH
    })
    headers = {
        'Accept': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 400
    assert 'Файл не может быть больше 50' in response.text


@allure.title(f'TEST: Удалить медиа файл пользователем {STAGE_LOGIN_USER_1}')
@pytest.mark.api
@pytest.mark.skip
def test_delete_media_file_user_1(test_add_media, test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить DELETE запрос на удаление медиа-файлов
    Ожидаемый результат:
    Код ответа 200. Файл удален
    """
    url = f'{STAGE_API}v1/media{test_add_media}'
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("DELETE", url, headers=headers)
    assert response.status_code == 200

