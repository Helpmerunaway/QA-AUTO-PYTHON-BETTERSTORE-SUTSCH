
from selenium.webdriver.common.action_chains import ActionChains
from tests.sutsch_ui.pages.base_page import BasePage
import time
from tests.sutsch_ui.pages.locators import MainPageLocators
from tests.sutsch_ui.pages.locators import PlaylistPageLocators
from tests.sutsch_ui.config import SCREENSHOTS_DIR, STAGE_PLAYLIST_URL

from allure_commons._allure import step
from selenium.webdriver.common.keys import Keys

from current_date_and_time import today_date


class PlaylistPage(BasePage):
    def should_be_playlist_page(self):
        step1_title = "В URL адресе должен присутствовать /playlist"
        with step(step1_title):
            self.should_be_playlist_url()
        step2_title = "Должна быть открыта страница Плейлисты"
        with step(step2_title):
            self.should_be_playlist_page_open()
        return self.browser.current_url

    def should_be_playlist_url(self):
        assert 'playlist' in self.browser.current_url, \
            "URL is not valid. Should be playlist page"

    def should_be_playlist_page_open(self):
        assert 'Плейлисты' in self.browser.title, \
            "This is not a playlist page"

    def playlist_page_open_by_unauthorized_user(self):
        step1_title = "Пользователь попадает на страницу авторизации"
        with step(step1_title):
            self.when_unauthorized_user_opens_playlist_page()

    def when_unauthorized_user_opens_playlist_page(self):
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

    def check_playlist_page_header_buttons(self):
        step1_title = "Заголовок Плейлисты присутствует на странице"
        with step(step1_title):
            self.should_be_playlist_name_page_headline()
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

    def should_be_playlist_name_page_headline(self):
        assert self.is_element_present(*PlaylistPageLocators.PLAYLIST_NAME_HEADER), \
            "Header text Плейлисты is not presented"

    def should_be_exit_user_button(self):
        assert self.is_element_present(*MainPageLocators.EXIT_USER_BUTTON), \
            "Exit user button is presented"

    def check_playlist_page_main_area_buttons(self):
        # main_area
        step1_title = "Кнопка Создать плейлист присутствует на странице"
        with step(step1_title):
            self.should_be_create_playlist_button_found()
        step2_title = "Кнопка Удалить присутствует на странице"
        with step(step2_title):
            self.should_be_delete_playlist_button()
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

    def should_be_create_playlist_button_found(self):
        assert self.is_element_present(*PlaylistPageLocators.CREATE_PLAYLIST_BUTTON), \
            "Create playlist button is not presented"

    def should_be_delete_playlist_button(self):
        assert self.is_element_present(*PlaylistPageLocators.DELETE_PLAYLIST_BUTTON), \
            "Delete playlist button is not presented"

    def should_be_grid_view_button(self):
        assert self.is_element_present(*PlaylistPageLocators.GRID_VIEW_BUTTON), \
            "Grid view button is not presented"

    def should_be_table_view_button(self):
        assert self.is_element_present(*PlaylistPageLocators.TABLE_VIEW_BUTTON), \
            "Table view button is not presented"

    def should_be_search_by_name_input(self):
        assert self.is_element_present(*PlaylistPageLocators.SEARCH_BY_NAME_INPUT), \
            "Search by name input is not presented"

    def should_be_filter_button(self):
        assert self.is_element_present(*PlaylistPageLocators.FILTER_BUTTON), \
            "Filter button is not presented"

    def should_be_previous_page_button(self):
        assert self.is_element_present(*PlaylistPageLocators.PREVIOUS_PAGE_BUTTON), \
            "Previous page button is not presented"

    def should_be_next_page_button(self):
        assert self.is_element_present(*PlaylistPageLocators.NEXT_PAGE_BUTTON), \
            "Next page button is not presented"

    def should_be_open_playlist_button(self):
        assert self.is_element_present(*PlaylistPageLocators.ACTION_OPEN_PLAYLIST), \
            "Open playlist button is not presented"

    def should_be_change_playlist_button(self):
        assert self.is_element_present(*PlaylistPageLocators.ACTION_CHANGE_PLAYLIST), \
            "Change playlist button is not presented"

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

    def create_new_empty_playlist(self):
        step1_title = "Клик по кнопке Создать плейлист. Переход на страницу Настроить плейлист"
        with step(step1_title):
            self.click_on_create_button_and_go_to_step_1_set_playlist()
        step2_title = "Клик по кнопке Далее. Переход на страницу Выбрать устройства"
        with step(step2_title):
            self.click_on_next_button_and_go_to_step_2_choose_devices()
        step3_title = "Клик по кнопке Далее. Переход на страницу График воспроизведения"
        with step(step3_title):
            self.click_on_next_button_and_go_to_step_3_playback_schedule()
        step4_title = "Клик по кнопке Запустить. Плейлист не создается"
        with step(step4_title):
            self.click_on_run_playlist_button_if_not_valid()

    def click_on_create_button_and_go_to_step_1_set_playlist(self):
        create_new_playlist = self.browser.find_element(*PlaylistPageLocators.CREATE_PLAYLIST_BUTTON)
        create_new_playlist.click()
        assert self.is_element_present(*PlaylistPageLocators.PLAYLIST_NAME_INPUT)

    def click_on_next_button_and_go_to_step_2_choose_devices(self):
        next_step_button = self.browser.find_element(*PlaylistPageLocators.NEXT_STEP)
        next_step_button.click()
        assert self.is_element_present(*PlaylistPageLocators.FIND_DEVICES_INPUT)

    def click_on_next_button_and_go_to_step_3_playback_schedule(self):
        next_step_button = self.browser.find_element(*PlaylistPageLocators.NEXT_STEP)
        next_step_button.click()
        assert self.is_element_present(*PlaylistPageLocators.CALENDAR_SCHEDULE)

    def click_on_run_playlist_button_if_not_valid(self):
        run_playlist_button = self.browser.find_element(*PlaylistPageLocators.RUN_PLAYLIST)
        run_playlist_button.click()
        assert self.is_element_present(*PlaylistPageLocators.RUN_PLAYLIST), \
            "Empty playlist has been launched. Run playlist button is not presented"

    def should_be_playlist_name_not_present(self):
        assert self.is_not_element_present(*PlaylistPageLocators.PLAYLIST_NAME_1920x158_MTS_LIME_MAKET_IS_PRESENTED)

    def create_valid_new_playlist_1920_step_1_customize_playlist(self):
        self.click_on_create_button_and_go_to_step_1_set_playlist()
        self.click_on_checkbox_preview_size_1920()
        self.click_on_playlist_name_input()
        self.enter_playlist_name_in_playlist_name_form()
        self.click_on_playlist_new_tag_input()
        self.enter_new_tag_name_1920_in_add_tag_input()
        self.click_on_add_tag_button()
        self.check_tag_1920_is_added()
        self.click_on_plus_content_button()
        self.choose_file_type_picture()
        self.check_is_media_file_number_1_added()
        self.enter_input_content_name_1920_mts()
        self.click_on_plus_content_button_after_1_content_added()
        self.choose_file_type_video()
        self.check_is_media_file_number_2_added()
        self.enter_input_content_name_lime_1920()
        self.click_on_plus_content_button_after_1_content_added()
        self.choose_file_type_layout()
        self.check_is_media_file_number_3_added()
        self.enter_input_content_name_maket_1337()
        self.click_on_render_button()
        self.click_on_next_step_button()
        self.check_is_it_a_choose_devices_step()

    def click_on_checkbox_preview_size_1920(self):
        checkbox_size_1920_button = self.browser.find_element(*PlaylistPageLocators.RADIO_BUTTON_SIZE_1920)
        checkbox_size_1920_button.click()
        assert self.is_element_present(*PlaylistPageLocators.RADIO_BUTTON_IS_CHECKED)

    def click_on_playlist_name_input(self):
        playlist_name_input = self.browser.find_element(*PlaylistPageLocators.PLAYLIST_NAME_INPUT)
        playlist_name_input.click()

    def enter_playlist_name_in_playlist_name_form(self):
        playlist_name_input = self.browser.find_element(*PlaylistPageLocators.PLAYLIST_NAME_INPUT)
        playlist_name_input.clear()
        playlist_name_input.send_keys("1920x158_mts_lime_maket_" + today_date)

    def click_on_playlist_new_tag_input(self):
        new_tag_input = self.browser.find_element(*PlaylistPageLocators.ADD_TAG_INPUT)
        new_tag_input.click()
        assert self.browser.switch_to.active_element

    def enter_new_tag_name_1920_in_add_tag_input(self):
        new_tag_input = self.browser.find_element(*PlaylistPageLocators.ADD_TAG_INPUT)
        new_tag_input.clear()
        new_tag_input.send_keys("1920")

    def click_on_add_tag_button(self):
        add_tag_button = self.browser.find_element(*PlaylistPageLocators.ADD_NEW_TAG_BUTTON)
        add_tag_button.click()

    def check_tag_1920_is_added(self):
        assert self.is_element_present(*PlaylistPageLocators.TAG_1920)

    def click_on_plus_content_button(self):
        plus_content_button = self.browser.find_element(*PlaylistPageLocators.PLUS_CONTENT_BUTTON)
        plus_content_button.click()

    def click_on_plus_content_button_after_1_content_added(self):
        plus_content_button_after_1 = self.browser.find_element(*PlaylistPageLocators.PLUS_CONTENT_BUTTON_AFTER_1_ADDED)
        plus_content_button_after_1.click()
        assert self.is_element_present(*PlaylistPageLocators.SIDE_MENU_FILE_TYPE)

    def choose_file_type_picture(self):
        file_type_picture = self.browser.find_element(*PlaylistPageLocators.CHOOSE_FILE_TYPE_PICTURE)
        file_type_picture.click()

    def check_is_media_file_number_1_added(self):
        assert self.is_element_present(*PlaylistPageLocators.NUMBER_OF_ADDED_CONTENT_1)

    def enter_input_content_name_1920_mts(self):
        content_name_input = self.browser.find_element(*PlaylistPageLocators.CONTENT_1_NAME_INPUT)
        content_name_input.clear()
        content_name_input.send_keys("1920_158_mts.png")
        content_name_input.send_keys(Keys.ENTER)
        assert self.is_element_present(*PlaylistPageLocators.MTS_1920_PNG_IS_ADDED)

    def choose_file_type_video(self):
        file_type_video = self.browser.find_element(*PlaylistPageLocators.CHOOSE_FILE_TYPE_VIDEO)
        file_type_video.click()

    def check_is_media_file_number_2_added(self):
        assert self.is_element_present(*PlaylistPageLocators.NUMBER_OF_ADDED_CONTENT_2)

    def enter_input_content_name_lime_1920(self):
        content_name_input = self.browser.find_element(*PlaylistPageLocators.CONTENT_2_NAME_INPUT)
        content_name_input.clear()
        content_name_input.send_keys("Лайм_1920x158_12sec.mp4")
        content_name_input.send_keys(Keys.ENTER)
        assert self.is_element_present(*PlaylistPageLocators.LIME_1920_MP4_IS_ADDED)

    def choose_file_type_layout(self):
        file_type_picture = self.browser.find_element(*PlaylistPageLocators.CHOOSE_FILE_TYPE_LAYOUT)
        file_type_picture.click()

    def check_is_media_file_number_3_added(self):
        assert self.is_element_present(*PlaylistPageLocators.NUMBER_OF_ADDED_CONTENT_3)

    def enter_input_content_name_maket_1337(self):
        content_name_input = self.browser.find_element(*PlaylistPageLocators.CONTENT_3_NAME_INPUT)
        content_name_input.clear()
        content_name_input.send_keys("Макет 1337")
        content_name_input.send_keys(Keys.ENTER)
        assert self.is_element_present(*PlaylistPageLocators.MAKET_1337_IS_ADDED)

    def click_on_render_button(self):
        render_button = self.browser.find_element(*PlaylistPageLocators.RENDER_BUTTON)
        render_button.click()
        assert self.is_element_present(*PlaylistPageLocators.LOAD_SPINNER)

    def click_on_next_step_button(self):
        next_step_button = self.browser.find_element(*PlaylistPageLocators.NEXT_STEP)
        next_step_button.click()

    def check_is_it_a_choose_devices_step(self):
        assert self.is_element_present(*PlaylistPageLocators.FIND_DEVICES_INPUT)

    def create_valid_new_playlist_1920_step_2_choose_devices(self):
        self.uncover_small_stand_group()
        self.click_on_checkbox_small_shelf()
        self.click_on_next_step_button()

    def uncover_small_stand_group(self):
        uncover_button = self.browser.find_element(*PlaylistPageLocators.UNCOVER_GROUP_SMALL_STAND)
        uncover_button.click()
        assert self.is_element_present(*PlaylistPageLocators.PRESS_TO_COVER_GROUP_SMALL_STAND)

    def click_on_checkbox_small_shelf(self):
        click_to_2300314490466_small = self.browser.find_element(
            *PlaylistPageLocators.CHECKBOX_SMALL_SHELF_2300314490466)
        click_to_2300314490466_small.click()
        assert self.is_element_present(*PlaylistPageLocators.CHECKBOX_SMALL_SHELF_2300314490466_IS_CHECKED)

    def create_valid_new_playlist_1920_step_3_play_schedule(self):
        self.click_on_calendar_schedule()
        self.check_calendar_container_is_present()
        self.calendar_schedule_is_current_date()
        self.click_on_checkbox_play_everyday()
        self.check_checkbox_play_everyday_is_checked()
        self.click_on_checkbox_all_day_long_play()
        self.check_checkbox_all_day_long_is_checked()
        self.click_on_run_playlist_button()
        self.should_be_playlist_name_on_page()
        self.make_screenshot_proof()

    def click_on_calendar_schedule(self):
        click_on_calendar_schedule_button = self.browser.find_element(*PlaylistPageLocators.CALENDAR_SCHEDULE)
        click_on_calendar_schedule_button.click()

    def check_calendar_container_is_present(self):
        assert self.is_element_present(*PlaylistPageLocators.CALENDAR_BODY_CONTAINER)

    def calendar_schedule_is_current_date(self):
        calendar_body_container = self.browser.find_element(*PlaylistPageLocators.CALENDAR_BODY_CONTAINER)
        calendar_body_container.send_keys(Keys.RETURN)
        calendar_body_container.send_keys(Keys.RETURN)

    def click_on_checkbox_play_everyday(self):
        checkbox_play_everyday = self.browser.find_element(*PlaylistPageLocators.PLAY_EVERYDAY_CHECKBOX)
        checkbox_play_everyday.click()

    def check_checkbox_play_everyday_is_checked(self):
        assert self.is_element_present(*PlaylistPageLocators.PLAY_EVERYDAY_CHECKBOX_IS_CHECKED)

    def click_on_checkbox_all_day_long_play(self):
        all_day_long_checkbox = self.browser.find_element(*PlaylistPageLocators.ALL_DAY_LONG_CHECKBOX)
        all_day_long_checkbox.click()

    def check_checkbox_all_day_long_is_checked(self):
        assert self.is_element_present(*PlaylistPageLocators.ALL_DAY_LONG_CHECKBOX_IS_CHECKED)

    def click_on_run_playlist_button(self):
        run_playlist_button = self.browser.find_element(*PlaylistPageLocators.RUN_PLAYLIST)
        run_playlist_button.click()

    def should_be_playlist_name_on_page(self):
        assert self.is_element_present(*PlaylistPageLocators.PLAYLIST_NAME_1920x158_MTS_LIME_MAKET_IS_PRESENTED)

    def make_screenshot_proof(self):
        self.browser.save_screenshot(SCREENSHOTS_DIR+"test_playlist_create_new_playlist_mts_card_maket_1920.png")

    def open_playlist_1920_mts_lime_maket(self):
        open_playlist_button = self.browser.find_element(*PlaylistPageLocators.OPEN_PLAYLIST_BUTTON)
        open_playlist_button.click()
        time.sleep(0.1)
        self.browser.save_screenshot(SCREENSHOTS_DIR+"test_playlist_open_new_playlist_mts_card_maket_1920.png")
        assert self.is_element_present(*PlaylistPageLocators.MODAL_BODY_IS_ACTIVE)

    def get_video_src_playlist_1920_mts_lime_maket(self):
        open_playlist_button = self.browser.find_element(*PlaylistPageLocators.OPEN_PLAYLIST_BUTTON)
        open_playlist_button.click()
        time.sleep(1.0)
        VIDEO_SRC = self.browser.find_element(*PlaylistPageLocators.VIDEO_SRC_1920x158_MTS_LIME_MAKET)
        video = self.browser.find_element_by_tag_name('video').get_attribute("src")
        print('Video src=', video)
        return(video)

    def edit_playlist_1920_mts_lime_maket(self):
        self.check_play_changed_is_not_presented()
        self.press_edit_playlist_button()
        self.click_on_playlist_new_tag_input()
        self.enter_new_tag_name_playlist_changed_in_add_tag_input()
        self.click_on_add_tag_button()
        self.check_tag_playlist_was_edited()
        self.click_on_next_button_and_go_to_step_2_choose_devices()
        self.click_on_next_button_and_go_to_step_3_playback_schedule()
        self.click_on_run_playlist_button()
        self.check_tag_name_play_changed_is_presented()
        self.make_screenshot_after_edit()

    def check_play_changed_is_not_presented(self):
        assert self.is_not_element_present(
            *PlaylistPageLocators.TAG_NAME_PLAY_CHANGED_IS_PRESENTED), \
            "PLAY CHANGED IS PRESENTED"

    def press_edit_playlist_button(self):
        edit_playlist_button = self.browser.find_element(*PlaylistPageLocators.EDIT_PLAYLIST_BUTTON)
        edit_playlist_button.click()

    def enter_new_tag_name_playlist_changed_in_add_tag_input(self):
        new_tag_input = self.browser.find_element(*PlaylistPageLocators.ADD_TAG_INPUT)
        new_tag_input.clear()
        new_tag_input.send_keys("PLAY_CHANGED")

    def check_tag_playlist_was_edited(self):
        assert self.is_element_present(*PlaylistPageLocators.CHECK_NEW_TAG_PLAY_CHANGED)

    def check_tag_name_play_changed_is_presented(self):
        assert self.is_element_present(*PlaylistPageLocators.TAG_NAME_PLAY_CHANGED_IS_PRESENTED)

    def make_screenshot_after_edit(self):
        self.browser.save_screenshot(
            SCREENSHOTS_DIR+"test_playlist_edit_new_playlist_mts_card_maket_1920_add_tag_play_changed.png")

    def delete_playlist_1920_mts_lime_maket(self):
        self.click_on_checkbox_first_playlist()
        self.check_checkbox_first_playlist_is_checked()
        self.click_on_delete_playlist_button()
        self.click_are_you_sure_yes_button()
        self.check_playlist_1920x158_mts_lime_maket_is_presented()
        self.check_is_playlist_deleted()

    def click_on_checkbox_first_playlist(self):
        checkbox_first__on_table_playlist = self.browser.find_element(*PlaylistPageLocators.CHECKBOX_FIRST_ROW_PLAYLIST)
        checkbox_first__on_table_playlist.click()

    def check_checkbox_first_playlist_is_checked(self):
        assert self.is_element_present(*PlaylistPageLocators.CHECKBOX_FIRST_ROW_PLAYLIST_IS_CHECKED)

    def click_on_delete_playlist_button(self):
        delete_playlist_button = self.browser.find_element(*PlaylistPageLocators.DELETE_PLAYLIST_BUTTON)
        ActionChains(self.browser).release(delete_playlist_button).click().perform()
        time.sleep(0.3)

    def click_are_you_sure_yes_button(self):
        are_you_sure_yes_button = self.browser.find_element(*PlaylistPageLocators.ARE_YOU_SURE_YES_BUTTON)
        ActionChains(self.browser).release(are_you_sure_yes_button).click().perform()

    def check_is_playlist_deleted(self):
        self.browser.refresh()
        self.browser.save_screenshot(SCREENSHOTS_DIR+'test_playlist_delete_new_playlist_mts_card_maket.png')

    def check_playlist_1920x158_mts_lime_maket_is_presented(self):
        assert self.browser.find_element(*PlaylistPageLocators.PLAYLIST_NAME_1920x158_MTS_LIME_MAKET_IS_PRESENTED)

    def preview_playlist_on_grid_view(self):
        self.click_on_grid_view_button()
        self.click_on_playlist_preview_button()

    def click_on_grid_view_button(self):
        grid_button = self.browser.find_element(*PlaylistPageLocators.GRID_VIEW_BUTTON)
        ActionChains(self.browser).release(grid_button).click().perform()

    def click_on_playlist_preview_button(self):
        preview_playlist_button = self.browser.find_element(*PlaylistPageLocators.PLAYLIST_PREVIEW_BUTTON)
        ActionChains(self.browser).release(preview_playlist_button).double_click().perform()
        time.sleep(0.1)
        VIDEO_SRC = self.browser.find_element(*PlaylistPageLocators.VIDEO_SRC_1920x158_MTS_LIME_MAKET)
        video = self.browser.find_element_by_tag_name('video').get_attribute("src")
        print(video)
        self.browser.get(video)
        source = self.browser.find_element_by_tag_name('source').get_attribute("src")
        assert source == video, \
            "Source src and video src are equal"
        self.browser.get(STAGE_PLAYLIST_URL)

    def get_playlist_id_1920_mts_lime_maket(self):
        playlist_id = self.browser.find_element_by_css_selector("tr[class='ant-table-row ant-table-row-level-0']")\
            .get_attribute("data-row-key")
        print('Playlist id =', playlist_id)
        change_playlist = self.browser.find_element(*PlaylistPageLocators.ACTION_CHANGE_PLAYLIST)
        change_playlist.click()
        assert playlist_id in self.browser.current_url, \
            "URL is not valid. Should be change_playlist page"
