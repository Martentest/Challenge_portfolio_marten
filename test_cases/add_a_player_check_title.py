import time

import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.add_a_player_page import AddAPlayerPage


class TestAddPlayerTitle(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player_title(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_add_a_player_button()
        time.sleep(5)
        add_player_page = AddAPlayerPage(self.driver)
        add_player_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()

