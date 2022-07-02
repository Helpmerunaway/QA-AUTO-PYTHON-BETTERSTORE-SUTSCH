
from selenium.webdriver import ActionChains

from .base_page import BasePage
from tests.sutsch_ui.pages.locators import ForgotPasswordPageLocators
from tests.sutsch_ui.pages.locators import LoginPageLocators
from tests.sutsch_ui.pages.locators import OutlookPageLocators
from tests.sutsch_ui.pages.locators import ChangePasswordPageLocators
from tests.sutsch_ui.randomizer_eng import generated_password_eng, generated_password_rus
from tests.sutsch_ui.config import OUTLOOK_EMAIL_LOGIN, OUTLOOK_EMAIL_PASSWORD, STAGE_LOGIN_USER_1, \
    STAGE_PASSWORD_USER_1


class ForgotPasswordPage(BasePage):

    def click_on_forgot_password_button(self):
        forgot_password_button = self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        forgot_password_button.click()

    def should_be_forgot_password_page(self):
        self.should_be_forgot_password_page_url()
        self.should_be_forgot_password_page_open()

    def should_be_forgot_password_page_url(self):
        assert "forgot-password" in self.browser.current_url, \
            "URL is not valid"

    def should_be_forgot_password_page_open(self):
        assert "Восстановление пароля" in self.browser.title, \
            'This is not a forgot_password page'

    def should_be_forgot_password_elements_on_page(self):
        self.should_be_email_input()
        self.should_be_reset_password_button()

    def should_be_email_input(self):
        assert self.is_element_present(*ForgotPasswordPageLocators.EMAIL_INPUT), \
            "Email input is not presented"

    def should_be_reset_password_button(self):
        assert self.is_element_present(*ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON), \
            "Reset password button is not presented"

    def should_be_forgot_password_alert_window(self):
        self.enter_email()
        self.press_reset_password_and_check_alert_window()
        self.check_alert_message()

    def enter_email(self):
        enter_email = self.browser.find_element(*ForgotPasswordPageLocators.EMAIL_INPUT)
        enter_email.click()
        enter_email.clear()
        enter_email.send_keys(STAGE_LOGIN_USER_1)

    def press_reset_password_and_check_alert_window(self):
        reset_password = self.browser.find_element(*ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
        reset_password.click()
        assert self.is_element_present(*ForgotPasswordPageLocators.ALERT_WINDOW), \
            "Alert window is not presented"

    def check_alert_message(self):
        reset_password = self.browser.find_element(*ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
        reset_password.click()
        assert self.is_element_present(*ForgotPasswordPageLocators.ALERT_TEXT), \
            "Alert text is not presented"

    def mail_auth(self):
        self.outlook_authorization()

    def outlook_authorization(self):
        outlook_email = self.browser.find_element(*OutlookPageLocators.OUTLOOK_USERNAME_INPUT)
        outlook_email.click()
        outlook_email.clear()
        outlook_email.send_keys(OUTLOOK_EMAIL_LOGIN)
        outlook_password = self.browser.find_element(*OutlookPageLocators.OUTLOOK_PASSWORD_INPUT)
        outlook_password.click()
        outlook_password.clear()
        outlook_password.send_keys(OUTLOOK_EMAIL_PASSWORD)
        outlook_sign_in = self.browser.find_element(*OutlookPageLocators.OUTLOOK_SIGN_IN)
        outlook_sign_in.click()
        outlook_user_menu = self.browser.find_element(*OutlookPageLocators.OUTLOOK_TITLE)
        assert self.is_element_present(*OutlookPageLocators.OUTLOOK_TITLE)
        return outlook_user_menu

    def check_hyperlink_and_open_change_password_page(self):
        self.find_restore_message_in_outlook()
        self.should_be_change_page_title()

    def find_restore_message_in_outlook(self):
        outlook_shelftalker_dir = self.browser.find_element(*OutlookPageLocators.OUTLOOK_SHELF_TALKER_DIR)
        outlook_shelftalker_dir.click()
        outlook_hyperlink = self.browser.find_element(*OutlookPageLocators.OUTLOOK_HYPERLINK)

        ActionChains(self.browser).move_to_element(outlook_hyperlink).click().perform()
        href_link = self.browser.find_element(*OutlookPageLocators.HREF_LINK)
        ActionChains(self.browser).move_to_element(href_link).click_and_hold().click().perform()
        self.browser.switch_to.window(self.browser.window_handles[-1])

    def should_be_change_page_title(self):
        assert self.is_element_present(*ChangePasswordPageLocators.CHANGE_PASSWORD_TITLE), \
            "Смена пароля title is not presented"

    def should_be_change_page_elements(self):
        self.should_be_new_password_input()
        self.should_be_repeat_password_input()
        self.should_be_save_password_button()

    def should_be_new_password_input(self):
        assert self.is_element_present(*ChangePasswordPageLocators.NEW_PASSWORD_INPUT), \
            "New password input is not presented"

    def should_be_repeat_password_input(self):
        assert self.is_element_present(*ChangePasswordPageLocators.REPEAT_PASSWORD_INPUT), \
            "Repeat password input is not presented"

    def should_be_save_password_button(self):
        assert self.is_element_present(*ChangePasswordPageLocators.SAVE_PASSWORD_BUTTON), \
            "Save password button is not presented"

    def negative_password_do_not_match(self):
        self.negative_passwords_dont_match()
        assert self.is_disappeared(*ChangePasswordPageLocators.ALERT_MESSAGE_TEXT_DONT_MATCH), \
            "Alert message passwords dont match has not disappeared"

    def negative_passwords_dont_match(self):
        new_password_input = self.browser.find_element(*ChangePasswordPageLocators.NEW_PASSWORD_INPUT)
        new_password_input.click()
        new_password_input.clear()
        new_password_input.send_keys('assd')
        repeat_password_input = self.browser.find_element(*ChangePasswordPageLocators.REPEAT_PASSWORD_INPUT)
        repeat_password_input.click()
        repeat_password_input.clear()
        repeat_password_input.send_keys('7777777')
        save_password = self.browser.find_element(*ChangePasswordPageLocators.SAVE_PASSWORD_BUTTON)
        save_password.click()
        assert self.is_not_element_present(*ChangePasswordPageLocators.ALERT_MESSAGE_TEXT_WAS_CHANGED), \
            "Alert message 'Пароль изменен' was presented"
        assert self.is_element_present(*ChangePasswordPageLocators.ALERT_MESSAGE), \
            "Alert message is not presented"
        assert self.is_element_present(*ChangePasswordPageLocators.ALERT_MESSAGE_TEXT_DONT_MATCH), \
            "Alert message is wrong. Must be: 'Пароли не совпадают'"

    def negative_passwords_to_short(self):
        self.negative_password_too_short()
        assert self.is_disappeared(*ChangePasswordPageLocators.ALERT_MESSAGE_TEXT_TOO_SHORT), \
            "Alert message 'Пароль слишком короткий' has not disappeared"

    def negative_password_too_short(self):
        new_password_input = self.browser.find_element(*ChangePasswordPageLocators.NEW_PASSWORD_INPUT)
        new_password_input.click()
        new_password_input.clear()
        new_password_input.send_keys('qwe')
        repeat_password_input = self.browser.find_element(*ChangePasswordPageLocators.REPEAT_PASSWORD_INPUT)
        repeat_password_input.click()
        repeat_password_input.clear()
        repeat_password_input.send_keys('987')
        save_password = self.browser.find_element(*ChangePasswordPageLocators.SAVE_PASSWORD_BUTTON)
        save_password.click()
        assert self.is_element_present(*ChangePasswordPageLocators.ALERT_MESSAGE), \
            "Alert message is not presented"
        assert self.is_element_present(*ChangePasswordPageLocators.ALERT_MESSAGE_TEXT_TOO_SHORT), \
            "Alert message is wrong. Must be: 'Недопустимая длина пароля'"

    def negative_random_password(self):
        self.negative_randomly_generated_password()
        assert self.is_element_present(*ChangePasswordPageLocators.ALERT_MESSAGE), \
            "Alert message is not presented"

    def negative_randomly_generated_password(self):
        new_password_input = self.browser.find_element(*ChangePasswordPageLocators.NEW_PASSWORD_INPUT)
        new_password_input.click()
        new_password_input.send_keys(generated_password_eng)
        print('new password = ', generated_password_eng)
        repeat_password_input = self.browser.find_element(*ChangePasswordPageLocators.REPEAT_PASSWORD_INPUT)
        repeat_password_input.click()
        repeat_password_input.send_keys(generated_password_rus)
        print('repeat_password =', generated_password_rus)
        save_password = self.browser.find_element(*ChangePasswordPageLocators.SAVE_PASSWORD_BUTTON)
        save_password.click()

    def check_enter_and_save_new_password(self):
        self.enter_new_password_input()
        self.press_save_password_button_valid()

    def enter_new_password_input(self):
        new_password_input = self.browser.find_element(*ChangePasswordPageLocators.NEW_PASSWORD_INPUT)
        new_password_input.click()
        new_password_input.clear()
        new_password_input.send_keys(STAGE_PASSWORD_USER_1)
        repeat_password_input = self.browser.find_element(*ChangePasswordPageLocators.REPEAT_PASSWORD_INPUT)
        repeat_password_input.click()
        repeat_password_input.clear()
        repeat_password_input.send_keys(STAGE_PASSWORD_USER_1)

    def press_save_password_button_valid(self):
        save_password = self.browser.find_element(*ChangePasswordPageLocators.SAVE_PASSWORD_BUTTON)
        save_password.click()
        assert self.is_element_present(*ChangePasswordPageLocators.ALERT_MESSAGE_TEXT_WAS_CHANGED), \
            "Alert message 'Пароль изменен' is not presented"
        assert self.is_disappeared(*ChangePasswordPageLocators.ALERT_MESSAGE_TEXT_WAS_CHANGED), \
            "Alert message with text 'Пароль изменен' wasnt disappeared"
        assert "auth" in self.browser.current_url, \
            "Wrong URL. Must be auth URL"
















