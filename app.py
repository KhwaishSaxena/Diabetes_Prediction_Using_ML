import streamlit as st
import pandas as pd
import numpy as np
import pickle


model = pickle.load(open("model.pkl", "rb"))
    
st.title('Diabetes Prediction Using Machine Learning')
Pregnancies=st.number_input("Pregnancies",min_value=0,format="%d")
Glucose=st.number_input("Glucose",min_value=0,format="%d")
BloodPressure=st.number_input("BloodPressure",min_value=0,format="%d")
SkinThickness=st.number_input("SKinThickness",min_value=0,format="%d")
Insulin=st.number_input("Insulin",min_value=0,format="%d")
BMI=st.number_input("BMI",min_value=0.0)
DiabetesPedigreeFunction=st.number_input("DiabetesPedigreeFunction")
Age=st.number_input("Age",min_value=0,max_value=100,format="%d")

input_array = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

def predict(input_array):
    y_pred=model.predict(input_array)
    prediction = "Yes" if y_pred == 1 else "No"

    st.write(f"Diabetes Prediction: {prediction}")
    
st.button("Predict",on_click=predict(input_array))


    


