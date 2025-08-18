
import numpy as np
from flask import Flask, request, render_template

from model import load_or_train_model

regressor_model = load_or_train_model()

app = Flask(__name__)

@app.route('/',methods =['GET','POST'])

def sales_view():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        g= float(request.form["Glucose"])
        b = float(request.form["BloodPressure"])
        s= float(request.form["SkinThickness"])
        i = float(request.form["Insulin"])
        bmi = float(request.form["BMI"])
        p = float(request.form["Pregnancies"])
        a = float(request.form["Age"])
        d = float(request.form["DiabetesPedigreeFunction"])

        input_data = np.array([[g, b, s, i, bmi, p, a, d]])
        op_array = regressor_model.predict(input_data)
        y_pred = op_array

        pred_value = int(y_pred[0])
        if pred_value == 1:
            result = "The patient will  suffer from diabetes."
        else:
            result = "The patient will not suffer from diabetes."

        return render_template("output.html", predicted_diabetes = result )

if __name__ == '__main__':
    app.run(debug=True)
