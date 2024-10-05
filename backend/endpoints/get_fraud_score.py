#from services.text_inference.run_inference import get_prediction_score
from models.run_inference import get_prediction_score
from services.extract_text_features import extract_fetures
from services.digital_reputation.compute_reputation import compute_reputation_score
import pandas as pd


from fastapi import APIRouter


router = APIRouter()

#todo:
# retrieve sentence from ipfs by iD??

@router.post("/backend/fraud_prediction")
def predict_fraud(sentence: str, wallet:str, farcaster_id: str):
    try:
        # retrieve text fetures
        # build sentence vector
        sentence_features = extract_fetures(sentence)
        #sentence_vector = [value for value in sentence_features.values()]
        sentence_df = pd.DataFrame.from_dict(sentence_features, orient='index').T

        # inference
        text_prediction_score = get_prediction_score(sentence_df)

        # talent_protocol_score
        reputation_score = 1-compute_reputation_score(wallet, farcaster_id)

        # final scoring
        text_weight = 0.4
        rep_weight = 0.6
        score = ((text_weight*text_prediction_score[0]) + (rep_weight*reputation_score))/2

        response = {"prediction": score, "status_code": 200}

        return response

    except Exception as e:
        return {"error": str(e), "status_code":400}


