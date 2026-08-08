# Importing the necessary dependencies

import numpy as np
import pandas as pd
import streamlit as st
from flask import Flask, render_template, request
import pickle

# Flask - framework used to run/serve our application
# Streamlit - used for Streamlit-based UI/components
# request - used to access data submitted by the user

app = Flask(__name__)

# Loading the trained ML model
model = pickle.load(open('HDI.pkl', 'rb'))


# Home page
@app.route('/')
def home():
    return render_template('home.html')


# Prediction page
@app.route('/Prediction', methods=['POST', 'GET'])
def prediction():
    return render_template('indexnew.html')


# Home route
@app.route('/Home', methods=['POST', 'GET'])
def my_home():
    return render_template('home.html')


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():

    # Reading the inputs given by the user
    input_features = [float(x) for x in request.form.values()]

    # Converting inputs into NumPy array
    features_value = [np.array(input_features)]

    # Feature names
    features_name = [
        'Life expectancy',
        'Mean years of schooling',
        'Gross national income (GNI) per capita',
        'Internet users'
    ]

    # Creating DataFrame
    df = pd.DataFrame(features_value, columns=features_name)

    # Making prediction
    output = model.predict(df)

    # Round prediction
    y_pred = round(output[0], 2)

    print("Prediction:", y_pred)

    # Classify HDI level
    if 0.3 <= y_pred < 0.4:
        result = 'Low HDI ' + str(y_pred)

    elif 0.4 <= y_pred < 0.7:
        result = 'Medium HDI ' + str(y_pred)

    elif 0.7 <= y_pred < 0.8:
        result = 'High HDI ' + str(y_pred)

    elif 0.8 <= y_pred <= 0.94:
        result = 'Very High HDI ' + str(y_pred)

    else:
        result = 'The given values do not match the HDI range'

    return render_template(
        'resultnew.html',
        prediction_text=result
    )


# Dashboard page
@app.route('/Dashboard')
def dashboard():
    return render_template('dashboard.html')


# Run Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
