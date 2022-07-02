import allure
import pytest
import requests
from tests.sutsch_ui.config import STAGE_LOGIN_USER_1
from tests.sutsch_api.class_api import Api


@allure.title(f'TEST: Получить все теги пользователем {STAGE_LOGIN_USER_1} ')
@pytest.mark.api
def test_get_all_tags_user_1(test_get_cookie_user_1):
    """
    Предусловия:
    Пользователь авторизован в системе.
    Шаги:
    1. Отправить GET запрос на получение все тегов
    Ожидаемый результат:
    Код ответа 200. В теле ответа присутствует информация об тегах
    """
    url = Api.GET_ALL_TAGS
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    assert response.reason == 'OK'
    assert '1920x158' or '2880x158' or 'fixture' in response.text, 'Теги не найдены'