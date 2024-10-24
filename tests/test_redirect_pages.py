import allure
from pages.main_page import MainPage


class TestLogoRedirect:
    @allure.title('Проверка, при клике на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def test_logo_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_header_logo_scooter()
        assert main_page.current_url_is_base_url()

    @allure.title('Проверка,при клике на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена')
    def test_logo_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        assert 'dzen' in main_page.get_current_url()
