from .base_page import BasePage
import time
from tests.sutsch_ui.pages.locators import DevicesPageLocators
from tests.sutsch_ui.pages.locators import MainPageLocators
from allure_commons._allure import step


class DevicesPage(BasePage):

    def should_be_devices_page(self):
        step1_title = "В URL адресе должен присутствовать /devices"
        with step(step1_title):
            self.should_be_devices_url()
        step2_title = "Должна быть открыта страница устройства"
        with step(step2_title):
            self.should_be_devices_page_open()

    def should_be_devices_url(self):
        assert 'devices' in self.browser.current_url, \
            "URL is not valid. Should be devices page"

    def should_be_devices_page_open(self):
        assert 'Устройства' in self.browser.title, \
            "This is not a devices page"

    def devices_page_open_by_unauthorized_user(self):
        step1_title = "Неавторизованный пользователь попадает на страницу авторизации"
        with step(step1_title):
            self.when_unauthorized_user_opens_devices_page()

    def when_unauthorized_user_opens_devices_page(self):
        assert self.is_element_present(*MainPageLocators.BETTERSTORE_LOGO), \
            "Betterstore logo is not presented"
        assert 'auth' in self.browser.current_url, \
            "URL is not valid. Should be auth page"

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

    def check_devices_page_header_buttons(self):
        step1_title = "Заголовок Устройства присутствует на странице"
        with step(step1_title):
            self.should_be_devices_name_page_headline()
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

    def should_be_devices_name_page_headline(self):
        assert self.is_element_present(*DevicesPageLocators.DEVICES_NAME_HEADER), \
            "Header text Устройства is not presented"

    def should_be_exit_user_button(self):
        assert self.is_element_present(*MainPageLocators.EXIT_USER_BUTTON), \
            "Exit user button is presented"

    def check_devices_page_main_area_buttons(self):
        # main_area
        step1_title = "Счетчик устройств присутствует на странице"
        with step(step1_title):
            self.should_be_devices_counter_found()
        step2_title = "Кнопка +Плейлист присутствует на странице"
        with step(step2_title):
            self.should_be_playlist_button()
        step3_title = "Кнопка В группу присутствует на странице"
        with step(step3_title):
            self.should_be_to_the_group_button()
        step4_title = "Кнопка Удалить присутствует на странице"
        with step(step4_title):
            self.should_be_delete_device_button()
        step5_title = "Кнопка сеточное отображение присутствует на странице"
        with step(step5_title):
            self.should_be_grid_view_button()
        step6_title = "Кнопка табличное отображение присутствует на странице"
        with step(step6_title):
            self.should_be_table_view_button()
        step7_title = "Поле Поиск по название присутствует на странице"
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

    def should_be_devices_counter_found(self):
        assert self.is_element_present(*DevicesPageLocators.DEVICES_FOUND_COUNTER), \
            "Devices found counter is not presented"

    def should_be_playlist_button(self):
        assert self.is_element_present(*DevicesPageLocators.ADD_TO_PLAYLIST_BUTTON), \
            "Add to playlist button is not presented"

    def should_be_to_the_group_button(self):
        assert self.is_element_present(*DevicesPageLocators.ADD_TO_GROUP_BUTTON), \
            "Add to group button is not presented"

    def should_be_delete_device_button(self):
        assert self.is_element_present(*DevicesPageLocators.DELETE_DEVICE_BUTTON), \
            "Delete device button is not presented"

    def should_be_grid_view_button(self):
        assert self.is_element_present(*DevicesPageLocators.GRID_VIEW_BUTTON), \
            "Grid view button is not presented"

    def should_be_table_view_button(self):
        assert self.is_element_present(*DevicesPageLocators.TABLE_VIEW_BUTTON), \
            "Table view button is not presented"

    def should_be_search_by_name_input(self):
        assert self.is_element_present(*DevicesPageLocators.SEARCH_BY_NAME_INPUT), \
            "Search by name input is not presented"

    def should_be_filter_button(self):
        assert self.is_element_present(*DevicesPageLocators.FILTER_BUTTON), \
            "Filter button is not presented"

    def should_be_previous_page_button(self):
        assert self.is_element_present(*DevicesPageLocators.PREVIOUS_PAGE_BUTTON), \
            "Previous page button is not presented"

    def should_be_next_page_button(self):
        assert self.is_element_present(*DevicesPageLocators.NEXT_PAGE_BUTTON), \
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

    def logout_user(self):
        step1_title = "Клик по кнопке выход"
        with step(step1_title):
            self.logout()
        step2_title = "Пользователь находится на странице авторизации"
        with step(step2_title):
            self.check_url_must_be_auth()

    def logout(self):
        logout_button = self.browser.find_element(*MainPageLocators.EXIT_USER_BUTTON)
        logout_button.click()

    def check_url_must_be_auth(self):
        time.sleep(0.3)
        assert 'Авторизация' in self.browser.title, \
            "This is not a auth page"










