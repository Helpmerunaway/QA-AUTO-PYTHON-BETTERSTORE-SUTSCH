import allure
import pytest
import requests
import json
from tests.sutsch_ui.config import STAGE_LOGIN_USER_1, STAGE_LOGIN_USER_2
from tests.sutsch_api.class_api import Api


@allure.title(f'TEST: Получение всех групп пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_groups_all_by_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение всех групп
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует "Главный стенд"
    """
    url = Api.GET_ALL_GROUPS
    headers = {'Cookie': test_get_cookie_user_1
               }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert 'Главный стенд' in response.text, 'Главный стенд не найден'


@allure.title(f'TEST: Получение всех групп пользователем {STAGE_LOGIN_USER_2} ')
@pytest.mark.api
def test_get_groups_all_groups_all_user_2(test_get_cookie_user_2):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение всех групп
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует "Главный стенд"
    """
    url = Api.GET_ALL_GROUPS
    headers = {
        'Cookie': test_get_cookie_user_2
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert 'Главный стенд' in response.text, 'Главный стенд не найден'


@allure.title(f'TEST: Создание новой пустой группы пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
@pytest.mark.negative
def test_post_create_group_is_empty_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить POST запрос на создание новой пустой группы
    Ожидаемый результат:
    Код ответа 400. В теле ответа присутствует "Укажите название группы"
    """
    url = Api.POST_GROUP
    payload = {}
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 400
    assert "Укажите название группы" in response.text, "Wrong response. Must be error_text:'Укажите название группы' "


@allure.title(f'TEST: Создание новой группы пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_post_create_new_group_user_1(test_get_cookie_user_1, test_delete_group):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить POST запрос на создание новой группы
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует ID созданной группы
    Teardown:
    Группа удалена.
    """
    url = Api.POST_GROUP
    payload = Api.GROUP_PAYLOAD
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    new_group_id = response.text
    assert response.status_code == 200
    return new_group_id


@allure.title(f'TEST: Получение новой группы пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_new_group_by_user_1(test_get_cookie_user_1, test_create_group):
    """
    Предусловия:
    Пользователь авторизован в системе. Новая группа создана.
    Шаги:
    1. Отправить GET запрос на создание новой группы
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует ID созданной группы
    """
    url = Api.GET_GROUP + test_create_group
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    response_body = response.text
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert test_create_group in response_body
    assert 'Группа Крови' in response_body


@allure.title(f'TEST: Получение новой группы пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
@pytest.mark.skip
def test_get_new_group_by_id_user_1_alternative(test_delete_and_create_group, test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе. Новая группа создана.
    Шаги:
    1. Отправить GET запрос на создание новой группы
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует ID созданной группы
    Teardown:
    Группа удалена.
    """
    url = Api.GET_GROUP + test_delete_and_create_group
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    response_body = response.text
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert test_delete_and_create_group in response_body
    assert 'Группа Крови' in response_body


@allure.title(f'TEST: Удаление новой группы пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_delete_group_user_1(test_get_cookie_user_1, test_create_group):
    """
    Предусловия:
    Пользователь авторизован в системе. Новая группа создана.
    Шаги:
    1. Отправить DELETE запрос на удаление новой группы
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует ID удаленной группы
    """
    print('Delete group id =', test_create_group)
    url = Api.DELETE_GROUP + test_create_group
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("DELETE", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'


@allure.title(f'TEST: Поиск группы по строке пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_search_by_string_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить GET запрос на поиск группы
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует информация о группе
    """
    url = f"{Api.GET_SEARCH_GROUP}нарукаве"
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert "Нарукаве" in response.text, "Wrong response. Must be search phrase presented"


@allure.title(f'TEST: Добавить полку в созданную группу пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_put_add_shelf_and_group_to_group_user_1(test_get_cookie_user_1, test_create_group):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить PUT запрос на добавление полки в группу
    Ожидаемый результат:
    Код ответа 200.
    """
    url = Api.PUT_SHELF_TO_GROUP + test_create_group + '/add_to'
    payload = json.dumps({
        "group_ids": [
            1,
            2
        ],
        "shelf_ids": [
            589,
            428
        ],
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    response_body = response.text
    print(response)
    print(response_body)
    print(response.reason)
    print(response.request)
    print(response.raw)
    assert response.status_code == 200
    assert response.reason == 'OK'


@allure.title(f'TEST: Удалить полки из группы пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_put_remove_group_and_shelf_from_group_user_1(test_get_cookie_user_1, test_create_group):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить PUT запрос на удаление полки из группы
    Ожидаемый результат:
    Код ответа 200.
    """
    url = Api.DELETE_SHELF_OR_GROUP_FROM_GROUP + test_create_group + '/remove_from'
    payload = json.dumps({
        "group_ids": [
            1,
            2
        ],
        "shelf_ids": [
            589,
            428
        ],
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    response_body = response.text
    assert response.status_code == 200
    assert response.reason == 'OK'
