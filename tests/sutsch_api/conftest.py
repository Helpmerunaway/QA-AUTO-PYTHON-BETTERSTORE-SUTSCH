import pytest
import json
import requests

from tests.sutsch_ui.config import STAGE_API, STAGE_LOGIN_USER_1, STAGE_PASSWORD_USER_1, STAGE_LOGIN_USER_2, \
    STAGE_PASSWORD_USER_2, CAT_PATH
from tests.sutsch_api.class_api import Api


@pytest.fixture()
def test_get_cookie_user_1():
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
    jar = str(cookie_jar)
    jar = jar[27:247]
    assert response.status_code == 200
    return jar

@pytest.fixture()
def test_get_cookie_user_2():
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
    cookie_jar = response.cookies
    jar = str(cookie_jar)
    jar = jar[27:247]
    assert response.status_code == 200
    return jar


@pytest.fixture()
def test_create_group(test_get_cookie_user_1):
    url = f'{STAGE_API}v1/group'
    payload = Api.GROUP_PAYLOAD
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    new_group_id = response.text
    group_id = new_group_id[6:10]
    print(group_id)
    assert response.status_code == 200
    return group_id


@pytest.fixture()
def test_delete_group(test_create_group, test_get_cookie_user_1):
    yield
    url = f'{STAGE_API}v1/group/{test_create_group}'
    payload={}
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 200
    assert response.reason == 'OK'


@pytest.fixture()
def test_delete_and_create_group():
    test_create_group_fixture()
    yield
    test_delete_group_fixture()


@pytest.fixture()
def test_create_group_fixture(test_get_cookie_user_1):
    url = f'{STAGE_API}v1/group'
    payload = Api.GROUP_PAYLOAD
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    new_group_id = response.text
    group_id = new_group_id[6:10]
    print(group_id)
    assert response.status_code == 200
    return group_id


@pytest.fixture()
def test_delete_group_fixture(test_create_group_fixture, test_get_cookie_user_1):
    url = f'{STAGE_API}v1/group/{test_create_group_fixture}'
    payload={}
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 200
    assert response.reason == 'OK'

@pytest.fixture()
def test_add_media(test_get_cookie_user_1):
    url = Api.POST_ADD_MEDIA_FILE
    payload = json.dumps({
        "file": CAT_PATH

    })
    headers = {
        'Accept': 'application/json',
        'Cookie': test_get_cookie_user_1
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200


@pytest.fixture()
def test_create_playlist_fixture(test_get_cookie_user_1):
    url = Api.POST_CREATE_PLAYLIST
    payload = Api.PLAYLIST_FIXTURE_PAYLOAD
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    playlist_id = response.text
    print(playlist_id)
    new_playlist_id = playlist_id[6:10]
    assert response.status_code == 200
    assert response.reason == 'OK'
    return new_playlist_id


@pytest.fixture()
def test_delete_playlist_fixture(test_get_cookie_user_1, test_create_playlist_fixture):
    print('Playlist id =', test_create_playlist_fixture)
    url = f'{STAGE_API}v1/playlist/{test_create_playlist_fixture}'
    payload={}
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 200
    assert response.reason == 'OK'
    print(f'Playlist {test_create_playlist_fixture} deleted successfully')


@pytest.fixture()
def test_create_layout_fixture(test_get_cookie_user_1):
    url = Api.POST_CREATE_LAYOUT
    payload = Api.POST_CREATE_LAYOUT_SCHEMA
    headers = {
        'Content-Type': 'application/json',
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    layout_id = response.text
    print(layout_id)
    new_layout_id = layout_id[6:9]
    assert response.status_code == 200
    assert response.reason == 'OK'
    return new_layout_id


@pytest.fixture()
def test_delete_layout_fixture(test_get_cookie_user_1, test_create_layout_fixture):
    print('Layout id =', test_create_layout_fixture)
    url = Api.DELETE_LAYOUT_ID + test_create_layout_fixture
    payload={}
    headers = {
        'Cookie': test_get_cookie_user_1
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 200
    assert response.reason == 'OK'
    print(f'Layout {test_create_layout_fixture} deleted successfully')