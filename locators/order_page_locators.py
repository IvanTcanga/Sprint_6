from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма "Для кого самокат"
    TITLE_SCOOTER_INFO = (By.XPATH, "//div[text()='Для кого самокат']")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LASTNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    SELECTOR_METRO = (By.XPATH, "//button[@value='1']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    # Форма "Про аренду"
    TITLE_RENT = (By.XPATH, "//div[text()='Про аренду']")
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_SELECTOR = (By.XPATH, "//*[@class='react-datepicker-popper']")
    DAY_RENT = (By.XPATH, "//div[text()='30']")
    FIELD_RENTAL_PERIOD = (By.XPATH, ".//div[text()='* Срок аренды']")
    RENTAL_DAY = (By.XPATH, "//div[@class = 'Dropdown-menu']/div[text() ='сутки']")
    CHECKBOX_GREY = (By.XPATH, "//input[@id='grey']")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    # Подтверждение заказа
    BUTTON_CONFIRM = (By.XPATH, "//button[text()='Да']")
    BUTTON_STATUS_ORDER = (By.XPATH, ".//button[text()='Посмотреть статус']")

    # coockie
    CONFIRM_COOCKIE = (By.XPATH, "//button[text()='да все привыкли']")
