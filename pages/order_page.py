import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import DataForTests


class OrderPage(BasePage):

    @allure.step('Клик по станции метро')
    def select_station(self):
        self.click_to_element(OrderPageLocators.METRO_FIELD)
        self.click_to_element(OrderPageLocators.SELECTOR_METRO)

    @allure.step('Выбор даты "Когда привезти самокат"')
    def sending_data_to_date_field(self):
        self.send_keys_to_input(OrderPageLocators.DATE_FIELD).send_keys(DataForTests.test_user_1[4])

    @allure.step('Клик для выбора срока аренды')
    def click_date_in_calendar(self):
        self.find_element_with_wait(OrderPageLocators.DATE_FIELD)
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        self.find_element_with_wait(OrderPageLocators.DATE_SELECTOR)
        self.click_to_element(OrderPageLocators.DAY_RENT)

    @allure.step('Проверка,что есть кнопка "Посмотреть статус"')
    def check_status_order_displayed(self):
        return self.check_displaying_of_element(OrderPageLocators.BUTTON_STATUS_ORDER)

    @allure.step('Заполнение первой формы + Далее')
    def data_entry_first_form(self, test_data):
        self.find_element_with_wait(OrderPageLocators.NAME_FIELD)
        self.click_to_element(OrderPageLocators.NAME_FIELD)
        self.send_keys_to_input(OrderPageLocators.NAME_FIELD, test_data[0])
        self.click_to_element(OrderPageLocators.LASTNAME_FIELD)
        self.send_keys_to_input(OrderPageLocators.LASTNAME_FIELD, test_data[1])
        self.click_to_element(OrderPageLocators.ADDRESS_FIELD)
        self.send_keys_to_input(OrderPageLocators.ADDRESS_FIELD, test_data[2])
        self.select_station()
        self.click_to_element(OrderPageLocators.PHONE_FIELD)
        self.send_keys_to_input(OrderPageLocators.PHONE_FIELD, test_data[3])
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение второй формы + подтверждение заказа')
    def data_entry_second_form(self, test_data):
        self.click_date_in_calendar()
        self.click_to_element(OrderPageLocators.CHECKBOX_GREY)
        self.click_to_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.RENTAL_DAY)
        self.click_to_element(OrderPageLocators.COMMENT_FIELD)
        self.send_keys_to_input(OrderPageLocators.CHECKBOX_GREY, test_data[-1])
        self.click_to_element(OrderPageLocators.BUTTON_ORDER)
        self.find_element_with_wait(OrderPageLocators.BUTTON_CONFIRM)
        self.click_to_element(OrderPageLocators.BUTTON_CONFIRM)
