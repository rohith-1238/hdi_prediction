import streamlit as st
import pandas as pd
from pathlib import Path
import pickle

st.set_page_config(
    page_title="HDI Prediction System",
    page_icon="🌍"
)

# Find project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Find model
MODEL_PATH = BASE_DIR / "Flask" / "HDI.pkl"

# Load model
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

st.title("🌍 Human Development Index Prediction")
