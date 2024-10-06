from services.text_inference.run_inference import get_prediction_score
from services.extract_text_features import extract_fetures
from services.digital_reputation.talent_protocol_passport import extract_talent_protocol_score
import pandas as pd


from fastapi import APIRouter


router = APIRouter()

#todo:
# retrieve sentence from ipfs by iD??

@router.post("/backend/fraud_prediction")
def predict_fraud(id):

    _db = pd.read_csv("/backend/db/database.csv")
    campaign_data = _db.loc[_db['id']==id]
    sentence = campaign_data['Description'].values()[0]
    wallet = campaign_data['Wallet'].values()[0]


    try:
        # retrieve text fetures
        # build sentence vector
        sentence_features = extract_fetures(sentence)
        #sentence_vector = [value for value in sentence_features.values()]
        sentence_df = pd.DataFrame.from_dict(sentence_features, orient='index').T

        # inference
        text_prediction_score = get_prediction_score(sentence_df)

        # talent_protocol_score
        talent_protocol_score = 1-extract_talent_protocol_score(wallet)

        # final scoring
        text_weight = 1
        tp_weight = 1
        score = ((text_weight*text_prediction_score[0]) + (tp_weight*talent_protocol_score))/2


        response = {"prediction": score, "status_code": 200}


        return response

    except Exception as e:
        return {"error": str(e), "status_code":400}
