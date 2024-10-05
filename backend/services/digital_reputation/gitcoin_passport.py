import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GITCOIN_PASSPORT_API_KEY")
scorer_id = os.getenv("GITCOIN_SCORER_ID")

wallet_string = "0x49e4f4be7d3f8db51044269ff02e3ff6169c2c45"
biancotto_id = "1696"

def get_gitcoin_score(wallet_string):
    # retrieve score of a single wallet/id

    http_request_string = f"https://api.scorer.gitcoin.co/registry/score/{scorer_id}/{wallet_string}"

    response = requests.get(
        http_request_string,
        headers={
            "X-API-KEY": api_key
        },
    )

    data = response.json()

    return data


_test = get_talent_passport_score(biancotto_id)

