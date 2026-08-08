import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), "HDI.pkl")
model = pickle.load(open(model_path, "rb"))


# Home page
@app.route("/")
def home():
    return render_template("home.html")


# Prediction page
@app.route("/Prediction", methods=["GET", "POST"])
def prediction():
    return render_template("indexnew.html")


# Home route
@app.route("/Home", methods=["GET", "POST"])
def my_home():
    return render_template("home.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    # Get input values from HTML form
    input_features = [float(x) for x in request.form.values()]

    features_name = [
        "Life expectancy",
        "Mean years of schooling",
        "Gross national income (GNI) per capita",
        "Internet users"
    ]

    # Create DataFrame
    df = pd.DataFrame(
        [input_features],
        columns=features_name
    )

    # Predict HDI
    output = model.predict(df)
    y_pred = round(float(output[0]), 2)

    # Classify HDI
    if 0.3 <= y_pred < 0.4:
        result = f"Low HDI - {y_pred}"

    elif 0.4 <= y_pred < 0.7:
        result = f"Medium HDI - {y_pred}"

    elif 0.7 <= y_pred < 0.8:
        result = f"High HDI - {y_pred}"

    elif 0.8 <= y_pred <= 0.94:
        result = f"Very High HDI - {y_pred}"

    else:
        result = "The given values do not match the HDI range."

    return render_template(
        "resultnew.html",
        prediction_text=result
    )


# Dashboard
@app.route("/Dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
