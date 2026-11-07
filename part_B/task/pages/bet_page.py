from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BetPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.url = "https://qae-assignment-tau.vercel.app/?user-id=candidate-UTA0y1xZ7sCk"

        self.BET_SLIP = (By.ID, "bet-slip")
        self.FIRST_ODD_BUTTON = (By.CSS_SELECTOR, "#match-list .matchCard .oddsButton")
        self.STAKE_INPUT = (By.ID, "bet-slip-stake-input")
        self.PLACE_BET_BUTTON = (By.ID, "bet-slip-place-bet")
        self.SUCCESS_MODAL = (By.ID, "modal-success")
        self.CLOSE_MODAL_BUTTON = (By.ID, "modal-success-close")

    def open(self):
        self.driver.get(self.url)

    def get_bet_slip_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.BET_SLIP))
        return element.text

    def select_first_odd(self):
        element = self.wait.until(EC.element_to_be_clickable(self.FIRST_ODD_BUTTON))
        element.click()

    def wait_for_match_in_bet_slip(self, match_name):
        self.wait.until(lambda d: match_name in d.find_element(*self.BET_SLIP).text)

    def enter_stake(self, stake_value):
        element = self.driver.find_element(*self.STAKE_INPUT)
        element.click()
        element.send_keys(str(stake_value))

    def click_place_bet(self):
        self.wait.until(EC.element_to_be_clickable(self.PLACE_BET_BUTTON)).click()

    def get_success_modal_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MODAL))
        return element.text

    def close_success_modal(self):
        self.driver.find_element(*self.CLOSE_MODAL_BUTTON).click()

    def wait_for_modal_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(self.SUCCESS_MODAL))
