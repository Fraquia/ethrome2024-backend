import numpy as np
import xgboost as xgb

model_loaded = xgb.Booster()
model_loaded.load_model("../backend/models/text_model.json")

def get_prediction_score(sentence_vector):

    #sentence_array = np.array([sentence_vector])  # replace with your feature vector
    dvector = xgb.DMatrix(sentence_vector)

    # Perform inference
    prediction = model_loaded.predict(dvector)

    return prediction