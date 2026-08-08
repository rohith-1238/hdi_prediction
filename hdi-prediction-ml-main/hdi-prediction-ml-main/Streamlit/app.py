import streamlit as st
import pandas as pd
import pickle

# Page configuration
st.set_page_config(
    page_title="HDI Prediction System",
    page_icon="🌍",
    layout="centered"
)

# Load trained model
model_path = "Flask/HDI.pkl"

try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)

except FileNotFoundError:
    st.error("HDI.pkl file not found. Please check the Flask/HDI.pkl path.")
    st.stop()


# Title
st.title("🌍 Human Development Index Prediction")
st.write(
    "Enter the socioeconomic indicators to predict the Human Development Index."
)


# Input fields
life_expectancy = st.number_input(
    "Life Expectancy",
    min_value=0.0,
    max_value=100.0,
    value=72.5
)

schooling = st.number_input(
    "Mean Years of Schooling",
    min_value=0.0,
    max_value=30.0,
    value=10.2
)

gni = st.number_input(
    "GNI per capita",
    min_value=0.0,
    value=15000.0
)

internet = st.number_input(
    "Internet Users (%)",
    min_value=0.0,
    max_value=100.0,
    value=65.4
)


# Prediction
if st.button("Predict HDI"):

    data = pd.DataFrame(
        [[
            life_expectancy,
            schooling,
            gni,
            internet
        ]],
        columns=[
            "Life expectancy",
            "Mean years of schooling",
            "Gross national income (GNI) per capita",
            "Internet users"
        ]
    )

    prediction = model.predict(data)[0]
    prediction = round(float(prediction), 2)


    # HDI classification
    if 0.3 <= prediction < 0.4:
        level = "Low HDI"

    elif 0.4 <= prediction < 0.7:
        level = "Medium HDI"

    elif 0.7 <= prediction < 0.8:
        level = "High HDI"

    elif 0.8 <= prediction <= 0.94:
        level = "Very High HDI"

    else:
        level = "Outside HDI range"


    # Display result
    st.success(f"{level}: {prediction}")

    st.subheader("Input Values")

    result_df = pd.DataFrame({
        "Indicator": [
            "Life Expectancy",
            "Mean Years of Schooling",
            "GNI per capita",
            "Internet Users (%)"
        ],
        "Value": [
            life_expectancy,
            schooling,
            gni,
            internet
        ]
    })

    st.table(result_df)
