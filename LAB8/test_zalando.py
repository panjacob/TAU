import threading

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_rodo(driver):
    try:
        element = WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.ID, "uc-btn-accept-banner"))
        )
        element.click()
    except:
        print("NIE MA RODO")


def wait_for_rodo_async(driver):
    thread = threading.Thread(target=wait_for_rodo, args=[driver])
    thread.start()


def open_zalando():
    driver = webdriver.Chrome(executable_path="../lib/chromedriver.exe")
    url = "https://www.zalando.pl/"
    driver.maximize_window()
    driver.get(url)
    wait_for_rodo_async(driver)
    return driver


# driver = open_zalando()


def search(driver, phrase):
    search_input = driver.find_element_by_name("q")
    search_input.send_keys(phrase)
    search_input.send_keys(Keys.ENTER)


def click_on_first_element(driver):
    driver.find_elements_by_class_name("heWLCX")[0].click()


def add_to_basket(driver):
    add_to_basket_button = driver.find_element_by_xpath("//button[@aria-label='Dodaj do koszyka']")
    add_to_basket_button.click()


def go_to_basket(driver):
    basket_button = driver.find_element_by_xpath("//a[@title='Koszyk']")
    basket_button.click()


def is_phrase_in_basket(driver, phrase):
    found_phrases = driver.find_elements_by_xpath(f"//a[contains(text(), '{phrase}')]")
    return len(found_phrases) > 0


test_data = ["Casio", "Bidon"]


@pytest.mark.parametrize("phrase", test_data)
def test_add_to_basket(phrase):
    driver = open_zalando()
    search(driver, phrase)
    click_on_first_element(driver)
    add_to_basket(driver)
    go_to_basket(driver)
    assert is_phrase_in_basket(driver, phrase)
    driver.quit()


# test_add_to_basket()
