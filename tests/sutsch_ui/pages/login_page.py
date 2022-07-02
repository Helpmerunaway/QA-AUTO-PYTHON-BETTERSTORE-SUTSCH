from .base_page import BasePage
from tests.sutsch_ui.pages.locators import LoginPageLocators
from tests.sutsch_ui.pages.locators import MainPageLocators
from tests.sutsch_ui.config import STAGE_PASSWORD_USER_2, STAGE_LOGIN_USER_1, \
    STAGE_PASSWORD_USER_1, STAGE_LOGIN_USER_2
from allure_commons._allure import step


class LoginPage(BasePage):
    def should_be_login_page(self):
        step1_title = "В URL адресе должен присутствовать /auth"
        with step(step1_title):
            self.should_be_auth_url()
        step2_title = "Должна быть открыта страница авторизации"
        with step(step2_title):
            self.should_be_auth_page_open()

    def should_be_auth_url(self):
        assert 'auth' in self.browser.current_url, \
            "URL is not valid. Must be auth page"

    def should_be_auth_page_open(self):
        assert 'Авторизация' in self.browser.title, \
            "This is not a authorization page"

    def should_be_login_page_elements(self):
        step1_title = "Должен присутствовать элемент поле логина"
        with step(step1_title):
            self.should_be_login_form()
        step2_title = "Должен присутствовать элемент поле пароля"
        with step(step2_title):
            self.should_be_password_form()
        step3_title = "Должен присутствовать элемент показать пароль"
        with step(step3_title):
            self.should_be_password_view_button()
        step4_title = "Должен присутствовать элемент запомнить меня"
        with step(step4_title):
            self.should_be_remember_me_button()
        step5_title = "Должен присутствовать элемент войти"
        with step(step5_title):
            self.should_be_enter_button()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT), \
            "Login input form is not presented"

    def should_be_password_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT), \
            "Password input form is not presented"

    def should_be_password_view_button(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_VIEW_BUTTON), \
            "Password view button is not presented"

    def should_be_remember_me_button(self):
        assert self.is_element_present(*LoginPageLocators.CHECKBOX_REMEMBER_ME), \
            "Button 'remember me' is not presented"

    def should_be_enter_button(self):
        assert self.is_element_present(*LoginPageLocators.ENTER_STAGE_BUTTON), \
            "Enter button is not presented"

    def click_on_buttons(self):
        step1_title = "Клик по кнопке запомнить меня"
        with step(step1_title):
            self.click_on_remember_me()
        step2_title = "Клик по кнопке показать пароль"
        with step(step2_title):
            self.click_on_view_password()
        step3_title = "Клик по кнопке забыли пароль"
        with step(step3_title):
            self.click_on_forgot_password()

    def click_on_remember_me(self):
        remember_me_button = self.browser.find_element(*LoginPageLocators.CHECKBOX_REMEMBER_ME)
        remember_me_button.click()
        assert self.is_element_present(*LoginPageLocators.REMEMBER_ME_IS_CHECKED), \
            "Remember me is not checked"

    def click_on_view_password(self):
        password_view = self.browser.find_element(*LoginPageLocators.PASSWORD_VIEW_BUTTON)
        password_view.click()
        assert self.is_element_present(*LoginPageLocators.PASSWORD_VIEW_IS_CHECKED), \
            "Password view is not checked"

    def click_on_forgot_password(self):
        forgot_password = self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        forgot_password.click()
        assert 'Восстановление пароля' in self.browser.title, \
            "This is not a forgot password"

    def do_login(self):
        step1_title = "Ввод логина в поле логин"
        with step(step1_title):
            self.input_login_email()
        step2_title = "Ввод пароля в поле пароль"
        with step(step2_title):
            self.input_password()
        step3_title = "Клик по кнопке войти"
        with step(step3_title):
            self.press_enter_button()
        step4_title = "Проверка наличия меню с именем пользователя"
        with step(step4_title):
            self.check_user_container()

    def input_login_email(self):
        input_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT)
        input_email.click()
        input_email.clear()
        input_email.send_keys(STAGE_LOGIN_USER_1)

    def input_password(self):
        input_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT)
        input_password.click()
        input_password.clear()
        input_password.send_keys(STAGE_PASSWORD_USER_1)

    def do_login_user_2(self):
        step1_title = "Ввод логина пользователя в поле логин"
        with step(step1_title):
            self.input_login_email_user_2()
        step2_title = "Ввод пароля пользователя в поле пароль"
        with step(step2_title):
            self.input_password_user_2()
        step3_title = "Клик по кнопке войти"
        with step(step3_title):
            self.press_enter_button()
        step4_title = "Проверка наличия меню с именем пользователя"
        with step(step4_title):
            self.check_user_container()

    def input_login_email_user_2(self):
        input_email_user_2 = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT)
        input_email_user_2.click()
        input_email_user_2.clear()
        input_email_user_2.send_keys(STAGE_LOGIN_USER_2)

    def input_password_user_2(self):
        input_password_user_2 = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT)
        input_password_user_2.click()
        input_password_user_2.clear()
        input_password_user_2.send_keys(STAGE_PASSWORD_USER_2)

    def press_enter_button(self):
        enter_button = self.browser.find_element(*LoginPageLocators.ENTER_STAGE_BUTTON)
        enter_button.click()

    def check_user_container(self):
        assert self.is_element_present(*MainPageLocators.USER_CONTAINER), \
            "User is not authorized"

    def fake_password(self):
        step1_title = "Ввод логина в поле логин"
        with step(step1_title):
            self.input_login_email()
        step2_title = "Ввод неверного пароля в поле пароль"
        with step(step2_title):
            self.invalid_password_input()
        step3_title = "Клик по кнопке войти"
        with step(step3_title):
            self.press_enter_button()
        step4_title = "Сообщение об ошибке: неверный логин или пароль"
        with step(step4_title):
            self.check_alert_invalid_login_or_password()
        step5_title = "Пользователь находится на странице авторизации"
        with step(step5_title):
            self.should_be_auth_url()

    def invalid_password_input(self):
        input_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT)
        input_password.click()
        input_password.clear()
        input_password.send_keys('fake')

    def check_alert_invalid_login_or_password(self):
        assert self.is_element_present(*LoginPageLocators.ALERT_MESSAGE_INVALID_LOGIN_OR_PASSWORD)

    def fake_email(self):
        step1_title = "Ввод неверного логина в поле логин"
        with step(step1_title):
            self.invalid_email_input()
        step2_title = "Ввод пароля в поле пароль"
        with step(step2_title):
            self.input_password()
        step3_title = "Клик по кнопке войти"
        with step(step3_title):
            self.press_enter_button()
        step4_title = "Сообщение об ошибке: неверный логин или пароль"
        with step(step4_title):
            self.check_alert_invalid_login_or_password()
        step5_title = "Пользователь находится на странице авторизации"
        with step(step5_title):
            self.should_be_auth_url()

    def invalid_email_input(self):
        input_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT)
        input_email.click()
        input_email.clear()
        input_email.send_keys("V.Pupkin@mail.ru")



