from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_login(email, password, expected_text, driver):
    try:
        url = "https://www.zalando.pl/"
        driver.maximize_window()
        driver.get(url)
        button_login = driver.find_element_by_class_name("z-navicat-header_navToolItem")
        button_login.click()
        input_email = driver.find_element_by_id("login.email")
        input_email.send_keys(email)
        input_password = driver.find_element_by_id("login.password")
        input_password.send_keys(password)
        button_login_confirm = driver.find_element_by_xpath("//button[@data-testid='login_button']")
        button_login_confirm.click()
    except Exception as e:
        print(f"Nie znaleziono pól do logowania: {e}")
        driver.quit()
        return False

    try:
        expected_text_found = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_text}')]")))
    except Exception as e:
        print(f"Nie znaleziono: {expected_text}, {e}")
        driver.quit()
        return False
    driver.quit()
    return True


def test_login_succesful(driver):
    email = "testowanie@123.pl"
    password = "qwerty123"
    expected_text = "Witaj Test"
    return test_login(email, password, expected_text, driver)


def test_login_wrong_email(driver):
    email = "@wrongemail.{pl}"
    password = "qwerty123"
    expected_text = "Podaj pełny adres e-mail"
    return test_login(email, password, expected_text, driver)


def test_login_no_email(driver):
    email = ""
    password = "qwerty123"
    expected_text = "Pole obowiązkowe"
    return test_login(email, password, expected_text, driver)


def test_login_no_password(driver):
    email = "testowanie@123.pl"
    password = ""
    expected_text = "Pole obowiązkowe"
    return test_login(email, password, expected_text, driver)
