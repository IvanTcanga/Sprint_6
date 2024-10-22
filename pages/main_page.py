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
