import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))
    
st.title('Diabetes Prediction Using Machine Learning')
Pregnancies=st.number_input("Pregnancies",min_value=0,format="%d",help="Number of pregnancies")
Glucose=st.number_input("Glucose",min_value=0,format="%d",help="Plasma Glucose Concentration")
BloodPressure=st.number_input("Blood Pressure",min_value=0,format="%d",help="Diastolic Blood Pressure (mm Hg)")
SkinThickness=st.number_input("Skin Thickness",min_value=0,format="%d",help="Triceps skin fold thickness (in mm)")
Insulin=st.number_input("Insulin",min_value=0,format="%d",help="2-Hour Serum Insulin (mu U/ml)")
BMI=st.number_input("BMI",min_value=0.0,help="Body Mass Index")
DiabetesPedigreeFunction=st.number_input("Diabetes Pedigree Function",help="Likelihood of diabetes based on genetic/hereditary factors")
Age=st.number_input("Age",min_value=0,max_value=100,format="%d",help="Age in years")

if st.button("Predict"):
    input_array = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    def predict(input_array):
        y_pred=model.predict(input_array)
        y_prob=model.predict_proba(input_array)[0][1]
        if y_pred == 1:
            prediction = "Diabetic "
            confidence = y_prob
        else:
            prediction = " Non Diabetic"
            confidence = (100 - y_prob)

        st.markdown(f"Based on your input: {prediction}")
        st.markdown(f"Confidence: {confidence:.2f}%")
    on_click=predict(input_array)

if __name__ == '__page__':
    predict()
