import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Подождать загрузку элемента')
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Добавить текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получить текст из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Форматирование локаторов согласно номеру вопроса')
    def format_locators(self, locator, number_of_question):
        method, locator = locator
        locator = locator.format(number_of_question)
        return method, locator

    @allure.step('Ввести значение в поле ввода')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Переключиться на новое окно')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Определить текущий URL')
    def get_current_url(self):
        return self.driver.current_url
