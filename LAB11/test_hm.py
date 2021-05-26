import logging
import threading
import time

logging.basicConfig(format='%(asctime)s %(message)s', filename='test_hm.log', encoding='utf-8', level=logging.DEBUG)


import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_rodo(driver):
    logging.info("wait_for_rodo() - start")
    try:
        logging.debug("wait_for_rodo() - try")
        element = WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )
        element.click()
    except:
        logging.warning("wait_for_rodo() - failed")
        print("NIE MA RODO")
        return
    logging.info("wait_for_rodo() - success")


def wait_for_rodo_async(driver):
    thread = threading.Thread(target=wait_for_rodo, args=[driver])
    thread.start()


def open_hm():
    logging.info("open_hm() - start")
    logging.debug("starting driver")
    driver = webdriver.Chrome(executable_path="../lib/chromedriver.exe")
    url = "https://www2.hm.com/"
    logging.debug("maximizing window")
    driver.maximize_window()
    logging.debug("opening url")
    driver.get(url)
    wait_for_rodo_async(driver)
    logging.debug("open_hm() - return")
    return driver


# driver = open_zalando()


def search(driver, phrase):
    logging.info("search() - start")
    logging.debug('driver.find_element_by_id("main-search)')
    search_input = driver.find_element_by_id("main-search")
    driver.find_element_by_id("sending keys to main-search")
    search_input.send_keys(phrase)
    driver.find_element_by_id("enter - main-search")
    search_input.send_keys(Keys.ENTER)


def click_on_first_element(driver):
    logging.info('click_on_first_element() - start')
    driver.find_element_by_id("click_on_first_element() - start")
    driver.find_elements_by_class_name("image-container")[0].click()


def add_to_basket(driver):
    logging.info('add_to_basket() - start')
    driver.find_element_by_id("add_to_basket() - start")
    driver.find_elements_by_class_name("product-item-buttons")[0].click()
    logging.debug('driver.find_elements_by_class_name("product-item-buttons")[0].click()')
    driver.find_elements_by_class_name("option")[1].click()
    logging.debug('driver.find_elements_by_class_name("option")[1].click()')
    random_element = driver.find_element_by_tag_name("body")
    logging.debug('random_element = driver.find_element_by_tag_name("body")')
    ActionChains(driver).move_to_element(random_element).perform()
    logging.debug('ActionChains(driver).move_to_element(random_element).perform()')
    driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[1]/button").click()
    logging.debug('driver.find_element_by_xpath("/html/body/main/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[1]/button").click()')


def go_to_basket(driver):
    basket_button = driver.find_element_by_xpath("//a[@title='Koszyk']")
    basket_button.click()


def bucket_count_is_more_than_zero(driver):
    time.sleep(2)
    bucket_count = driver.find_element_by_class_name("shoppingbag-item-count").get_attribute("innerHTML")
    return len(bucket_count) > 0


test_data = ["kid", "jacket"]


def choose_language(driver):
    logging.info("choose_language() - start")
    driver.find_element_by_id("link_en_us").click()


@pytest.mark.parametrize("phrase", test_data)
def test_add_to_basket(phrase):
    driver = open_hm()
    choose_language(driver)
    search(driver, phrase)
    click_on_first_element(driver)

    add_to_basket(driver)
    logging.info('test_add_to_basket() - end')
    if not bucket_count_is_more_than_zero(driver):
        logging.error('test_add_to_basket() - failed assertion')
    else:
        logging.info('test_add_to_basket() - assertion passed')
    assert bucket_count_is_more_than_zero(driver)
    driver.quit()


# test_register_and_add_to_basket("kid")

test_add_to_basket("kid")
