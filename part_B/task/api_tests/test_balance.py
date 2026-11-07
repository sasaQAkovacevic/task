from clients.clients import *

def test_balance_calculation():
    start_balance = get_balance()
    place_bet()
    finish_balance = get_balance()
    assert finish_balance + STAKE == start_balance
    print("After placing a bet - balance is correctly recalculated")
