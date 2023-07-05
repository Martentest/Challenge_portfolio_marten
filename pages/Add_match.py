from pages.base_page import BasePage


class Add_match(BasePage):
    my_team_input_xpath = "//*[@name = 'myTeam']"
    enemy_team_input_xpath = "//*[@name = 'enemyTeam']"
    my_team_score_input_xpath = "//*[@name = 'myTeamScore']"
    enemy_team_score_input_xpath = "//*[@name = 'enemyTeamScore']"
    date_input_xpath = "//*[@name = 'date']"
    matchAtHome_radio_xpath = "//*[@name = 'matchAtHome']"
    matchOutHome_radio_xpath = "//*[@name = 'matchOutHome']"
    tshirt_input_xpath = "//*[@name = 'tshirt']"
    league_input_xpath = "//*[@name = 'league']"
    time_played_input_xpath = "//*[@name = 'timePlayed']"
    number_input_xpath = "//*[@name = 'number']"
    web_match_input_xpath = "//*[@name = 'webMatch']"
    general_input_xpath = "//*[@name = 'general']"
    rating_input_xpath = "//*[@name = 'rating']"
    submit_button_xpath = "//*[@type = 'submit']"
    clear_button_xpath = "//body/div/div/main/div[2]/form/div[3]/button[2]"

pass