import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the trained model
with open("linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

# Function to preprocess user input
def preprocess_input(age, sex, bmi, children, smoker, region):
    # Encode categorical values
    sex = 1 if sex == "Male" else 0
    smoker = 1 if smoker == "Yes" else 0
    
    # One-hot encoding for region
    region_dict = {"northeast": [1, 0, 0], "northwest": [0, 1, 0], "southeast": [0, 0, 1], "southwest": [0, 0, 0]}
    region_encoded = region_dict.get(region.lower(), [0, 0, 0])

    # Standardization (use mean and std from training data)
    age_scaled = (age - 39) / 14  # Example: mean=39, std=14 (adjust if different)
    bmi_scaled = (bmi - 30) / 6    # Example: mean=30, std=6 (adjust if different)
    children_scaled = (children - 1) / 1.2  # Example: mean=1, std=1.2 (adjust if different)

    # Final input array
    input_data = np.array([age_scaled, sex, bmi_scaled, children_scaled, smoker] + region_encoded).reshape(1, -1)
    
    return input_data

# Streamlit UI
st.title("Medical Insurance Charges Prediction")
st.write("Enter details below to predict insurance charges.")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
sex = st.radio("Sex", ("Male", "Female"))
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=5, value=0, step=1)
smoker = st.radio("Smoker", ("Yes", "No"))
region = st.selectbox("Region", ("northeast", "northwest", "southeast", "southwest"))

# Predict button
if st.button("Predict Charges"):
    # Preprocess input
    input_data = preprocess_input(age, sex, bmi, children, smoker, region)
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display result
    st.success(f"Predicted Insurance Charges: **${prediction:.2f}**")
