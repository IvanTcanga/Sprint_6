from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step('Кликаем на вопрос')
    def click_to_question(self, locator_q_formatted):
        self.scroll_to_element(MainPageLocators.LAST_QUESTION_BUTTON)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получаем текст с ответа по номеру вопроса')
    def get_answer_text(self, number_of_question):
        formatted_question_button = self.format_locators(MainPageLocators.QUESTION_BUTTON, number_of_question)
        formatted_answer_button = self.format_locators(MainPageLocators.ANSWER_P, number_of_question)

        self.scroll_to_element(MainPageLocators.LAST_QUESTION_BUTTON)
        self.click_to_question(formatted_question_button)
        return self.get_text_from_element(formatted_answer_button)

    @allure.step('Подождать прогрузки лого с надписью "Самокат" в хэдере')
    def wait_visibility_of_header_logo_scooter(self):
        self.find_element_with_wait(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Подождать прогрузки лого с надписью "Яндекс" в хэдере')
    def wait_visibility_of_header_logo_yandex(self):
        self.find_element_with_wait(MainPageLocators.LOGO_YANDEX)

    @allure.step('Кликнуть по части лого с надписью "Самокат" в хэдере')
    def click_on_header_logo_scooter(self):
        self.click_to_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Кликнуть по части лого с надписью "Яндекс" в хэдере')
    def click_on_header_logo_yandex(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Подождать прогрузки кнопки "Заказать" в хэдере')
    def wait_visibility_of_order_button_in_header(self):
        self.find_element_with_wait(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Кликнуть по кнопке "Заказать" в хэдере')
    def click_on_order_button_in_header(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Сравниваем current_url с base_url')
    def current_url_is_base_url(self):
        return self.get_current_url() == DataForTests.BASE_URL
