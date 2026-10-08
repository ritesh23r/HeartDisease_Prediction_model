from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained objects
model = joblib.load("model/heart_disease_model.pkl")
scaler = joblib.load("model/scaler.pkl")
columns = joblib.load("model/columns.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from form
    age = float(request.form["age"])
    resting_bp = float(request.form["resting_bp"])
    cholesterol = float(request.form["cholesterol"])
    fasting_bs = int(request.form["fasting_bs"])
    max_hr = float(request.form["max_hr"])
    oldpeak = float(request.form["oldpeak"])

    sex = request.form["sex"]
    chest_pain = request.form["chest_pain"]
    resting_ecg = request.form["resting_ecg"]
    exercise_angina = request.form["exercise_angina"]
    st_slope = request.form["st_slope"]

    # Create base numerical features
    # Scaler was trained on these 5 continuous features.
    numerical = np.array([[
        age,
        resting_bp,
        cholesterol,
        max_hr,
        oldpeak
    ]])

    scaled = scaler.transform(numerical)[0]

    # Create complete feature dictionary
    data = {
        "Age": scaled[0],
        "RestingBP": scaled[1],
        "Cholesterol": scaled[2],
        "FastingBS": fasting_bs,
        "MaxHR": scaled[3],
        "Oldpeak": scaled[4],

        "is_male": 1 if sex == "male" else 0,

        "ChestPainType_ATA": 1 if chest_pain == "ATA" else 0,
        "ChestPainType_NAP": 1 if chest_pain == "NAP" else 0,
        "ChestPainType_TA": 1 if chest_pain == "TA" else 0,

        "RestingECG_Normal": 1 if resting_ecg == "Normal" else 0,
        "RestingECG_ST": 1 if resting_ecg == "ST" else 0,

        "ExerciseAngina_Y": 1 if exercise_angina == "Yes" else 0,

        "ST_Slope_Flat": 1 if st_slope == "Flat" else 0,
        "ST_Slope_Up": 1 if st_slope == "Up" else 0,
    }

    # Arrange features in EXACT model column order
    input_df = pd.DataFrame([data])[columns]

    # Prediction
    prediction = int(model.predict(input_df)[0])

    # Probability
    probabilities = model.predict_proba(input_df)[0]

    probability = float(probabilities[prediction]) * 100

    if prediction == 1:
        result = "Higher Risk Indicated"
        result_type = "high"
    else:
        result = "Lower Risk Indicated"
        result_type = "low"

    return render_template(
        "index.html",
        result=result,
        result_type=result_type,
        probability=round(probability, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)