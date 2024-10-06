from services.text_inference.run_inference import get_prediction_score
from services.extract_text_features import extract_fetures
import pandas as pd


from fastapi import APIRouter


router = APIRouter()


@router.post("/backend/text_reputation")
def text_reputation(sentence: str):

    try:
        # retrieve text fetures build sentence vector
        sentence_features = extract_fetures(sentence)
        sentence_df = pd.DataFrame.from_dict(sentence_features, orient='index').T

        # inference
        score = get_prediction_score(sentence_df)
        response = {"prediction": float(score[0]), "status_code": 200}

        return response

    except Exception as e:
        return {"error": str(e), "status_code":400}
