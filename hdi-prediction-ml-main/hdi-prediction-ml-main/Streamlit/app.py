import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="HDI Prediction System",
    page_icon="🌍",
    layout="centered"
)

# --------------------------------------------------
# Locate project root
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Correct location of HDI.pkl
MODEL_PATH = (
    PROJECT_ROOT
    / "ML-0027-Human-Development-Index"
    / "Flask"
    / "HDI.pkl"
)

# --------------------------------------------------
# Load trained model
# --------------------------------------------------

try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

except FileNotFoundError:
    st.error(f"HDI.pkl not found at: {MODEL_PATH}")
    st.stop()


# --------------------------------------------------
# Application
# --------------------------------------------------

st.title("🌍 Human Development Index Prediction")

st.write(
    "Enter the socioeconomic indicators to predict the Human Development Index."
)

# Input 1
life_expectancy = st.number_input(
    "Life Expectancy",
    min_value=0.0,
    max_value=100.0,
    value=72.5
)

# Input 2
schooling = st.number_input(
    "Mean Years of Schooling",
    min_value=0.0,
    max_value=30.0,
    value=10.2
)

# Input 3
gni = st.number_input(
    "GNI per capita",
    min_value=0.0,
    value=15000.0
)

# Input 4
internet = st.number_input(
    "Internet Users (%)",
    min_value=0.0,
    max_value=100.0,
    value=65.4
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict HDI"):

    # Create DataFrame
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

    # Predict
    prediction = model.predict(data)[0]
    prediction = round(float(prediction), 2)

    # Classify HDI
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

    # Display inputs
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
