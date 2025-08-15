import os
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

MODEL_PATH = 'regressor_model.pkl'

regressor_model = None


def load_or_train_model() -> LinearRegression:
    global regressor_model

    if regressor_model is not None:
        return regressor_model

    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            regressor_model = pickle.load(f)
        return regressor_model

    # Fallback: train quickly if model file is missing
    df = pd.read_csv('Diabetes_cleaned.csv')
    X = df[[
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "Pregnancies",
        "Age",
        "DiabetesPedigreeFunction",
    ]]
    y = df["Outcome"]

    model = LinearRegression()
    model.fit(X, y)

    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)

    regressor_model = model
    return regressor_model


# Initialize model once on import to keep app.py unchanged
regressor_model = load_or_train_model()