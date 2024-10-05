import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("MBD_APY_KEY")


def get_sentiment_analysis(sentence):
    http_request_string = "https://api.mbd.xyz/v1/farcaster/casts/labels/for-text"
    request_data = json.dumps({
        "text_inputs": [
            sentence],
        "label_category": "sentiment"
    })

    print(request_data)

    response = requests.post(
        http_request_string,
        headers={
            "HTTP-Referer": "https://docs.mbd.xyz/",
            "X-Title":"mbd_docs",
            "accept":"application/json",
            "content-type": "application/json",
            "x-api-key": api_key,
        },
        data=request_data
    )

    data = response.json()
    response_body = data['body']
    return response_body
