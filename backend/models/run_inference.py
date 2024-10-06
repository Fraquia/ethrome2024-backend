import xgboost as xgb
import os

abs_model_path = os.path.abspath("./backend/db/database.csv")


def get_prediction_score(sentence_vector):

    model_loaded = xgb.Booster()
    model_loaded.load_model("/Users/emanuelefratocchi/Documents/Progetti/ethrome/ethrome2k24/backend/models/text_model.json")

    #sentence_array = np.array([sentence_vector])  # replace with your feature vector
    dvector = xgb.DMatrix(sentence_vector)

    # Perform inference
    prediction = model_loaded.predict(dvector)

    return prediction
