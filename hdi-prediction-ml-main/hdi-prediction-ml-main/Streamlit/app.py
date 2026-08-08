
import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="HDI Prediction System",
    page_icon="🌍",
    layout="centered"
)

# =========================================================
# FIND PROJECT ROOT
# =========================================================

# Current file:
# .../hdi-prediction-ml-main/Streamlit/app.py

BASE_DIR = Path(__file__).resolve().parent

# Model location:
# .../hdi-prediction-ml-main/
#     ML-0027-Human-Development-Index/
#         Flask/
#             HDI.pkl

MODEL_PATH = (
    BASE_DIR.parent
    / "ML-0027-Human-Development-Index"
    / "Flask"
    / "HDI.pkl"
)

# =========================================================
# LOAD MACHINE LEARNING MODEL
# =========================================================

if not MODEL_PATH.exists():

    st.error("❌ HDI.pkl was not found.")

    st.write("Expected model location:")
    st.code(str(MODEL_PATH))

    st.write("Current Streamlit directory:")
    st.code(str(BASE_DIR))

    st.stop()


try:

    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

except ModuleNotFoundError as e:

    st.error("❌ Required Python package is missing.")
    st.code(str(e))

    st.info(
        "Make sure scikit-learn is present in requirements.txt."
    )

    st.stop()

except Exception as e:

    st.error("❌ Error loading HDI.pkl")
    st.code(str(e))

    st.stop()


# =========================================================
# TITLE
# =========================================================

st.title("🌍 Human Development Index Prediction")

st.write(
    "Enter the socioeconomic indicators below "
    "to predict the Human Development Index."
)

# =========================================================
# INPUT FIELDS
# =========================================================

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

# =========================================================
# PREDICTION
# =========================================================

if st.button("Predict HDI", type="primary"):

    # -----------------------------------------------------
    # Prepare input data
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # Make prediction
    # -----------------------------------------------------

    try:

        prediction = model.predict(input_data)[0]

        prediction = round(float(prediction), 2)

    except Exception as e:

        st.error("❌ Prediction failed.")
        st.code(str(e))

        st.stop()

    # =====================================================
    # HDI CLASSIFICATION
    # =====================================================

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

    # =====================================================
    # DISPLAY RESULT
    # =====================================================

    st.success(
        f"🌍 {hdi_level} — Predicted HDI: {prediction}"
    )

    # =====================================================
    # DISPLAY INPUTS
    # =====================================================

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

