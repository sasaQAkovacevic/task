from pages.bet_page import BetPage

STAKE = 10.00

def test_place_bet_on_first_odd(driver):
    bet_page = BetPage(driver)

    bet_page.open()
    assert "Select odds to place a bet" in bet_page.get_bet_slip_text()

    bet_page.select_first_odd()
    bet_page.wait_for_match_in_bet_slip("Manchester Utd vs Chelsea")

    bet_page.enter_stake(STAKE)
    bet_page.click_place_bet()

    assert "Bet Placed Successfully!" in bet_page.get_success_modal_text()
    print("Bet is successfully placed")

    bet_page.close_success_modal()
    bet_page.wait_for_modal_to_disappear()
