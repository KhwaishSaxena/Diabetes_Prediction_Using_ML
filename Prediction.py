import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

model = pickle.load(open("model.pkl", "rb"))
    
st.title('Diabetes Prediction Using Machine Learning')
Pregnancies=st.number_input("Pregnancies",min_value=0,format="%d",help="Number of times Pregnant")
Glucose=st.number_input("Glucose",min_value=0,format="%d",help="Plasma Glucose Concentration")
BloodPressure=st.number_input("BloodPressure",min_value=0,format="%d",help="Diastolic Blood Pressure (mm Hg)")
SkinThickness=st.number_input("SKinThickness",min_value=0,format="%d",help="Triceps skin fold thickness (in mm)")
Insulin=st.number_input("Insulin",min_value=0,format="%d",help="2-Hour Serum Insulin (mu U/ml)")
BMI=st.number_input("BMI",min_value=0.0,help="Body Mass Index")
DiabetesPedigreeFunction=st.number_input("DiabetesPedigreeFunction",help="likelihood of diabetes based on genetic/hereditary factors")
Age=st.number_input("Age",min_value=0,max_value=100,format="%d",help="Age in years")

if st.button("Predict"):
    input_array = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    def predict(input_array):
        y_pred=model.predict(input_array)
        y_prob=model.predict_proba(input_array)
        if y_pred == 1:
            prediction = "Based on your input"
            confidence = y_prob
        else:
            prediction = "Great News! No Indication of Diabetes"
            confidence = (100 - y_prob)

        st.markdown(f"Based on your input : {prediction}")
        st.markdown(f"Confidence : {confidence}")
    on_click=predict(input_array)

if __name__ == '__page__':
    predict()