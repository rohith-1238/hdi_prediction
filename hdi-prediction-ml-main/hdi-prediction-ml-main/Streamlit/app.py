import streamlit as st
import pandas as pd
import pickle
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="HDI Prediction System",
    page_icon="🌍",
    layout="centered"
)


# ============================================================
# MODEL
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "HDI.pkl"


if not MODEL_PATH.exists():
    st.error("HDI.pkl not found.")
    st.write("Expected location:")
    st.code(str(MODEL_PATH))
    st.stop()


try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

except ModuleNotFoundError as e:
    st.error("Required ML dependency is missing.")
    st.code(str(e))
    st.stop()

except Exception as e:
    st.error("HDI model could not be loaded.")
    st.code(str(e))
    st.stop()


# ============================================================
# TITLE
# ============================================================

st.title("🌍 Human Development Index Prediction")

st.write(
    "Enter the socioeconomic indicators to predict "
    "the Human Development Index."
)


# ============================================================
# INPUTS
# ============================================================

life_expectancy = st.number_input(
    "Life Expectancy",
    min_value=0.0,
    max_value=100.0,
    value=72.5,
    step=0.1
)

schooling = st.number_input(
    "Mean Years of Schooling",
    min_value=0.0,
    max_value=30.0,
    value=10.2,
    step=0.1
)

gni = st.number_input(
    "GNI per capita",
    min_value=0.0,
    value=15000.0,
    step=100.0
)

internet = st.number_input(
    "Internet Users (%)",
    min_value=0.0,
    max_value=100.0,
    value=65.4,
    step=0.1
)


# ============================================================
# PREDICTION
# ============================================================

if st.button("Predict HDI", type="primary"):

    input_data = pd.DataFrame(
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

    try:

        prediction = model.predict(input_data)[0]
        prediction = round(float(prediction), 2)

    except Exception as e:

        st.error("Prediction failed.")
        st.code(str(e))
        st.stop()


    # ========================================================
    # HDI LEVEL
    # ========================================================

    if prediction < 0.4:
        hdi_level = "Low HDI"

    elif prediction < 0.7:
        hdi_level = "Medium HDI"

    elif prediction < 0.8:
        hdi_level = "High HDI"

    elif prediction <= 0.94:
        hdi_level = "Very High HDI"

    else:
        hdi_level = "Outside HDI Range"


    # ========================================================
    # RESULT
    # ========================================================

    st.success(
        f"{hdi_level} — Predicted HDI: {prediction}"
    )


    # ========================================================
    # INPUT SUMMARY
    # ========================================================

    st.subheader("Prediction Inputs")

    result = pd.DataFrame({
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

    st.dataframe(
        result,
        use_container_width=True,
        hide_index=True
    )
