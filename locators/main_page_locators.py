from selenium.webdriver.common.by import By


class MainPageLocators:

    # вопросы и ответы
    QUESTION_BUTTON = By.XPATH, '//*[@aria-controls="accordion__panel-{}"]'
    ANSWER_P = By.XPATH, '//*[@id="accordion__panel-{}"]'
    LAST_QUESTION_BUTTON = By.XPATH, '//*[@aria-controls="accordion__panel-7"]'

    # кнопки "Заказать"
    ORDER_BUTTON_HEADER = (By.XPATH, '//button[ text()="Заказать" ]')
    ORDER_BUTTON_MAIN = (By.XPATH, '//button[text()="Заказать" and contains(@class, "Button_UltraBig__UU3Lp")]')

    # лого в шапке
    LOGO_SCOOTER = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    LOGO_YANDEX = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
