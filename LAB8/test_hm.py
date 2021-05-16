import threading
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_rodo(driver):
    try:
        element = WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )
        element.click()
    except:
        print("NIE MA RODO")


def wait_for_rodo_async(driver):
    thread = threading.Thread(target=wait_for_rodo, args=[driver])
    thread.start()


def open_hm():
    driver = webdriver.Chrome(executable_path="../lib/chromedriver.exe")
    url = "https://www2.hm.com/"
    driver.maximize_window()
    driver.get(url)
    wait_for_rodo_async(driver)
    return driver


# driver = open_zalando()


def search(driver, phrase):
    search_input = driver.find_element_by_id("main-search")
    search_input.send_keys(phrase)
    search_input.send_keys(Keys.ENTER)


def click_on_first_element(driver):
    driver.find_elements_by_class_name("image-container")[0].click()


def add_to_basket(driver):
    driver.find_elements_by_class_name("product-item-buttons")[0].click()
    driver.find_elements_by_class_name("option")[1].click()
    random_element = driver.find_element_by_tag_name("body")
    ActionChains(driver).move_to_element(random_element).perform()
    driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[1]/button").click()


def go_to_basket(driver):
    basket_button = driver.find_element_by_xpath("//a[@title='Koszyk']")
    basket_button.click()


def bucket_count_is_more_than_zero(driver):
    time.sleep(2)
    bucket_count = driver.find_element_by_class_name("shoppingbag-item-count").get_attribute("innerHTML")
    return len(bucket_count) > 0


test_data = ["kid", "jacket"]


def choose_language(driver):
    driver.find_element_by_id("link_en_us").click()


@pytest.mark.parametrize("phrase", test_data)
def test_add_to_basket(phrase):
    driver = open_hm()
    choose_language(driver)
    search(driver, phrase)
    click_on_first_element(driver)

    add_to_basket(driver)
    assert bucket_count_is_more_than_zero(driver)
    driver.quit()


# test_register_and_add_to_basket("kid")

# test_add_to_basket()
