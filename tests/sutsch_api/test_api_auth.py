import requests
import json
import pytest
import allure
from tests.sutsch_api.class_api import Api
from tests.sutsch_ui.config import STAGE_LOGIN_USER_1, STAGE_PASSWORD_USER_1, STAGE_LOGIN_USER_2, STAGE_PASSWORD_USER_2
from tests.sutsch_ui.randomizer_eng import generated_password_eng


@allure.title(f'TEST: Авторизация: валидные данные пользователя {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_post_auth_valid_user_1():
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Отправить POST запрос на авторизацию
    Ожидаемый результат:
    Код ответа 200 Ок
    """
    url = Api.LOGON
    payload = json.dumps({
        "login": STAGE_LOGIN_USER_1,
        "password": STAGE_PASSWORD_USER_1,
        "remember": True
    })
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    cookie_jar = response.cookies
    print(cookie_jar)
    assert response.status_code == 200


@allure.title(f'TEST: Авторизация с неверными данными пользователя {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_post_cookie_invalid_user_1():
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Отправить POST запрос на авторизацию
    Ожидаемый результат:
    Код ответа 400 Неверный логин или пароль
    """
    url = Api.LOGON
    payload = json.dumps({
        "login": STAGE_LOGIN_USER_1,
        "password": generated_password_eng,
        "remember": True
    })
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 400
    assert 'Неверный логин или пароль' in response.text


@allure.title(f'TEST: Получение данных о пользователе {STAGE_LOGIN_USER_1}')
@pytest.mark.api
def test_get_auth_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение данных о пользователе
    Ожидаемый результат:
    Код ответа 200. ID пользователя отображается в теле ответа.
    """
    url = Api.AUTH
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.status_code == 200
    assert '{"id":4' in response.text, f"Wrong user. Must be {STAGE_LOGIN_USER_1}"


@allure.title(f'TEST: Получение данных о пользователе {STAGE_LOGIN_USER_2}')
@pytest.mark.api
def test_get_user_cookie_user_2(test_get_cookie_user_2):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить GET запрос на получение данных о пользователе №2
    Ожидаемый результат:
    Код ответа 200. ID пользователя отображается в теле ответа.
    """
    url = Api.AUTH
    headers = {
        'Cookie': test_get_cookie_user_2
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.status_code == 200
    assert '{"id":3' in response.text, f"Wrong user. Must be {STAGE_LOGIN_USER_2}"


@allure.title(f'TEST: Выход пользователя {STAGE_LOGIN_USER_1} из системы ')
@pytest.mark.api
def test_post_logout_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить POST запрос на выход из системы
    Ожидаемый результат:
    Код ответа 200.
    """
    url = Api.LOGOUT
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers)
    print(response.text)
    assert response.status_code == 200, "Пользователь не вышел из личного кабинета"


@allure.title(f'TEST: Авторизация: валидные данные пользователя {STAGE_LOGIN_USER_2}')
@pytest.mark.api
def test_post_auth_valid_user_2():
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Отправить POST запрос на авторизацию
    Ожидаемый результат:
    Код ответа 200 Ок
    """
    url = Api.LOGON
    payload = json.dumps({
        "login": STAGE_LOGIN_USER_2,
        "password": STAGE_PASSWORD_USER_2,
        "remember": True
    })
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200
    assert '{"id":3}' in response.text


@allure.title(f'TEST: Авторизация: не валидные данные пользователя {STAGE_LOGIN_USER_2}')
@pytest.mark.api
def test_post_auth_invalid_user_2():
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Отправить POST запрос на авторизацию
    Ожидаемый результат:
    Код ответа 400. Неверный логин или пароль в теле ответа.
    """
    url = Api.LOGON
    payload = json.dumps({
        "login": STAGE_LOGIN_USER_2,
        "password": generated_password_eng,
        "remember": True
    })
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 400
    assert 'Неверный логин или пароль' in response.text


@allure.title(f'TEST: Получение данных о пользователе {STAGE_LOGIN_USER_2}')
@pytest.mark.api
def test_get_auth_user_2(test_get_cookie_user_2):
    url = Api.AUTH
    headers = {
        'Cookie': test_get_cookie_user_2
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    assert response.status_code == 200
    assert STAGE_LOGIN_USER_2 in response.text, f"Wrong user. Must be {STAGE_LOGIN_USER_2}"


@allure.title(f'TEST: Выход пользователя {STAGE_LOGIN_USER_2} из системы ')
@pytest.mark.api
def test_post_logout_user_2(test_get_cookie_user_2):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить POST запрос на выход из системы
    Ожидаемый результат:
    Код ответа 200.
    """
    url = Api.LOGOUT
    headers = {
        'Cookie': test_get_cookie_user_2
    }
    response = requests.request("POST", url, headers=headers)
    print(response.text)
    assert response.status_code == 200, "Пользователь не вышел из личного кабинета"


@allure.title(f'TEST: Сброс пароля пользователя {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_post_request_reset_password_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить POST запрос сброс пароля
    Ожидаемый результат:
    Код ответа 200. Письмо отправлено на почту.
    """
    url = Api.RESET_PASSWORD
    payload = json.dumps({
        "login": STAGE_LOGIN_USER_1,
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200, "Запрос на изменение пароля не отправлен на почту"


@allure.title(f'TEST: Смена пароля пользователя {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
@pytest.mark.negative
def test_post_request_change_password_negative_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить POST запрос смену пароля
    Ожидаемый результат:
    Код ответа 400. В теле ответа сообщение "Укажите токен"
    """
    url = Api.CHANGE_PASSWORD
    payload = json.dumps({
        "token": '',
        "password": generated_password_eng
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 400
    assert "Укажите token" in response.text, "В запрос должен передаваться токен из эл.почты"


@allure.title(f'TEST: Смена пароля пользователя по старой ссылке {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
@pytest.mark.negative
def test_post_request_change_password_negative2_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе
    Шаги:
    1. Отправить POST запрос смену пароля
    Ожидаемый результат:
    Код ответа 400. В теле ответа сообщение "Ссылка устарела"
    """
    url = Api.CHANGE_PASSWORD
    payload = json.dumps({
        "token": '249905ea-6d0a-4cc9-9e15-f29359c1e8b2',
        "password": generated_password_eng
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 400
    assert 'Ссылка устарела' in response.text, 'Ссылка для смены пароля срабатывает всего один раз'
