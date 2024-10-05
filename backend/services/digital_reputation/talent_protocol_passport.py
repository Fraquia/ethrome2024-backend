import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("TALENT_PROTOCOL_API_KEY")

wallet_id = "1106547"
wallet_string = "0x49e4f4be7d3f8db51044269ff02e3ff6169c2c45"


def get_talent_protocol_passport(wallet_string):
    http_request_string = f"https://api.talentprotocol.com/api/v2/passports/{wallet_string}"

    response = requests.get(
        http_request_string,
        headers={
            "X-API-KEY": api_key
        },
    )
    data = response.json()

    return data


def extract_talent_protocol_score(wallet_string):
    data = get_talent_protocol_passport(wallet_string)
    activity_score = data['passport']['activity_score']
    identity_score = data['passport']['identity_score']
    social_score = len(data['passport']['passport_socials'])
    wallet_score = len(data['passport']['verified_wallets'])

    _sum_elements = [activity_score/50, identity_score/40, social_score/8, wallet_score/5]

    _score = sum(_sum_elements)/len(_sum_elements)

    return _score


# _test = extract_talent_protocol_score("0x1358155a15930f89eBc787a34Eb4ccfd9720bC62")
# print('Done')