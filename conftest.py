import pytest
from selenium import webdriver
from data import DataForTests


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(DataForTests.BASE_URL)
    yield driver
    driver.quit()
