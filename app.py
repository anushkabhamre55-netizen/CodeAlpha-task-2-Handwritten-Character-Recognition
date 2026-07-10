import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("digit_model.pkl", "rb"))

st.title("📝 Handwritten Digit Recognition System")

st.write("Enter pixel values (0 to 16) and click Predict.")

features = []

# Create 64 input boxes
for i in range(64):
    value = st.number_input(
        f"Pixel {i+1}",
        min_value=0.0,
        max_value=16.0,
        value=0.0
    )
    features.append(value)

if st.button("Predict Digit"):

    prediction = model.predict([features])

    st.success(f"Predicted Digit: {prediction[0]}")