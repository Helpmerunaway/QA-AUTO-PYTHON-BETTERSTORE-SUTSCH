import json
import logging
import random
from current_date_and_time import current_date, current_time_with_sec, current_time
from playlist_name import playlist_name, fixture_playlist_name
from tests.sutsch_ui.config import STAGE_API
from tomorrow_date_and_time import mid


class Api:
    LOGGER = logging.getLogger(__name__)

    # AUTH
    LOGON = STAGE_API + 'v1/auth/logon'
    AUTH = STAGE_API + 'v1/auth'
    LOGOUT = STAGE_API + 'v1/auth/logout'
    RESET_PASSWORD = STAGE_API + 'v1/auth/request_reset_password'
    CHANGE_PASSWORD = STAGE_API + 'v1/auth/change_password'

    # GROUP
    GET_ALL_GROUPS = STAGE_API + 'v1/group'
    POST_GROUP = STAGE_API + 'v1/group'
    GET_GROUP = STAGE_API + 'v1/group/'
    PUT_GROUP = STAGE_API + 'v1/group/'
    DELETE_GROUP = STAGE_API + 'v1/group/'
    GET_SEARCH_GROUP = STAGE_API + 'v1/group/search/'
    PUT_SHELF_TO_GROUP = STAGE_API + 'v1/group/'
    DELETE_SHELF_OR_GROUP_FROM_GROUP = STAGE_API + 'v1/group/'

    # SHELF
    GET_ALL_SHELF_WITHOUT_GROUP = STAGE_API + 'v1/shelf/without_group'
    GET_ALL_SHELF_WITH_ERROR = STAGE_API + 'v1/shelf/with_status/error'
    GET_SHELF = STAGE_API + 'v1/shelf/'
    PUT_UPDATE_SHELF = STAGE_API + 'v1/shelf'

    # MEDIA
    GET_MEDIA_FILES = STAGE_API + 'v1/media'
    POST_ADD_MEDIA_FILE = STAGE_API + 'v1/media'
    DELETE_MEDIA_FILE = STAGE_API + 'v1/media'

    # PLAYLIST
    GET_ALL_PLAYLISTS = STAGE_API + 'v1/playlist'
    POST_CREATE_PLAYLIST = STAGE_API + 'v1/playlist'
    GET_RENDERED_PREVIEW = STAGE_API + 'v1/playlist/render'
    POST_RENDER_PLAYLIST = STAGE_API + 'v2/playlist'
    GET_SEARCH_PLAYLIST = STAGE_API + 'v1/playlist/search/'
    POST_CHECK_INTERSECTION = STAGE_API + 'v1/playlist/intersection'
    GET_PLAYLIST = STAGE_API + 'v1/playlist/'
    PUT_PLAYLIST = STAGE_API + 'v1/playlist/'
    DELETE_PLAYLIST = STAGE_API + 'v1/playlist/'
    GET_PLAYLIST_IMAGE = STAGE_API + 'v1/playlist/handbook/image'
    GET_PLAYLIST_VIDEO = STAGE_API + 'v1/playlist/handbook/video'
    GET_PLAYLIST_LAYOUT = STAGE_API + 'v1/playlist/handbook/layout'

    # LAYOUT
    GET_ALL_LAYOUTS = STAGE_API + 'v1/layout'
    POST_CREATE_LAYOUT = STAGE_API + 'v1/layout'
    GET_SEARCH_LAYOUT = STAGE_API + 'v1/layout/search/'
    GET_LAYOUT_ID = STAGE_API + 'v1/layout/'
    PUT_LAYOUT_ID = STAGE_API + 'v1/layout/'
    DELETE_LAYOUT_ID = STAGE_API + 'v1/layout/'
    GET_LAYOUT_HANDBOOK_PRICE_TAG = STAGE_API + 'v1/layout/handbook/price_tag'

    # DASHBOARD
    GET_ALL_DATA_DASHBOARD = STAGE_API + 'v1/dashboard'
    GET_PLAYLIST_ID_DASHBOARD = STAGE_API + 'v1/dashboard/playlist/'
    GET_DASHBOARD_SEARCH_TAGS = STAGE_API + 'v1/dashboard/tags_for_search_by_shelfs'


    # TAGS
    GET_ALL_TAGS = STAGE_API + 'v1/tag'



    # PAYLOADS SCHEMAS

    # CREATE_GROUP
    GROUP_PAYLOAD = json.dumps({
        "name": "Группа Крови",
        "tags": [
            "На рукаве"
        ],
        "group_ids": [
            1,
            2
        ],
        "shelf_ids": [
            1,
            2
        ],
        "description": "Твой порядковый номер"
    })

    # CREATE_PLAYLIST
    PLAYLIST_PAYLOAD = json.dumps({
        "name": playlist_name,
        "type": "ordinary",
        "screensize": "2880x158",
        "tags": [
            "AUTO",
            "TEST"
        ],
        "content": [
            {
                "id": 213,
                "type": "image",
                "duration": "00:15",
            },
            {
                "id": 343,
                "type": "video",
                "duration": "00:15"
            },
            {
                "id": 49,
                "type": "layout",
                "duration": "00:15"
            }
        ],
        "schedule": [
            {
                "start_date": current_date,
                "end_date": current_date,
                "start_time": current_time,
                "end_time": current_time,
                "days_of_week": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ]
            }
        ],
        "group_ids": [
            895
        ],
        "shelf_ids": [
            304,
            315,
            316

        ],
        "save_as_draft": True
    })

    # CREATE_PLAYLIST_FIXTURE
    PLAYLIST_FIXTURE_PAYLOAD = json.dumps({
        "name": fixture_playlist_name,
        "type": "ordinary",
        "screensize": "2880x158",
        "tags": [
            "AUTO",
            "TEST"
        ],
        "content": [
            {
                "id": 213,
                "type": "image",
                "duration": "00:15",
            },
            {
                "id": 343,
                "type": "video",
                "duration": "00:15"
            },
            {
                "id": 49,
                "type": "layout",
                "duration": "00:15"
            }
        ],
        "schedule": [
            {
                "start_date": current_date,
                "end_date": current_date,
                "start_time": mid,
                "end_time": mid,
                "days_of_week": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ]
            }
        ],
        "group_ids": [
            895
        ],
        "shelf_ids": [
            304,
            315,
            316

        ],
        "save_as_draft": True
    })

    # PUT_CHANGE_PLAYLIST
    PUT_CHANGE_PLAYLIST = json.dumps({
        "name": playlist_name,
        "type": "ordinary",
        "screensize": "2880x158",
        "tags": [
            "NEW",
            "TAG"
        ],
        "content": [
            {
                "id": 213,
                "type": "image",
                "duration": "00:15",
            },
            {
                "id": 343,
                "type": "video",
                "duration": "00:15"
            },
            {
                "id": 49,
                "type": "layout",
                "duration": "00:15"
            }
        ],
        "schedule": [
            {
                "start_date": current_date,
                "end_date": current_date,
                "start_time": current_time,
                "end_time": current_time,
                "days_of_week": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ]
            }
        ],
        "group_ids": [
            895
        ],
        "shelf_ids": [
            304,
            315,
            316

        ],
        "save_as_draft": True
    })

    # GET RENDER PREVIEW
    GET_PLAYLIST_RENDER_PREVIEW = json.dumps({
        "screensize": "2880x158",
        "content": [
            {
                "id": 213,
                "type": "image",
                "duration": "00:15",
            },
            {
                "id": 343,
                "type": "video",
                "duration": "00:15"
            },
            {
                "id": 49,
                "type": "layout",
                "duration": "00:15"
            }
        ]
    })

    # CREATE_LAYOUT
    POST_CREATE_LAYOUT_SCHEMA = json.dumps({
        "name": playlist_name,
        "price_tags": [
            {
                "id": 1,
                "number": 2
            }
        ],
        "screensize": "1920x158",
        "tags": [
            "Напитки из Черноголовки",
            "Пейте без остановки"
        ]
    })
    # CHANGE_LAYOUT
    PUT_CHANGE_LAYOUT_SCHEMA = json.dumps({
        "name": "Макет 1",
        "price_tags": [
            {
                "id": 5,
                "number": 2
            }
        ],
        "screensize": "1920x158",
        "tags": [
            "КокаКола",
            "Москва"
        ],
    })
