#from services.text_inference.run_inference import get_prediction_score
from backend.models.run_inference import get_prediction_score
from backend.services.extract_text_features import extract_fetures
from backend.services.digital_reputation.compute_reputation import compute_reputation_score
import pandas as pd
import os
from fastapi import APIRouter

router = APIRouter()

abs_db_path = os.path.abspath("./backend/db/database.csv")
print(abs_db_path)

@router.post("/backend/fraud_prediction")
def predict_fraud(id):

    _df = pd.read_csv("/Users/emanuelefratocchi/Documents/Progetti/ethrome/ethrome2k24/backend/db/database.csv")
    campaign_data = _df.loc[_df['id']==int(id)]

    sentence = campaign_data['Description'].values[0]
    wallet = campaign_data['Wallet'].values[0]
    farcaster_id = campaign_data['fid'].values[0]

    try:
        # retrieve text features and build sentence vector
        sentence_features = extract_fetures(sentence)
        sentence_df = pd.DataFrame.from_dict(sentence_features, orient='index').T

        # inference
        text_prediction_score = get_prediction_score(sentence_df)

        # talent_protocol_score
        reputation_score = 1-compute_reputation_score(wallet, farcaster_id)

        # final scoring
        text_weight = 0.4
        rep_weight = 0.6
        score = ((text_weight*text_prediction_score[0]) + (rep_weight*reputation_score))/2

        response = {"prediction": float(score), "status_code": 200}

        return response

    except Exception as e:
        return {"error": str(e), "status_code":400}


