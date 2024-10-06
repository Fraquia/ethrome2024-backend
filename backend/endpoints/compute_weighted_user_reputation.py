from services.text_inference.run_inference import get_prediction_score
from services.extract_text_features import extract_fetures
from services.digital_reputation.compute_reputation import compute_reputation_score
import pandas as pd


from fastapi import APIRouter


router = APIRouter()


@router.post("/backend/compute_weighted_user_reputation")
def compute_user_reputation(sentence: str, wallet: str, farcaster_id: str, text_weight: float, identity_weight: float):

    try:
        # retrieve text fetures build sentence vector
        sentence_features = extract_fetures(sentence)
        sentence_df = pd.DataFrame.from_dict(sentence_features, orient='index').T

        # inference
        text_prediction_score = get_prediction_score(sentence_df)[0]

        # talent_protocol_score
        identity_score = compute_reputation_score(wallet, farcaster_id)

        # final scoring
        score = ((text_weight*text_prediction_score) + (identity_weight*identity_score))/2

        response = {"prediction": float(score), "status_code": 200}

        return response

    except Exception as e:
        return {"error": str(e), "status_code":400}