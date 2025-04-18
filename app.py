import streamlit as st

def main():
    pg = st.navigation([
        
        st.Page("pages/About_project.py", title="Home"),
        st.Page('pages/Prediction.py', title="Predict"),
    ])
    pg.run()

if __name__ == '__main__':
    main()
