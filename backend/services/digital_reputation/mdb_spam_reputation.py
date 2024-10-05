import requests
from dotenv import load_dotenv
import os
import json


load_dotenv()
api_key = os.getenv("MBD_APY_KEY")


def get_spam_score(_id: str):
    try:
        url = "https://api.mbd.xyz/v1/farcaster/users/labels/for-users"

        payload = json.dumps({
            "users_list": [_id],
            "label_category": "llm_generated"
        })

        headers = {
            "HTTP-Referer": "https://docs.mbd.xyz/",
            "X-Title": "mbd_docs",
            "accept": "application/json",
            "content-type": "application/json",
            "x-api-key": api_key
        }

        response = requests.post(url,
                                 headers=headers,
                                 data=payload)

        return response['body'][0]['score']

    except Exception as e:
        print(e)
        return 0
