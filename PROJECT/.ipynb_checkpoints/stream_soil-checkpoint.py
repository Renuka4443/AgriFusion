import streamlit as st
import pandas as pd
import joblib

# Load saved model
model = joblib.load('soil_fertility_model.pkl')

# Title
st.title("🌾 Soil Fertility Predictor")

# Instructions
st.write("Enter the values for each soil feature below:")

# You must enter features in the same order as training
feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']  # Replace with your exact column names

# Create input fields dynamically
user_inputs = []
for feature in feature_names:
    val = st.number_input(f"{feature}", format="%.2f")
    user_inputs.append(val)

# Predict
if st.button("Predict Fertility"):
    input_df = pd.DataFrame([user_inputs], columns=feature_names)
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Fertility Class: **{prediction}**")
