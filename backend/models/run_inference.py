import xgboost as xgb
import os

abs_model_path = os.path.abspath("backend/models/text_model.json")


def get_prediction_score(sentence_vector):

    model_loaded = xgb.Booster()
    model_loaded.load_model(abs_model_path)

    #sentence_array = np.array([sentence_vector])  # replace with your feature vector
    dvector = xgb.DMatrix(sentence_vector)

    # Perform inference
    prediction = model_loaded.predict(dvector)

    return prediction


print(os.path.abspath("backend/models/text_model.json"))