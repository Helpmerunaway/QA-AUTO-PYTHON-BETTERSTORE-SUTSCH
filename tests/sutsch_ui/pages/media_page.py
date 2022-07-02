from selenium.webdriver.common.action_chains import ActionChains
from tests.sutsch_ui.pages.base_page import BasePage
import time
from tests.sutsch_ui.pages.locators import MainPageLocators
from tests.sutsch_ui.pages.locators import MediaPageLocators
from allure_commons._allure import step
from tests.sutsch_ui.config import CAT_PATH, CAT1_PATH, CAT2_PATH, CAT3_PATH, CAT4_PATH, CAT5_PATH


class MediaPage(BasePage):

    def should_be_media_page(self):
        step1_title = "В URL адресе должен присутствовать /media"
        with step(step1_title):
            self.should_be_media_url()
        step2_title = "Должна быть открыта страница Медиа"
        with step(step2_title):
            self.should_be_media_page_open()

    def should_be_media_url(self):
        assert 'media' in self.browser.current_url, \
            "URL is not valid. Should be media page"

    def should_be_media_page_open(self):
        assert 'Медиа' in self.browser.title, \
            "This is not a media page"

    def media_page_open_by_unauthorized_user(self):
        step1_title = "Неавторизованный пользователь видит страницу авторизации"
        with step(step1_title):
            self.when_unauthorized_user_opens_media_page()

    def when_unauthorized_user_opens_media_page(self):
        assert self.is_element_present(*MainPageLocators.BETTERSTORE_LOGO), \
            "Betterstore logo is not presented"
        assert 'auth' in self.browser.current_url, \
            "URL is not valid. Should be media page"

    def check_menu_buttons(self):
        # menu
        step1_title = "Кнопка ShelfTalker присутствует на странице"
        with step(step1_title):
            self.should_be_shelf_talker_button()
        step2_title = "Кнопка Dashboard присутствует на странице"
        with step(step2_title):
            self.should_be_dashboard_button()
        step3_title = "Кнопка Устройства присутствует на странице"
        with step(step3_title):
            self.should_be_devices_button()
        step4_title = "Кнопка Медиа присутствует на странице"
        with step(step4_title):
            self.should_be_media_button()
        step5_title = "Кнопка Плейлисты присутствует на странице"
        with step(step5_title):
            self.should_be_playlists_button()
        step6_title = "Кнопка Макеты полки присутствует на странице"
        with step(step6_title):
            self.should_be_layout_button()
        step7_title = "Кнопка Статистика присутствует на странице"
        with step(step7_title):
            self.should_be_statistic_button()

    def should_be_shelf_talker_button(self):
        assert self.is_element_present(*MainPageLocators.SHELF_TALKER_BUTTON), \
            "Shelftalker button is not presented"

    def should_be_dashboard_button(self):
        assert self.is_element_present(*MainPageLocators.DASHBOARD_BUTTON), \
            "Dashboard button is not presented"

    def should_be_devices_button(self):
        assert self.is_element_present(*MainPageLocators.DEVICES_BUTTON), \
            "Devices button is not presented"

    def should_be_media_button(self):
        assert self.is_element_present(*MainPageLocators.MEDIA_BUTTON), \
            "Media button is not presented"

    def should_be_playlists_button(self):
        assert self.is_element_present(*MainPageLocators.PLAYLISTS_BUTTON), \
            "Playlists button is not presented"

    def should_be_layout_button(self):
        assert self.is_element_present(*MainPageLocators.LAYOUT_BUTTON), \
            'Layout button is not presented'

    def should_be_statistic_button(self):
        assert self.is_element_present(*MainPageLocators.STATISTIC_BUTTON), \
            'Statistic button is not presented'

    def check_media_page_header_buttons(self):
        step1_title = "Заголовок Медиа присутствует на странице"
        with step(step1_title):
            self.should_be_media_name_page_headline()
        step2_title = "Кнопка колокольчик присутствует на странице"
        with step(step2_title):
            self.should_be_bell_button()
        step3_title = "Имя пользователя присутствует на странице"
        with step(step3_title):
            self.should_be_username_on_page()
        step4_title = "Должна присутствовать кнопка Выход"
        with step(step4_title):
            self.should_be_exit_user_button()

    def should_be_username_on_page(self):
        assert self.is_element_present(*MainPageLocators.USERNAME), \
            "Username is not presented"

    def should_be_bell_button(self):
        assert self.is_element_present(*MainPageLocators.BELL_BUTTON), \
            "Bell button is not presented"

    def should_be_media_name_page_headline(self):
        assert self.is_element_present(*MediaPageLocators.MEDIA_NAME_HEADER), \
            "Header text Медиа is not presented"

    def should_be_exit_user_button(self):
        assert self.is_element_present(*MainPageLocators.EXIT_USER_BUTTON), \
            "Exit user button is presented"

    def check_media_page_main_area_buttons(self):
        # main_area
        step1_title = "Кнопка Загрузить файлы присутствует на странице"
        with step(step1_title):
            self.should_be_download_files_button_found()
        step2_title = "Кнопка Только видео присутствует на странице"
        with step(step2_title):
            self.should_be_only_video_button()
        step3_title = "Кнопка + В плейлист присутствует на странице"
        with step(step3_title):
            self.should_be_to_playlist_button()
        step4_title = "Кнопка Удалить файлы присутствует на странице"
        with step(step4_title):
            self.should_be_delete_files_button()
        step5_title = "Кнопка сеточное отображение присутствует на странице"
        with step(step5_title):
            self.should_be_grid_view_button()
        step6_title = "Кнопка табличное отображение присутствует на странице"
        with step(step6_title):
            self.should_be_table_view_button()
        step7_title = "Поле Поиск по названию присутствует на странице"
        with step(step7_title):
            self.should_be_search_by_name_input()
        step8_title = "Кнопка фильтр присутствует на странице"
        with step(step8_title):
            self.should_be_filter_button()
        step9_title = "Кнопка предыдущая страница присутствует на странице"
        with step(step9_title):
            self.should_be_previous_page_button()
        step10_title = "Кнопка следующая страница присутствует на странице"
        with step(step10_title):
            self.should_be_next_page_button()
        step11_title = "Чекбокс выбор медиа-файла присутствует на странице"
        with step(step11_title):
            self.should_be_checkbox_select_media_files()
        step12_title = "Кнопка Просмотр присутствует на странице"
        with step(step12_title):
            self.should_be_viewing_media_files()

    def should_be_download_files_button_found(self):
        assert self.is_element_present(*MediaPageLocators.DOWNLOAD_FILES_BUTTON), \
            "Download files button is not presented"

    def should_be_only_video_button(self):
        assert self.is_element_present(*MediaPageLocators.ONLY_VIDEO_BUTTON), \
            "Only video button is not presented"

    def should_be_to_playlist_button(self):
        assert self.is_element_present(*MediaPageLocators.ADD_TO_PLAYLIST_BUTTON), \
            "To playlist button is not presented"

    def should_be_delete_files_button(self):
        assert self.is_element_present(*MediaPageLocators.BLOCKED_DELETE_FILES_BUTTON), \
            "Delete files button is not presented"

    def should_be_grid_view_button(self):
        assert self.is_element_present(*MediaPageLocators.GRID_VIEW_BUTTON), \
            "Grid view button is not presented"

    def should_be_table_view_button(self):
        assert self.is_element_present(*MediaPageLocators.TABLE_VIEW_BUTTON), \
            "Table view button is not presented"

    def should_be_search_by_name_input(self):
        assert self.is_element_present(*MediaPageLocators.SEARCH_BY_NAME_INPUT), \
            "Search by name input is not presented"

    def should_be_filter_button(self):
        assert self.is_element_present(*MediaPageLocators.FILTER_BUTTON), \
            "Filter button is not presented"

    def should_be_checkbox_select_media_files(self):
        assert self.is_element_present(*MediaPageLocators.CHECKBOX_MEDIA_FILES), \
            "Checkbox media_files is not presented"

    def should_be_viewing_media_files(self):
        assert self.is_element_present(*MediaPageLocators.VIEWING_MEDIA_FILES), \
            "Viewing media_files is not presented"

    def should_be_previous_page_button(self):
        assert self.is_element_present(*MediaPageLocators.PREVIOUS_PAGE_BUTTON), \
            "Previous page button is not presented"

    def should_be_next_page_button(self):
        assert self.is_element_present(*MediaPageLocators.NEXT_PAGE_BUTTON), \
            "Next page button is not presented"

    def check_clickable_menu_buttons(self):

        step2_title = "Клик по кнопке Dashboard"
        with step(step2_title):
            self.click_on_dashboard()
        step3_title = "Клик по кнопке Устройства"
        with step(step3_title):
            self.click_on_devices()
        step4_title = "Клик по кнопке Медиа"
        with step(step4_title):
            self.click_on_media()
        step5_title = "Клик по кнопке Плейлист"
        with step(step5_title):
            self.click_on_playlist()
        step6_title = "Клик по кнопке Макеты полки"
        with step(step6_title):
            self.click_on_layout()
        step7_title = "Клик по кнопке Статистика"
        with step(step7_title):
            self.click_on_statistic()

    def click_on_dashboard(self):
        dashboard_button = self.browser.find_element(*MainPageLocators.DASHBOARD_BUTTON)
        dashboard_button.click()

    def click_on_devices(self):
        dashboard_button = self.browser.find_element(*MainPageLocators.DASHBOARD_BUTTON)
        dashboard_button.click()
        devices_button = self.browser.find_element(*MainPageLocators.DEVICES_BUTTON)
        devices_button.click()
        assert 'devices' in self.browser.current_url, \
            "Wrong URL. Should be devices page"

    def click_on_media(self):
        media_button = self.browser.find_element(*MainPageLocators.MEDIA_BUTTON)
        media_button.click()
        assert 'media' in self.browser.current_url, \
            "Wrong URL. Should be media page"

    def click_on_playlist(self):
        playlist_button = self.browser.find_element(*MainPageLocators.PLAYLISTS_BUTTON)
        playlist_button.click()
        assert 'playlist' in self.browser.current_url, \
            "Wrong URL. Should be playlist page"

    def click_on_layout(self):
        layout_button = self.browser.find_element(*MainPageLocators.LAYOUT_BUTTON)
        layout_button.click()
        assert 'layout' in self.browser.current_url, \
            "Wrong URL. Should be layout page"

    def click_on_statistic(self):
        statistic_button = self.browser.find_element(*MainPageLocators.STATISTIC_BUTTON)
        statistic_button.click()

    def upload_media_file_0(self):
        step1_title = "Загрузка медиа-файла cat0.png"
        with step(step1_title):
            self.download_media_files_cat0()

    def download_media_files_cat0(self):
        download_files_button = self.browser.find_element(*MediaPageLocators.DOWNLOAD_FILES_BUTTON)
        download_files_button.click()
        input_field = self.browser.find_element(*MediaPageLocators.CHOOSE_FILE_BUTTON)
        image_path = CAT_PATH
        input_field.send_keys(image_path)
        time.sleep(0.1)
        download_button = self.browser.find_element(*MediaPageLocators.DOWNLOAD_BUTTON)
        download_button.click()
        time.sleep(0.1)
        assert self.is_element_present(*MediaPageLocators.CAT0_PICTURE), \
            "Media file cat0.png is not presented on page"

    def delete_cat0(self):
        step1_title = "Удаление медиа-файла cat0.png"
        with step(step1_title):
            self.delete_media_file_0()

    def delete_media_file_0(self):
        checkbox_cat1_button = self.browser.find_element(*MediaPageLocators.CHECKBOX_CAT0_PICTURE)
        checkbox_cat1_button.click()
        delete_media_files = self.browser.find_element(*MediaPageLocators.DELETE_MEDIA_FILES)
        ActionChains(self.browser).move_to_element(delete_media_files).click().perform()
        are_you_sure_yes_button = self.browser.find_element(*MediaPageLocators.ARE_YOU_SURE_YES_BUTTON)
        ActionChains(self.browser).move_to_element(are_you_sure_yes_button).click().perform()
        time.sleep(0.1)
        assert self.is_element_present(*MediaPageLocators.CAT0_PICTURE), \
            "Media file cat0.png is presented on page"

    def upload_media_files_1_5(self):
        self.download_media_files_cats_5()
        self.check_is_media_files_presented()

    def download_media_files_cats_5(self):
        download_files_button = self.browser.find_element(*MediaPageLocators.DOWNLOAD_FILES_BUTTON)
        download_files_button.click()
        input_field = self.browser.find_element(*MediaPageLocators.CHOOSE_FILE_BUTTON)
        image_path1 = CAT1_PATH
        image_path2 = CAT2_PATH
        image_path3 = CAT3_PATH
        image_path4 = CAT4_PATH
        image_path5 = CAT5_PATH
        time.sleep(0.1)
        input_field.send_keys(image_path1)
        input_field = self.browser.find_element(*MediaPageLocators.CHOOSE_FILE_BUTTON)
        input_field.send_keys(image_path2)
        input_field = self.browser.find_element(*MediaPageLocators.CHOOSE_FILE_BUTTON)
        input_field.send_keys(image_path3)
        input_field = self.browser.find_element(*MediaPageLocators.CHOOSE_FILE_BUTTON)
        input_field.send_keys(image_path4)
        input_field = self.browser.find_element(*MediaPageLocators.CHOOSE_FILE_BUTTON)
        input_field.send_keys(image_path5)
        time.sleep(0.1)
        download_on_page_button = self.browser.find_element(*MediaPageLocators.DOWNLOAD_BUTTON)
        download_on_page_button.click()
        time.sleep(0.1)

    def check_is_media_files_presented(self):
        assert self.is_element_present(*MediaPageLocators.CAT1_PICTURE), \
            "Media file cat1 is not presented on page"
        assert self.is_element_present(*MediaPageLocators.CAT2_PICTURE), \
            "Media file cat2 is not presented on page"
        assert self.is_element_present(*MediaPageLocators.CAT3_PICTURE), \
            "Media file cat3 is not presented on page"
        assert self.is_element_present(*MediaPageLocators.CAT4_PICTURE), \
            "Media file cat4 is not presented on page"
        assert self.is_element_present(*MediaPageLocators.CAT5_PICTURE), \
            "Media file cat5 is not presented on page"

    def delete_cats1_5(self):
        self.delete_media_file1()
        self.delete_media_file1()
        self.delete_media_file1()
        self.delete_media_file1()
        self.delete_media_file1()
        self.check_deleted_files()

    def delete_media_file1(self):
        checkbox_cat1_button = self.browser.find_element(*MediaPageLocators.CHECKBOX_CAT_PICTURE)
        checkbox_cat1_button.click()
        delete_media_files = self.browser.find_element(*MediaPageLocators.DELETE_MEDIA_FILES)
        ActionChains(self.browser).move_to_element(delete_media_files).click().perform()
        are_you_sure_yes_button = self.browser.find_element(*MediaPageLocators.ARE_YOU_SURE_YES_BUTTON)
        time.sleep(0.1)
        ActionChains(self.browser).move_to_element(are_you_sure_yes_button).click().perform()

    def check_deleted_files(self):
        assert self.is_not_element_present(*MediaPageLocators.CAT3_PICTURE)

    def check_search_field(self):
        self.enter_keys_card_in_search_input_media()

    def enter_keys_card_in_search_input_media(self):
        search_button = self.browser.find_element(*MediaPageLocators.SEARCH_BY_NAME_INPUT)
        search_button.click()
        search_button.clear()
        search_button.send_keys("Card")
        assert self.is_element_present(*MediaPageLocators.CARD_POSTER_LOCATOR), \
            "Card_poster_2880x158_Web is not presented"




