import time

import os
import unittest
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.base_page import BasePage

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service



class TestDashboardTitle(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_dashboard_title(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(4)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

