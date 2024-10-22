import allure
import pytest
from data import DataForTests
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    @pytest.mark.parametrize(
        'number_of_question, answer',
        [
            (0, DataForTests.ANSWERS_TEXT[0]),
            (1, DataForTests.ANSWERS_TEXT[1]),
            (2, DataForTests.ANSWERS_TEXT[2]),
            (3, DataForTests.ANSWERS_TEXT[3]),
            (4, DataForTests.ANSWERS_TEXT[4]),
            (5, DataForTests.ANSWERS_TEXT[5]),
            (6, DataForTests.ANSWERS_TEXT[6]),
            (7, DataForTests.ANSWERS_TEXT[7])
        ]
    )
    def test_answers_from_questions_is_answers_from_answers_text(self, driver, number_of_question, answer):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(number_of_question) == answer
