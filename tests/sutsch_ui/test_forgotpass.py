from tests.sutsch_ui.pages.forgot_password_page import ForgotPasswordPage
import pytest
import allure
from tests.sutsch_ui.config import auth_link, email_link, enter_link




@allure.title('TEST: Проверка сброса пароля /forgot-password')
@pytest.mark.forgot_pass
def test_reset_password_second(browser):
    """
    Предусловия:
    Пользователь находится на странице авторизация
    Шаги:
    1. Нажать на кнопку "Забыли пароль"
    2. Ввести email в поле "E-mail"
    3. Нажать на кнопку "Сбросить пароль"
    Ожидаемый результат:
    Всплывающее окно с информацией: "В течение нескольких минут на адрес
    придет письмо с инструкциями по восстановлению пароля"
    Пользователь попадает на страницу "Авторизация"
    """
    page = ForgotPasswordPage(browser, auth_link)
    page.open()
    page.click_on_forgot_password_button()
    page.should_be_forgot_password_alert_window()


@allure.title('TEST: Проверяем та ли это страница: /forgot-password')
@pytest.mark.forgot_pass
def test_forgot_password_is_open(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу "Восстановление пароля"
    2. URL страницы содержит /forgot-password
    3. Заголовок страницы содержит "Восстановление пароля"
    Ожидаемый результат:
    Пользователь находится на странице "Восстановление пароля"
    """
    page = ForgotPasswordPage(browser, auth_link)
    page.open()
    page.click_on_forgot_password_button()
    page.should_be_forgot_password_page()


@allure.title('TEST: Проверка наличия элементов /forgot-password')
@pytest.mark.forgot_pass
def test_forgot_password_page_check_elements(browser):
    """
    Предусловия:
    Пользователь не авторизован в системе
    Шаги:
    1. Открыть страницу /forgot-password
    2. URL страницы содержит /forgot-password
    3. Проверка наличия элементов, кнопок и полей на странице /forgot-password
    Ожидаемый результат:
    Веб-элементы страницы присутствуют"
    """
    page = ForgotPasswordPage(browser, auth_link)
    page.open()
    page.click_on_forgot_password_button()
    page.should_be_forgot_password_elements_on_page()


@allure.title('TEST: Проверка сброса пароля /forgot-password')
@pytest.mark.forgot_pass
def test_reset_password(browser):
    """
    Предусловия:
    Пользователь находится на странице авторизация
    Шаги:
    1. Нажать на кнопку "Забыли пароль"
    2. Ввести email в поле "E-mail"
    3. Нажать на кнопку "Сбросить пароль"
    Ожидаемый результат:
    Всплывающее окно с информацией: "В течение нескольких минут на адрес
    придет письмо с инструкциями по восстановлению пароля"
    Пользователь попадает на страницу "Авторизация"
    """
    page = ForgotPasswordPage(browser, auth_link)
    page.open()
    page.click_on_forgot_password_button()
    page.should_be_forgot_password_alert_window()


@allure.title('TEST: Проверка гиперссылки и элементов на странице /change_password')
@pytest.mark.forgot_pass
def test_hyperlink_and_change_password_page(browser, reset_password_ui_link_to_email):
    """
    Предусловия:
    Пользователь отправил письмо с восстановлением пароля на электронный ящик
    Шаги:
    1. Открыть сайт электронной почты
    2. Найти письмо с инструкцией о смене пароля
    3. Перейти по ссылке в письме
    4. Открыть страницу "Смена пароля"
    5. Проверка наличия элементов, кнопок и полей
    Ожидаемый результат:
    Веб-элементы страницы присутствуют
    """
    page = ForgotPasswordPage(browser, email_link)
    page.open()
    page.mail_auth()
    page = ForgotPasswordPage(browser, enter_link)
    page.open()
    page.check_hyperlink_and_open_change_password_page()
    page.should_be_change_page_elements()


@allure.title('TEST: Несовпадающие пароли /forgot_password')
@pytest.mark.forgot_pass
def test_passwords_do_not_match(browser, reset_password_ui_link_to_email):
    """
    Предусловия:
    Пользователь отправил письмо с восстановлением пароля на электронный ящик
    Шаги:
    1. Открыть сайт электронной почты
    2. Найти письмо с инструкцией о смене пароля
    3. Перейти по ссылке в письме
    4. Открыть страницу "Смена пароля"
    5. Ввести пароль в поле "Новый пароль"
    6. Ввести пароль,отличающийся от введенного в п.5 в поле "Повторите пароль"
    7. Нажать на кнопку "Сохранить пароль"
    Ожидаемый результат:
    Всплывающее окно: "Пароли не совпадают"
    """
    page = ForgotPasswordPage(browser, email_link)
    page.open()
    page.mail_auth()
    page.check_hyperlink_and_open_change_password_page()
    page.negative_password_do_not_match()
    # баг: не совпадающие пароли принимаются системой 23.05.2022


@allure.title('TEST: Слишком короткий пароль /forgot_password')
@pytest.mark.forgot_pass
def test_passwords_too_short(browser, reset_password_ui_link_to_email):
    """
    Предусловия:
    Пользователь отправил письмо с восстановлением пароля на электронный ящик
    Шаги:
    1. Открыть сайт электронной почты
    2. Найти письмо с инструкцией о смене пароля
    3. Перейти по ссылке в письме
    4. Открыть страницу "Смена пароля"
    5. Ввести пароль меньше 4 символов в поле "Новый пароль" и в поле "Повторите пароль"
    6. Нажать на кнопку "Сохранить пароль"
    Ожидаемый результат:
    Всплывающее окно: "Недопустимая длина пароля"
    """
    page = ForgotPasswordPage(browser, email_link)
    page.open()
    page.mail_auth()
    page.check_hyperlink_and_open_change_password_page()
    page.negative_passwords_to_short()


@allure.title('TEST: Слишком короткий пароль /forgot_password')
@pytest.mark.forgot_pass
def test_random_passwords(browser, reset_password_ui_link_to_email):
    """
    Предусловия:
    Пользователь отправил письмо с восстановлением пароля на электронный ящик
    Шаги:
    1. Открыть сайт электронной почты
    2. Найти письмо с инструкцией о смене пароля
    3. Перейти по ссылке в письме
    4. Открыть страницу "Смена пароля"
    5. Ввести сгенерированный пароль в поле "Новый пароль" и в поле "Повторите пароль"
    6. Нажать на кнопку "Сохранить пароль"
    Ожидаемый результат:
    Всплывающее окно: "Пароли не совпадают"
    """
    page = ForgotPasswordPage(browser, email_link)
    page.open()
    page.mail_auth()
    page.check_hyperlink_and_open_change_password_page()
    page.negative_random_password()


@allure.title('TEST: Проверка смены пароля /change_password')
@pytest.mark.forgot_pass
def test_restore_password(browser, reset_password_ui_link_to_email):
    """
    Предусловия:
    Пользователь отправил письмо с восстановлением пароля на электронный ящик
    Шаги:
    1. Открыть сайт электронной почты
    2. Найти письмо с инструкцией о смене пароля
    3. Перейти по ссылке в письме
    4. Открыть страницу "Смена пароля"
    6. Ввести пароль в поле "Новый пароль"
    7. Повторить пароль в поле "Повторите пароль"
    8. Нажать на кнопку "Сохранить пароль"
    Ожидаемый результат:
    Всплывающее окно: "Пароль успешно изменен. Вы будете перенаправлены на
    страницу авторизации в течении нескольких секунд."
    Пользователь попадет на страницу авторизации
    """
    page = ForgotPasswordPage(browser, email_link)
    page.open()
    page.mail_auth()
    page.check_hyperlink_and_open_change_password_page()
    page.check_enter_and_save_new_password()



