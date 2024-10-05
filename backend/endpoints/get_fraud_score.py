from services.text_inference.run_inference import get_prediction_score
from services.extract_text_features import extract_fetures
import pandas as pd


from fastapi import APIRouter


router = APIRouter()

#todo:
# retrieve sentence from ipfs by iD??

@router.post("/backend/fraud_prediction")
def predict_fraud(sentence: str):
    try:
        #retrieve
        # build sentence vector
        sentence_features = extract_fetures(sentence)
        #sentence_vector = [value for value in sentence_features.values()]
        sentence_df = pd.DataFrame.from_dict(sentence_features, orient='index').T

        # inference
        prediction = get_prediction_score(sentence_df)
        response = {"prediction": prediction, "status_code": 200}
        return response

    except Exception as e:
        return {"error": str(e), "status_code":400}
