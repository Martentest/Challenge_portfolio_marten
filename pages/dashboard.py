from pages.base_page import BasePage


class Dashboard(BasePage):
    menu_button_xpath = "//*[@id='__next']/div/header/div/button"
    main_page_return_xpath = "//body/div[2]/div[3]/div/ul[1]/div[1]"
    players_hyperlink_xpath = "//body/div[2]/div[3]/div/ul[1]/div[2]"
    lang_change_xpath = "//body/div[2]/div[3]/div/ul[2]/div[1]"
    sign_out_xpath = "//body/div[2]/div[3]/div/ul[2]/div[2]"
    team_contact_hyperlink_xpath = "//*[@id='__next']/div/main/div[3]/div/div/div[3]/a"
    logo_xpath = "//*[@title='Logo Scouts Panel']"
    last_created_player_xpath = "//*[@id='__next']/div/main/div[3]/div[3]/div/div/a[1]/button"
    last_updated_player_xpath = "//*[@id='__next']/div/main/div[3]/div[3]/div/div/a[2]/button"
    last_created_match_xpath = "//*[@id='__next']/div/main/div[3]/div[3]/div/div/a[3]/button"
    last_updated_match_xpath = "//*[@id='__next']/div/main/div[3]/div[3]/div/div/a[4]/button"
    last_updated_report_xpath = "//*[@id='__next']/div/main/div[3]/div[3]/div/div/a[5]/button"
    add_player_xpath = "//*[@id='__next']/div/main/div[3]/div[2]/div[1]/div[1]/a/button"
    pass
