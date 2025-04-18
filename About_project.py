import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("About the Diabetes Prediction Project")

st.markdown("""
    ## Objective
    The primary goal of this project is to leverage machine learning to assist in the early detection of diabetes, enabling timely intervention and management. By analyzing features such as glucose levels, BMI, age, and other health metrics, the model provides a probabilistic prediction of diabetes risk.

    ## Machine Learning Approach
    ### Dataset
    The model is trained on a publicly available diabetes dataset (e.g., Pima Indians Diabetes Dataset), which includes features like:
    - Glucose levels
    - Body Mass Index (BMI)
    - Blood pressure
    - Age
    - Insulin levels
    - Diabetes pedigree function
    - Number of pregnancies (where applicable)

    The final model was selected based on metrics such as accuracy, precision, recall, F1-score, and AUC-ROC, ensuring reliable predictions.

    ## Technologies Used
    - **Streamlit**: For building the web application.
    - **Python**: Core programming language.
    - **Scikit-learn**: For machine learning model development.
    - **Pandas & NumPy**: For data manipulation and preprocessing.
    - **Matplotlib & Seaborn**: For visualizations.
      
    *Built with using Streamlit and Machine Learning*
    """)