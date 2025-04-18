import streamlit as st

def main():
    pg = st.navigation([
        
        st.title("Diabetes Prediction Using Machine Learning")
        st.write("Welcome to the Home Page of the Diabetes Prediction App.")
    ])
    pg.run()

if __name__ == '__main__':
    main()
