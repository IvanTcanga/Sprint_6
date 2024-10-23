import allure
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import *
import pytest


class TestOrderPageOrder:

    @allure.title('Проверка флоу позитивного сценария с двумя наборами данных')
    @allure.description('Проверка точек входа в сценарий: кнопка «Заказать» вверху страницы и внизу.')
    @pytest.mark.parametrize('button, test_user', [(MainPageLocators.ORDER_BUTTON_HEADER, DataForTests.test_user_1),
                                                   (MainPageLocators.ORDER_BUTTON_MAIN, DataForTests.test_user_2)])
    def test_order_all_fields_success(self, driver, button, test_user):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.find_element_with_wait(button)
        order_page.click_to_element(button)
        order_page.data_entry_first_form(test_user)
        order_page.data_entry_second_form(test_user)
        assert order_page.check_status_order_displayed()
