import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('Diabetes_cleaned.csv')

X = df[["Glucose","BloodPressure","SkinThickness","Insulin","BMI","Pregnancies","Age","DiabetesPedigreeFunction"]]
y = df["Outcome"]

regressor_model = LinearRegression()
regressor_model.fit(X, y)

pickle.dump(regressor_model, open('regressor_model.pkl','wb'))