import unittest

from selenium import webdriver

import test_login_utils


def driver_chrome():
    return webdriver.Chrome(executable_path="../../lib/chromedriver.exe")


def driver_firefox():
    return webdriver.Firefox(executable_path="../../lib/geckodriver.exe")


def driver_edge():
    return webdriver.Edge(executable_path="../../lib/msedgedriver.exe")


class TestPlemionaLogin(unittest.TestCase):

    def test_login_succesful_chrome(self):
        result = test_login_utils.test_login_succesful(driver_chrome())
        self.assertTrue(result)

    def test_wrong_email_chrome(self):
        result = test_login_utils.test_login_wrong_username(driver_chrome())
        self.assertTrue(result)

    def test_no_email_chrome(self):
        result = test_login_utils.test_login_no_username(driver_chrome())
        self.assertTrue(result)

    def test_no_password_chrome(self):
        result = test_login_utils.test_login_no_password(driver_chrome())
        self.assertTrue(result)

    def test_login_succesful_firefox(self):
        result = test_login_utils.test_login_succesful(driver_firefox())
        self.assertTrue(result)

    def test_wrong_email_firefox(self):
        result = test_login_utils.test_login_wrong_username(driver_firefox())
        self.assertTrue(result)

    def test_no_email_firefox(self):
        result = test_login_utils.test_login_no_username(driver_firefox())
        self.assertTrue(result)

    def test_no_password_firefox(self):
        result = test_login_utils.test_login_no_password(driver_firefox())
        self.assertTrue(result)

    def test_login_succesful_edge(self):
        result = test_login_utils.test_login_succesful(driver_edge())
        self.assertTrue(result)

    def test_wrong_email_edge(self):
        result = test_login_utils.test_login_wrong_username(driver_edge())
        self.assertTrue(result)

    def test_no_email_edge(self):
        result = test_login_utils.test_login_no_username(driver_edge())
        self.assertTrue(result)

    def test_no_password_edge(self):
        result = test_login_utils.test_login_no_password(driver_edge())
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
