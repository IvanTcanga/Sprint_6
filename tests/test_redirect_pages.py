import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import DataForTests


class TestLogoRedirect:
    @allure.title('Проверка, при клике на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_logo_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.find_element_with_wait(MainPageLocators.LOGO_SCOOTER)
        main_page.click_to_element(MainPageLocators.ORDER_BUTTON_HEADER)
        main_page.find_element_with_wait(MainPageLocators.LOGO_SCOOTER)
        main_page.click_to_element(MainPageLocators.LOGO_SCOOTER)
        main_page.find_element_with_wait(MainPageLocators.LOGO_SCOOTER)
        assert driver.current_url == DataForTests.BASE_URL

    @allure.title('Проверка,при клике на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_logo_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.find_element_with_wait(MainPageLocators.LOGO_YANDEX)
        main_page.click_to_element(MainPageLocators.LOGO_YANDEX)
        main_page.switch_to_next_tab()
        assert 'dzen' in driver.current_url
