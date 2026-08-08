import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

st.set_page_config(
    page_title="HDI Prediction System",
    page_icon="🌍",
    layout="centered"
)

# --------------------------------------------------
# Find project root
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Model location
MODEL_PATH = PROJECT_ROOT / "Flask" / "HDI.pkl"

# --------------------------------------------------
# Check files
# --------------------------------------------------

st.write("Project root:", PROJECT_ROOT)
st.write("Model path:", MODEL_PATH)

if not MODEL_PATH.exists():
    st.error("HDI.pkl was not found.")

    st.write("Files available in project:")

    for path in PROJECT_ROOT.rglob("*"):
        if path.is_file():
            st.write(str(path))

    st.stop()

# --------------------------------------------------
# Load model
# --------------------------------------------------

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


# --------------------------------------------------
# Application
# --------------------------------------------------

st.title("🌍 Human Development Index Prediction")

st.write(
    "Enter the socioeconomic indicators to predict the Human Development Index."
)

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

    st.success(f"{level}: {prediction}")
