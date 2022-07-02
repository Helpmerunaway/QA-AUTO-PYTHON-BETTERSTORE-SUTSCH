from selenium.webdriver.common.by import By


class MainPageLocators():

    USER_CONTAINER = (By.CSS_SELECTOR,
                      "div[class='UserContainer']")
    SHELF_TALKER_BUTTON = (By.XPATH,
                           "//div[contains(@class, 'Logo')]")
    BETTERSTORE_LOGO = (By.XPATH,
                        "//div[contains(@class, 'BetterstoreLogo')]")
    DASHBOARD_BUTTON = (By.XPATH,
                        "//span[contains(text(), 'Dashboard')]")
    DEVICES_BUTTON = (By.XPATH,
                      "//a[contains(text(), 'Устройства')]")
    MEDIA_BUTTON = (By.XPATH,
                    "//a[contains(text(), 'Медиа')]")
    PLAYLISTS_BUTTON = (By.XPATH,
                        "//a[contains(text(), 'Плейлисты')]")
    LAYOUT_BUTTON = (By.XPATH,
                     "//a[contains(text(), 'Макеты полки')]")
    STATISTIC_BUTTON = (By.XPATH,
                        "//span[contains(text(), 'Статистика')]")
    BELL_BUTTON = (By.XPATH,
                   "//i[contains(@class, 'anticon-bell')]")
    USERNAME = (By.XPATH,
                "//span[contains(@class, 'UserName')]")
    EXIT_USER_BUTTON = (By.XPATH,
                        "//i[contains(@class, 'anticon anticon-export')]")
    LOAD_SPINNER = (By.XPATH,
                    "//span[contains(@class, 'ant-spin-dot')]")


class LoginPageLocators():
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR,
                         "input[type='text'][placeholder='E-mail']")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR,
                            "input[type='password'][placeholder='Пароль']")
    CHECKBOX_REMEMBER_ME = (By.CSS_SELECTOR,
                            "input[class='ant-checkbox-input']")
    REMEMBER_ME_IS_CHECKED = (By.XPATH,
                              "//span[contains(@class, 'ant-checkbox-checked')]")
    PASSWORD_VIEW_BUTTON = (By.XPATH,
                            "//i[contains(@class, 'InputIconMask anticon anticon-eye-invisible')]")
    PASSWORD_VIEW_IS_CHECKED = (By.CSS_SELECTOR,
                                "i[class='InputIconMask anticon anticon-eye']")
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR,
                              "div[class='ForgotPassword']")
    ENTER_STAGE_BUTTON = (By.CSS_SELECTOR,
                          "button[class='Button ant-btn ant-btn-primary']")
    ALERT_MESSAGE_INVALID_LOGIN_OR_PASSWORD = (By.XPATH,
                                               "//span[contains(text(), 'Неверные логин или пароль')]")


class ForgotPasswordPageLocators():
    EMAIL_INPUT = (By.XPATH,
                   "//input[contains(@class, 'ForgotPasswordInput')]")
    RESET_PASSWORD_BUTTON = (By.XPATH,
                             "//button[contains(@class, 'Button ant-btn')]")
    ALERT_WINDOW = (By.XPATH,
                    "//span[contains(@class, 'ant-alert-message')]")
    ALERT_TEXT = (By.XPATH,
                  "//span[contains(text(), 'В течение нескольких минут на адрес')]")


class OutlookPageLocators():
    OUTLOOK_USERNAME_INPUT = (By.XPATH,
                              "//div[contains(@class, 'logonDiv')]//input[contains(@id, 'username')]")
    OUTLOOK_PASSWORD_INPUT = (By.XPATH,
                              "//div[contains(@class, 'logonDiv')]//input[@id='password']")
    OUTLOOK_SIGN_IN = (By.XPATH,
                       "//div[contains(@class, 'signInEnter')]//div[@class='signinbutton']")
    OUTLOOK_SHELF_TALKER_DIR = (By.XPATH,
                                "//span[@title='Shelftalker']")
    OUTLOOK_HYPERLINK = (By.XPATH,
                         "//div[contains(@class, '_lvv_J ms-font-s ms-fwt-sb ms-fcl-tp')]")
    OUTLOOK_USER_MENU = (By.XPATH,
                         "//button[contains(@aria-label, 'Меню Соловьев Руслан Игоревич')]")
    OUTLOOK_USER_NAME = (By.XPATH,
                         "//div[@class='_pe_61']//span[contains(text(), 'Соловьев Руслан Игоревич')]")
    HREF_LINK = (By.XPATH,
                 "//a[contains(@href, 'https://stage.betterstore.tech/ptm/page/change')]")
    OUTLOOK_TITLE = (By.XPATH,
                     "//span[contains(@title, 'Соловьев Руслан Игоревич')]")


class ChangePasswordPageLocators():
    CHANGE_PASSWORD_TITLE = (By.XPATH,
                             "//h2[contains(text(), 'Смена пароля')]")
    NEW_PASSWORD_INPUT = (By.XPATH,
                          "//input[contains(@placeholder, 'Новый пароль')]")
    REPEAT_PASSWORD_INPUT = (By.XPATH,
                             "//input[contains(@placeholder, 'Повторите пароль')]")
    SAVE_PASSWORD_BUTTON = (By.XPATH,
                            "//button[contains(@class, 'ant-btn-primary')]")
    SAVE_PASSWORD_IS_CLICKED = (By.CSS_SELECTOR,
                                'button[ant-click-animating-without-extra-node="true"]')
    ALERT_MESSAGE = (By.CSS_SELECTOR,
                     "div[class='ant-message-notice']")
    ALERT_MESSAGE_TEXT_DONT_MATCH = (By.XPATH,
                                     "//span[contains(text(), 'Пароли не совпадают')]")
    ALERT_MESSAGE_TEXT_TOO_SHORT = (By.XPATH,
                                    "//span[contains(text(), 'Недопустимая длина пароля. Пароль должен содержать не менее 4 символов.')]")
    ALERT_MESSAGE_TEXT_WAS_CHANGED = (By.XPATH,
                                      "//span[contains(text(), 'Пароль успешно изменен')]")

class DevicesPageLocators():
    # DEVICES_HEADERS
    DEVICES_NAME_HEADER = (By.XPATH,
                           "//div[text()='Устройства']")

    # MAIN_AREA

    DEVICES_FOUND_COUNTER = (By.XPATH,
                             "//div[contains(@class, 'DevicesHeader__counter')]")
    ADD_TO_PLAYLIST_BUTTON = (By.XPATH,
                              "//i[contains(@class, 'anticon anticon-plus')]")
    ADD_TO_GROUP_BUTTON = (By.XPATH,
                           "//i[contains(@class, 'anticon anticon-folder')]")
    DELETE_DEVICE_BUTTON = (By.XPATH,
                            "//i[contains(@class, 'anticon anticon-delete')]")
    GRID_VIEW_BUTTON = (By.XPATH,
                        "//i[contains(@class, 'anticon anticon-table')]")    # сеточное отображение
    TABLE_VIEW_BUTTON = (By.XPATH,
                         "//i[contains(@class, 'anticon anticon-menu active')]")
    SEARCH_BY_NAME_INPUT = (By.XPATH,
                            "//input[contains(@class, 'ant-input')]")
    FILTER_BUTTON = (By.XPATH,
                     "//i[contains(@class, 'anticon anticon-filter')]")
    PREVIOUS_PAGE_BUTTON = (By.XPATH,
                            "//i[contains(@class, 'anticon anticon-left')]")
    NEXT_PAGE_BUTTON = (By.XPATH,
                        "//i[contains(@class, 'anticon anticon-right')]")

class MediaPageLocators():
    MEDIA_NAME_HEADER = (By.XPATH,
                         "//div[text()='Медиа']")
    DOWNLOAD_FILES_BUTTON = (By.XPATH,
                             "//button[contains(@class, 'ant-btn-primary')]")
    ONLY_VIDEO_BUTTON = (By.XPATH,
                         "//button[@class='ant-switch']")
    ADD_TO_PLAYLIST_BUTTON = (By.XPATH,
                              "//i[contains(@class, 'anticon anticon-plus')]")
    BLOCKED_DELETE_FILES_BUTTON = (By.XPATH,
                                   "//span[contains(@style, 'display')]//button[contains(@class, 'ant-btn')]")
    ACTIVE_DELETE_FILES_BUTTON2 = (By.XPATH,
                                   "//button[@type='button']//button[@class='ant-btn']")
    ACTIVE_DELETE_FILES_BUTTON3 = (By.XPATH,
                                   "//button[@type='button'][@class='ant-btn']")
    ACTIVE_DELETE_FILES_BUTTON = (By.XPATH,
                                  "//button[@type='button']//i[@class='anticon anticon-delete']")
    DELETE_MEDIA_FILES = (By.XPATH,
                          "//i[contains(@class, 'anticon anticon-delete')]")
    GRID_VIEW_BUTTON = (By.XPATH,
                        "//i[contains(@class, 'anticon-table')]")
    TABLE_VIEW_BUTTON = (By.XPATH,
                         "//i[contains(@class, 'anticon-menu active')]")
    SEARCH_BY_NAME_INPUT = (By.XPATH,
                            "//input[contains(@class, 'ant-input')]")
    FILTER_BUTTON = (By.XPATH,
                     "//i[contains(@class, 'anticon-filter')]")
    CHECKBOX_MEDIA_FILES = (By.XPATH,
                            "//label[contains(@class, 'ant-checkbox-wrapper')]")
    VIEWING_MEDIA_FILES = (By.XPATH,
                           "//span[contains(@class, 'MediafilesTable__action')]")
    PREVIOUS_PAGE_BUTTON = (By.XPATH,
                            "//i[contains(@class, 'anticon-left')]")
    NEXT_PAGE_BUTTON = (By.XPATH,
                        "//i[contains(@class, 'anticon-right')]")
    CHOOSE_FILE_BUTTON = (By.XPATH,
                          "//input[contains(@type, 'file')]")
    DOWNLOAD_BUTTON = (By.XPATH,
                       "//div[contains(@class, 'MediafilesUpload__footer')]//button[contains(@class, 'ant-btn ant-btn-primary')]")
    DOWNLOAD_ON_PAGE = (By.XPATH,
                        "//span[text()='Загрузить']")
    CAT0_PICTURE = (By.XPATH,
                    "//td[text()='cat0']")
    CAT1_PICTURE = (By.XPATH,
                    "//td[text()='cat1']")
    CAT2_PICTURE = (By.XPATH,
                    "//td[text()='cat2']")
    CAT3_PICTURE = (By.XPATH,
                    "//td[text()='cat3']")
    CAT4_PICTURE = (By.XPATH,
                    "//td[text()='cat4']")
    CAT5_PICTURE = (By.XPATH,
                    "//td[text()='cat5']")
    CHECKBOX_CAT0_PICTURE = (By.XPATH,
                             "//tbody[@class='ant-table-tbody']//label[@class='ant-checkbox-wrapper']")
    CHECKBOX_CAT_PICTURE = (By.XPATH,
                            "//tbody[@class='ant-table-tbody']//label[@class='ant-checkbox-wrapper']")
    ARE_YOU_SURE_YES_BUTTON = (By.XPATH,
                               "//button[contains(@class, 'ant-btn ant-btn-primary ant-btn-sm')]")
    CARD_POSTER_LOCATOR = (By.XPATH,
                           "//td[text()='Card_poster_2880x158_Web']")


class PlaylistPageLocators():
    PLAYLIST_NAME_HEADER = (By.XPATH,
                            "//div[text()='Плейлисты']")
    CREATE_PLAYLIST_BUTTON = (By.XPATH,
                              "//button[contains(@class, 'ant-btn-primary')]")
    NEXT_STEP = (By.CSS_SELECTOR,
                 "div [class='NewPlaylist__footer'] :nth-child(2)")
    PREVIOUS_STEP = (By.CSS_SELECTOR,
                     "div [class='NewPlaylist__footer'] :nth-last-child(2)")
    RUN_PLAYLIST = (By.CSS_SELECTOR,
                    "div [class='NewPlaylist__footer'] :nth-child(2)")
    PLAYLIST_NAME_INPUT = (By.XPATH,
                           "//input[@placeholder='Введите название']")
    OPEN_PLAYLIST_BUTTON = (By.CSS_SELECTOR,
                            "div [class='PlaylistTable__action']:nth-child(1)")
    MODAL_BODY_IS_ACTIVE = (By.XPATH,
                            "//div[@class='ant-modal-body']")
    VIDEO_SRC_1920x158_MTS_LIME_MAKET = (By.XPATH,
                                         "//div[@class='ant-modal-body']//video[contains(@src, 'https://cdn.betterstore.tech/rendered-playlist/playlist_')]")
    EDIT_PLAYLIST_BUTTON = (By.CSS_SELECTOR,
                            "span[class='PlaylistTable__action']:nth-child(2)")
    CHECK_NEW_TAG_PLAY_CHANGED = (By.XPATH,
                                  "//span[text()=' PLAY_CHANGED ']")

    DELETE_PLAYLIST_BUTTON = (By.XPATH,
                              "//button[@class='PlaylistHeader__del-btn ant-btn']")
    GRID_VIEW_BUTTON = (By.XPATH,
                        "//i[contains(@class, 'anticon-table')]")
    TABLE_VIEW_BUTTON = (By.XPATH,
                         "//i[contains(@class, 'anticon anticon-menu')]")
    SEARCH_BY_NAME_INPUT = (By.XPATH,
                            "//input[contains(@class, 'ant-input')]")
    FILTER_BUTTON = (By.XPATH,
                     "//i[contains(@class, 'anticon-filter')]")
    CHECKBOX_PLAYLIST = (By.XPATH,
                         "//label[contains(@class, 'ant-checkbox-wrapper')]")
    ACTION_OPEN_PLAYLIST = (By.XPATH,
                            "//span[text()=' Открыть ']")
    ACTION_CHANGE_PLAYLIST = (By.XPATH,
                              "//a[text()='Изменить']")
    PREVIOUS_PAGE_BUTTON = (By.XPATH,
                            "//i[contains(@class, 'anticon-left')]")
    NEXT_PAGE_BUTTON = (By.XPATH,
                        "//i[contains(@class, 'anticon-right')]")
    # STEP_1_CUSTOMIZE_PLAYLIST

    RADIO_BUTTON_SIZE_1920 = (By.CSS_SELECTOR,
                              "input[class='ant-radio-input'][value='s']")
    RADIO_BUTTON_SIZE_2880 = (By.CSS_SELECTOR,
                              "input[class='ant-radio-input'][value='m']")
    RADIO_BUTTON_SIZE_3840 = (By.CSS_SELECTOR,
                              "input[class='ant-radio-input'][value='l']")
    RADIO_BUTTON_IS_CHECKED = (By.XPATH,
                               "//label[@class='ant-radio-wrapper ant-radio-wrapper-checked']")
    ADD_TAG_INPUT = (By.XPATH,
                     "//input[contains(@class, 'ant-select-search__field')]")
    ADD_NEW_TAG_BUTTON = (By.XPATH,
                          "//button[contains(@class, 'ant-btn ant-btn-primary')]")
    TAG_1920 = (By.XPATH,
                "//span[text()=' 1920 ']")
    PLUS_CONTENT_BUTTON = (By.CSS_SELECTOR,
                           "div [class='PlaylistForm__field']:nth-child(4) :nth-last-child(1)")
    PLUS_CONTENT_BUTTON_AFTER_1_ADDED = (By.XPATH,
                                         "//button[@type='button'] [@class='AddedMedia__add-btn ant-btn']")

    CHOOSE_FILE_TYPE_PICTURE = (By.XPATH,
                                "//div[contains(@class, 'PlaylistForm__popover-item')]//i[@class='anticon anticon-picture']")
    CHOOSE_FILE_TYPE_VIDEO = (By.XPATH,
                              "//div[contains(@class, 'PlaylistForm__popover-item')]//i[@class='anticon anticon-video-camera']")
    CHOOSE_FILE_TYPE_LAYOUT = (By.XPATH,
                               "//div[contains(@class, 'PlaylistForm__popover-item')]//i[@class='anticon anticon-layout']")
    NUMBER_OF_ADDED_CONTENT_1 = (By.XPATH,
                                 "//div[@class='AddedMedia']//span[@class='AddedMedia__key'][text()='1.']")
    CONTENT_1_NAME_INPUT = (By.CSS_SELECTOR,
                            "div[class='ant-select-search__field__wrap'] input[placeholder='Начните вводить название']:enabled")
    MTS_1920_PNG_IS_ADDED = (By.CSS_SELECTOR,
                             "input[value='1920_158_mts.png']")
    NUMBER_OF_ADDED_CONTENT_2 = (By.XPATH,
                                 "//div[@class='AddedMedia']//span[@class='AddedMedia__key'][text()='2.']")
    CONTENT_2_NAME_INPUT = (By.CSS_SELECTOR,
                            "div[class='ant-select-search__field__wrap'] input[placeholder='Начните вводить название'][value='']")
    LIME_1920_MP4_IS_ADDED = (By.CSS_SELECTOR,
                              "input[value='Лайм_1920x158_12sec.mp4']")
    NUMBER_OF_ADDED_CONTENT_3 = (By.XPATH,
                                 "//div[@class='AddedMedia']//span[@class='AddedMedia__key'][text()='3.']")
    CONTENT_3_NAME_INPUT = (By.CSS_SELECTOR,
                            "div[class='ant-select-search__field__wrap'] input[placeholder='Начните вводить название'][value='']")
    MAKET_1337_IS_ADDED = (By.CSS_SELECTOR,
                           "input[value='Макет 1337']")
    RENDER_BUTTON = (By.XPATH,
                     "//div[contains(@class, 'PlaylistPlayer__render-button')]")
    SIDE_MENU_FILE_TYPE = (By.XPATH,
                           "//div[contains(@class, 'ant-popover-inner-content')]")
    LOAD_SPINNER = (By.XPATH,
                    "//span[@class='ant-spin-dot ant-spin-dot-spin']")

    # STEP_2_CHOOSE_DEVICES

    UNCOVER_GROUP_SMALL_STAND = (By.CSS_SELECTOR,
                                 "tr[class='ant-table-row ant-table-row-level-0']:nth-child(3) div[class='ant-table-row-expand-icon ant-table-row-collapsed']")
    PRESS_TO_COVER_GROUP_SMALL_STAND = (By.XPATH,
                                        "//div[@class='ant-table-row-expand-icon ant-table-row-expanded']")
    FIND_DEVICES_INPUT = (By.XPATH,
                          "//input[@placeholder='Поиск устройств']")
    UNDONE_CHECKBOX_SMALL_SHELF_2300314490466 = (By.CSS_SELECTOR,
                                                 "tr[class='ant-table-row ant-table-row-level-1'] label[class='ant-checkbox-wrapper'] span[class='ant-checkbox-inner'] ")
    CHECKBOX_SMALL_SHELF_2300314490466 = (By.CSS_SELECTOR,
                                          "tr[data-row-key='303'] input[class='ant-checkbox-input']")
    CHECKBOX_SMALL_SHELF_2300314490466_IS_CHECKED = (By.XPATH,
                                                     "//label[contains(@class, 'ant-checkbox-wrapper ant-checkbox-wrapper-checked')]")
    CHECKBOX_FIRST_ROW_PLAYLIST = (By.CSS_SELECTOR,
                                   "tr[class='ant-table-row ant-table-row-level-0'] label :nth-child(1)")
    CHECKBOX_FIRST_ROW_PLAYLIST_IS_CHECKED = (By.XPATH,
                                              "//span[@class='ant-checkbox ant-checkbox-checked']")



    # STEP_3_SCHEDULE

    CALENDAR_SCHEDULE = (By.XPATH,
                         "//span[@class='PlaylistThirdStep__timePicker ant-calendar-picker']")
    CALENDAR_BODY_CONTAINER = (By.XPATH,
                               "//div[contains(@class, 'ant-calendar ant-calendar-range ant-calendar-picker-container-content')]")
    PLAY_EVERYDAY_CHECKBOX = (By.XPATH,
                              "//label[contains(@class, 'PlaylistThirdStep__daily')]//input[contains(@class, 'ant-checkbox-input')]")
    PLAY_EVERYDAY_CHECKBOX_IS_CHECKED = (By.XPATH,
                                         "//label[contains(@class, 'PlaylistThirdStep__daily ant-checkbox-wrapper ant-checkbox-wrapper-checked')]")
    ALL_DAY_LONG_CHECKBOX = (By.XPATH,
                             "//label[contains(@class, 'PlaylistThirdStep__full ant-checkbox-wrapper')]//input[contains(@class, 'ant-checkbox-input')]")
    ALL_DAY_LONG_CHECKBOX_IS_CHECKED = (By.XPATH,
                                        "//label[contains(@class, 'PlaylistThirdStep__full ant-checkbox-wrapper')]//span[contains(@class, 'ant-checkbox ant-checkbox-checked')]")

    PLAYLIST_NAME_1920x158_MTS_LIME_MAKET_IS_PRESENTED = (By.XPATH,
                                                          "//span[contains(text(), '1920x158_mts_lime_maket')]")
    TAG_NAME_PLAY_CHANGED_IS_PRESENTED = (By.XPATH,
                                          "//span[text()='PLAY_CHANGED']")
    ARE_YOU_SURE_YES_BUTTON = (By.XPATH,
                               "//button[contains(@class, 'ant-btn ant-btn-primary ant-btn-sm')]")
    PLAYLIST_PREVIEW_BUTTON = (By.XPATH,
                               "//div[contains(@class, 'PlaylistCard-body')]")
    PLAYLIST_ID_ROW_KEY = (By.CSS_SELECTOR,
                           "tr[class='ant-table-row ant-table-row-level-0']")
    SOURCE_SRC = (By)

class LayoutPageLocators():

    CREATE_LAYOUT_BUTTON = (By.CSS_SELECTOR,
                            "button[class='ant-btn ant-btn-primary']")
    USED_SWITCHER = (By.XPATH,
                     "//div[contains(@class, 'MediafilesHeader__group')]//button[contains(@class, 'ant-switch')]")
    BLOCKED_DELETE_LAYOUT_BUTTON = (By.XPATH,
                                    "//span[contains(@style, 'display')]//button[contains(@class, 'ant-btn')]")
    ACTIVE_DELETE_LAYOUT_BUTTON = (By.XPATH,
                                   "//button[@type='button']//i[@class='anticon anticon-delete']")
    GRID_VIEW_BUTTON = (By.XPATH,
                        "//i[contains(@class, 'anticon anticon-table')]")
    TABLE_VIEW_BUTTON = (By.XPATH,
                         "//i[contains(@class, 'anticon anticon-menu active')]")
    SEARCH_BY_NAME_INPUT = (By.XPATH,
                            "//input[contains(@class, 'ant-input')]")
    FILTER_BUTTON = (By.XPATH,
                     "//i[contains(@class, 'anticon anticon-filter')]")
    PREVIOUS_PAGE_BUTTON = (By.XPATH,
                            "//i[contains(@class, 'anticon anticon-left')]")
    NEXT_PAGE_BUTTON = (By.XPATH,
                        "//i[contains(@class, 'anticon anticon-right')]")
    ACTION_OPEN_LAYOUT = (By.XPATH,
                          "//span[text()=' Открыть ']")
    ACTION_CHANGE_LAYOUT = (By.XPATH,
                            "//a[text()='Изменить']")
    MODAL_WINDOW = (By.XPATH,
                    "//div[@class='ant-modal-content']")
    EXIT_MODAL_WINDOW = (By.XPATH,
                         "//div[@class='ant-modal-content']//button[@class='ant-modal-close']")
    PLUS_ESL_BUTTON = (By.CSS_SELECTOR,
                       "div [class='LayoutFormField'] button[class='ant-btn'] :nth-child(2)")
    SAVE_LAYOUT_BUTTON = (By.CSS_SELECTOR,
                          "div [class='LayoutRow'] button[class='ant-btn']:nth-last-child(1) span:nth-child(1)")
    LAYOUT_NAME_INPUT = (By.CSS_SELECTOR,
                         "div [class='LayoutFormField'] input[type='input']")
    CHOOSE_ESL_TEMPLATE = (By.CSS_SELECTOR,
                           "div[class='LayoutFormField'] div[role='combobox'] i[class='anticon anticon-down ant-select-arrow-icon']")
    ONE_ESL_DROPDOWN = (By.CSS_SELECTOR,
                        "li[class='ant-select-dropdown-menu-item ant-select-dropdown-menu-item-active']")
    ESL_TEMPLATE_IS_ADDED = (By.CSS_SELECTOR,
                             "div[title='ценник 1']")
    NUMBER_OF_ESL_TEMPLATE = (By.CSS_SELECTOR,
                              "input[class='ant-input-number-input']")
    VALUE_OF_ESLS_NUMBER_11 = (By.CSS_SELECTOR,
                               "input[aria-valuenow='11']")
    ADD_ESL_TO_LAYOUT = (By.XPATH,
                         "//div[@class='LayoutFormField']//span[contains(text(), 'Ценник')]")
    VALUE_OF_ESLS_NUMBER_1 = (By.CSS_SELECTOR,
                              "input[aria-valuenow='1']")
    CHOOSE_ESL_TEMPLATE_SECOND = (By.CSS_SELECTOR,
                                  "div[class='LayoutFormField'] div[aria-controls='92e899f1-4404-4dea-92bb-ceb48c7a32cc']")
    CHOOSE_SOME_SHEAT = (By.CSS_SELECTOR,
                         "div[class='ant-select-selection ant-select-selection--single'] ")
    ADD_TAG_INPUT = (By.XPATH,
                     "//div[@class='ant-select-search__field__wrap']//input[@placeholder='Добавьте тэги']")
    ADD_TAG_BUTTON = (By.XPATH,
                      '//button[@class="ant-btn ant-btn-primary"]')
    MUST_BE_NEW_TAG_VALUE = (By.XPATH,
                             "//span[contains(text(), ' new_maket ')]")
    MAKET_IS_PRESENTED = (By.XPATH,
                          "//span[contains(text(), 'Maket ')]")
    WRAPPER_BODY_IS_PRESENTED = (By.XPATH,
                                 "//div[@class='ant-drawer-wrapper-body']")
    LAYOUT_NAME_IS_PRESENTED = (By.XPATH,
                                "//div[@class='ant-drawer-title'][contains(text(), 'Maket ')]")
    MUST_BE_MODIFIED_VALUE = (By.XPATH,
                              "//span[contains(text(), 'MODIFIED')]")
    CHECKBOXED_TOP_LAYOUT = (By.XPATH,
                             "//tbody[@class='ant-table-tbody']//label[@class='ant-checkbox-wrapper']")
    ARE_YOU_SURE_YES_BUTTON = (By.XPATH,
                               "//button[contains(@class, 'ant-btn ant-btn-primary ant-btn-sm')]")
