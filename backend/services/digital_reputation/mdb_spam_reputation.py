import requests


def get_spam_score(_id: str):
    try:
        url = "https://api.mbd.xyz/v1/farcaster/users/labels/for-users"

        payload = {
            "users_list": [_id],
            "label_category": "spam"
        }
        headers = {
            "accept": "application/json",
            "HTTP-Referer": "https://docs.mbd.xyz/",
            "X-Title": "mbd_docs",
            "content-type": "application/json",
            "x-api-key": "mbd-bd3df8ecf52f86f83b90bd36a5ea8bc3c5e2aacb8b83a518fa3a13eeac773e09"
        }

        response = requests.post(url, json=payload, headers=headers)

        return float(response.text)

    except:
        return 0
