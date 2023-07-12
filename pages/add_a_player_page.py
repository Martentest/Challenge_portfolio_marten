import time

from pages.base_page import BasePage


class AddAPlayerPage(BasePage):
    expected_title = "Add player"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

#    login_field_xpath = "//*[@id='login']"
#    password_field_xpath = "//*[@id ='password']"
#    remind_password_hyperlink_xpath = "//*[text()='Remind password']"
#    change_language_select_xpath = "//*[@aria-haspopup='listbox']"

    def title_of_page(self):
        print(self.login_url + self.expected_title)
        assert self.get_page_title(self.login_url) == self.expected_title
