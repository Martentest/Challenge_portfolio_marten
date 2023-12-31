import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    expected_title = "Scouts panel - sign in"
    login_url = 'https://dareit.futbolkolektyw.pl/en'

    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id ='password']"
    sign_in_button_xpath = "//*[@type='submit']"
#    remind_password_hyperlink_xpath = "//*[text()='Remind password']"
#    change_language_select_xpath = "//*[@aria-haspopup='listbox']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        print(self.login_url + self.expected_title)
        assert self.get_page_title(self.login_url) == self.expected_title