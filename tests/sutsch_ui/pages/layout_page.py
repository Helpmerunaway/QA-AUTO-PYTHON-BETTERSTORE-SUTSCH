from selenium.webdriver.common.action_chains import ActionChains
from tests.sutsch_ui.pages.base_page import BasePage
import time
from tests.sutsch_ui.pages.locators import MainPageLocators
from tests.sutsch_ui.pages.locators import LayoutPageLocators
from tests.sutsch_ui.config import SCREENSHOTS_DIR
from allure_commons._allure import step
from selenium.webdriver.common.keys import Keys
from current_date_and_time import today_date


class LayoutPage(BasePage):
    def should_be_layout_page(self):
        step1_title = "В URL адресе должен присутствовать /layout"
        with step(step1_title):
            self.should_be_layout_url()
        step2_title = "Должна быть открыта страница Макеты"
        with step(step2_title):
            self.should_be_layout_page_open()
        return self.browser.current_url

    def should_be_layout_url(self):
        assert 'layout' in self.browser.current_url, \
            "URL is not valid. Should be layout page"

    def should_be_layout_page_open(self):
        pass

    def layout_page_open_by_unauthorized_user(self):
        step1_title = "Пользователь попадает на страницу авторизации"
        with step(step1_title):
            self.when_unauthorized_user_opens_layout_page()

    def when_unauthorized_user_opens_layout_page(self):
        assert self.is_element_present(*MainPageLocators.SHELF_TALKER_BUTTON), \
            "Betterstore logo is not presented"

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

    def check_layout_page_header_buttons(self):
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

    def should_be_exit_user_button(self):
        assert self.is_element_present(*MainPageLocators.EXIT_USER_BUTTON), \
            "Exit user button is presented"

    def check_layout_page_main_area_buttons(self):
        # main_area
        step1_title = "Кнопка Создать макет присутствует на странице"
        with step(step1_title):
            self.should_be_create_layout_button_found()
        step2_title = "Кнопка Удалить присутствует на странице"
        with step(step2_title):
            self.should_be_delete_layout_button_found()
        step3_title = "Кнопка сеточное отображение присутствует на странице"
        with step(step3_title):
            self.should_be_grid_view_button()
        step4_title = "Кнопка табличное отображение присутствует на странице"
        with step(step4_title):
            self.should_be_table_view_button()
        step5_title = "Поле Поиск по название присутствует на странице"
        with step(step5_title):
            self.should_be_search_by_name_input()
        step6_title = "Кнопка фильтр присутствует на странице"
        with step(step6_title):
            self.should_be_filter_button()
        step6_1_title = "Кнопка Открыть плейлист присутствует на странице"
        with step(step6_1_title):
            self.should_be_open_playlist_button()
        step6_2_title = "Кнопка Изменить плейлист присутствует на странице"
        with step(step6_2_title):
            self.should_be_change_playlist_button()
        step7_title = "Кнопка предыдущая страница присутствует на странице"
        with step(step7_title):
            self.should_be_previous_page_button()
        step8_title = "Кнопка следующая страница присутствует на странице"
        with step(step8_title):
            self.should_be_next_page_button()

    def should_be_create_layout_button_found(self):
        assert self.is_element_present(*LayoutPageLocators.CREATE_LAYOUT_BUTTON), \
            "Create layout button is not presented"

    def should_be_delete_layout_button_found(self):
        assert self.is_element_present(*LayoutPageLocators.BLOCKED_DELETE_LAYOUT_BUTTON), \
            "Delete layout button is not presented"

    def should_be_used_switcher(self):
        assert self.is_element_present(*LayoutPageLocators.USED_SWITCHER), \
            "Used switcher is not presented"

    def should_be_grid_view_button(self):
        assert self.is_element_present(*LayoutPageLocators.GRID_VIEW_BUTTON), \
            "Grid view button is not presented"

    def should_be_table_view_button(self):
        assert self.is_element_present(*LayoutPageLocators.TABLE_VIEW_BUTTON), \
            "Table view button is not presented"

    def should_be_search_by_name_input(self):
        assert self.is_element_present(*LayoutPageLocators.SEARCH_BY_NAME_INPUT), \
            "Search by name input is not presented"

    def should_be_filter_button(self):
        assert self.is_element_present(*LayoutPageLocators.FILTER_BUTTON), \
            "Filter button is not presented"

    def should_be_previous_page_button(self):
        assert self.is_element_present(*LayoutPageLocators.PREVIOUS_PAGE_BUTTON), \
            "Previous page button is not presented"

    def should_be_next_page_button(self):
        assert self.is_element_present(*LayoutPageLocators.NEXT_PAGE_BUTTON), \
            "Next page button is not presented"

    def should_be_open_playlist_button(self):
        assert self.is_element_present(*LayoutPageLocators.ACTION_OPEN_LAYOUT), \
            "Open layout button is not presented"

    def should_be_change_playlist_button(self):
        assert self.is_element_present(*LayoutPageLocators.ACTION_CHANGE_LAYOUT), \
            "Change layout button is not presented"

    def check_clickable_menu_buttons(self):

        step1_title = "Клик по кнопке Dashboard"
        with step(step1_title):
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

    def create_new_layout_empty(self):
        self.click_on_create_layout_button()
        self.click_on_save_layout_button()
        self.check_is_modal_window_presented()

    def click_on_create_layout_button(self):
        create_layout = self.browser.find_element(*LayoutPageLocators.CREATE_LAYOUT_BUTTON)
        create_layout.click()

    def click_on_save_layout_button(self):
        save_layout_button = self.browser.find_element(*LayoutPageLocators.SAVE_LAYOUT_BUTTON)
        ActionChains(self.browser).move_to_element(save_layout_button).click().perform()

    def check_is_modal_window_presented(self):
        assert self.is_element_present(*LayoutPageLocators.MODAL_WINDOW), \
            "Modal window is not presented"

    def create_new_layout_maket_date_time(self):
        self.click_on_create_layout_button()
        self.enter_layout_name_input()
        self.choose_esl_template()
        self.number_of_esl_template_is_11()
        self.click_on_add_tag_input()
        self.press_add_new_tag_button_new_maket()
        self.click_on_save_layout_button()
        self.check_is_maket_presented()
        self.save_screenshot_created_layout()

    def enter_layout_name_input(self):
        layout_name_input = self.browser.find_element(*LayoutPageLocators.LAYOUT_NAME_INPUT)
        layout_name_input.click()
        layout_name_input.send_keys("Maket " + today_date)

    def choose_esl_template(self):
        esl_template = self.browser.find_element(*LayoutPageLocators.CHOOSE_ESL_TEMPLATE)
        ActionChains(self.browser).move_to_element(esl_template).click().send_keys(Keys.RETURN).perform()
        assert self.is_element_present(*LayoutPageLocators.ESL_TEMPLATE_IS_ADDED)

    def number_of_esl_template_is_11(self):
        number_of_esls = self.browser.find_element(*LayoutPageLocators.NUMBER_OF_ESL_TEMPLATE)
        ActionChains(self.browser).move_to_element(number_of_esls).click().send_keys('1').send_keys(Keys.RETURN).perform()
        assert self.is_element_present(*LayoutPageLocators.VALUE_OF_ESLS_NUMBER_11)

    def plus_els_to_layout_is_1(self):
        plus_esl_to_layout = self.browser.find_element(*LayoutPageLocators.ADD_ESL_TO_LAYOUT)
        ActionChains(self.browser).move_to_element(plus_esl_to_layout).click().perform()

    def choose_esl_template_second(self):
        devices_size_is = self.browser.find_element(*LayoutPageLocators.CHOOSE_ESL_TEMPLATE_SECOND)
        ActionChains(self.browser).release(devices_size_is).click().send_keys(Keys.RETURN).perform()

    def change_for_what_devices_to_1920_158(self):
        pass

    def click_on_add_tag_input(self):
        add_tag_input = self.browser.find_element(*LayoutPageLocators.ADD_TAG_INPUT)
        add_tag_input.click()
        add_tag_input.send_keys('new_maket')

    def press_add_new_tag_button_new_maket(self):
        add_tag_button = self.browser.find_element(*LayoutPageLocators.ADD_TAG_BUTTON)
        add_tag_button.click()
        assert self.is_element_present(*LayoutPageLocators.MUST_BE_NEW_TAG_VALUE)

    def check_is_maket_presented(self):
        assert self.is_element_present(*LayoutPageLocators.MAKET_IS_PRESENTED)

    def save_screenshot_created_layout(self):
        self.browser.refresh()
        self.browser.save_screenshot(SCREENSHOTS_DIR+"test_layout_create_new_valid_layout.png")

    def open_new_layout_maket_date_time(self):
        self.click_on_open_button_new_layout()

    def click_on_open_button_new_layout(self):
        action_open_button = self.browser.find_element(*LayoutPageLocators.ACTION_OPEN_LAYOUT)
        action_open_button.click()
        time.sleep(0.1)
        self.browser.save_screenshot(SCREENSHOTS_DIR+"test_layout_open_new_valid_layout.png")
        assert self.is_element_present(*LayoutPageLocators.WRAPPER_BODY_IS_PRESENTED)
        assert self.is_element_present(*LayoutPageLocators.LAYOUT_NAME_IS_PRESENTED)

    def edit_new_layout_maket_date_time(self):
        self.click_on_edit_layout_button()
        self.add_new_tag_calls_modified()
        self.press_add_new_tag_button()
        self.click_on_save_layout_button()
        self.make_screenshot_after_edit_layout()
        self.check_new_tag_modified_is_presented()

    def click_on_edit_layout_button(self):
        edit_layout_button = self.browser.find_element(*LayoutPageLocators.ACTION_CHANGE_LAYOUT)
        edit_layout_button.click()

    def add_new_tag_calls_modified(self):
        add_tag_input = self.browser.find_element(*LayoutPageLocators.ADD_TAG_INPUT)
        add_tag_input.click()
        add_tag_input.send_keys('MODIFIED')

    def press_add_new_tag_button(self):
        add_tag_button = self.browser.find_element(*LayoutPageLocators.ADD_TAG_BUTTON)
        add_tag_button.click()

    def make_screenshot_after_edit_layout(self):
        self.browser.refresh()
        time.sleep(0.1)
        self.browser.save_screenshot(SCREENSHOTS_DIR+"test_layout_edit_new_valid_layout.png")

    def check_new_tag_modified_is_presented(self):
        self.browser.refresh()
        time.sleep(0.1)
        assert self.is_element_present(*LayoutPageLocators.MUST_BE_MODIFIED_VALUE)

    def delete_maket_from_layouts(self):
        self.checkboxed_top_layout_maket_date_time()
        self.click_on_delete_button()
        self.click_on_are_you_sure_yes_button()
        self.check_is_layout_deleted()

    def checkboxed_top_layout_maket_date_time(self):
        checkboxed_maket = self.browser.find_element(*LayoutPageLocators.CHECKBOXED_TOP_LAYOUT)
        checkboxed_maket.click()

    def click_on_delete_button(self):
        delete_maket_button = self.browser.find_element(*LayoutPageLocators.ACTIVE_DELETE_LAYOUT_BUTTON)
        ActionChains(self.browser).release(delete_maket_button).click().perform()
        time.sleep(0.3)

    def click_on_are_you_sure_yes_button(self):
        are_you_sure_button = self.browser.find_element(*LayoutPageLocators.ARE_YOU_SURE_YES_BUTTON)
        ActionChains(self.browser).release(are_you_sure_button).click().perform()

    def check_is_layout_deleted(self):
        self.browser.refresh()
        self.browser.save_screenshot(SCREENSHOTS_DIR+'test_layout_delete_new_valid_layout.png')
