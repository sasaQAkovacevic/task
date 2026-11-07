import json
import requests

BASE_URL = "https://qae-assignment-tau.vercel.app"
USER_ID = "candidate-UTA0y1xZ7sCk"
STAKE = 10.00
SELECTION = "HOME"
HEADERS = {
    "accept": "*/*",
    "x-user-id": USER_ID,
}

def get_balance() -> float:
    response = requests.get(f"{BASE_URL}/api/balance", headers=HEADERS, timeout=30)
    response.raise_for_status()
    response_body = json.loads(response.text)
    return float(response_body["balance"])

def get_matches():
    response = requests.get(f"{BASE_URL}/api/matches", headers=HEADERS, timeout=30)
    response.raise_for_status()
    return json.loads(response.text)

def get_first_match_id():
    return get_matches()[0]["id"]

def make_place_bet_body():
    return {
        "stake": STAKE,
        "matchId": get_first_match_id(),
        "selection": SELECTION,
    }

def place_bet():
    response = requests.post(
        f"{BASE_URL}/api/place-bet",
        json=make_place_bet_body(),
        headers=HEADERS,
        timeout=30,
    )
    response_body = json.loads(response.text)
    if not response.ok:
        raise AssertionError(
            f"POST /api/place-bet failed ({response.status_code}): {response_body}"
        )
    return response_body
