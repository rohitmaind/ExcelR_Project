# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 09:21:14 2024

@author: rohit
"""
import pickle
import streamlit as st
from PIL import Image

# Load your model
load_model = pickle.load(open('bankurpcy_model.pkl', 'rb'))

# App Title with Emoji for style
st.markdown("""
    <div style='background-color:#f8f9fa; padding:10px; border-radius:10px;'>
        <h1 style='text-align:center; color:#4a4a4a;'>💼 Bankruptcy Risk Prediction Portal</h1>
        <h3 style='text-align:center; color:#7a7a7a;'>Accurate Financial Insights for Businesses</h3>
    </div>
    <br>
""", unsafe_allow_html=True)

# Load an image (Optional: You can include a relevant image here)
image = Image.open('finance.jpg')  # Replace with your own image if needed
st.image(image, caption='Financial Stability Assessment', use_column_width=True)

# Define the prediction function
def Prediction(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk):
    result = load_model.predict([[industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]])
    return result[0]

# Apply custom CSS to style the sidebar and main elements
st.markdown("""
    <style>
        /* Sidebar background color */
        [data-testid="stSidebar"] {
            background-color: #2c3e50;
            color: white;
        }

        /* Sidebar text color */
        [data-testid="stSidebar"] h3, [data-testid="stSidebar"] label {
            color: white;
        }

        /* Sidebar input padding */
        [data-testid="stSidebar"] .block-container {
            padding: 20px;
        }

        /* Main content background color */
        .stApp {
            background-color: #f8f9fa;
        }

        /* Button styling */
        .stButton > button {
            background-color: #007BFF;
            color: white;
            font-size: 16px;
            padding: 12px 24px;
            border-radius: 10px;
            border: none;
            font-weight: bold;
            transition: background-color 0.3s ease;
            display: block;
            margin: 0 auto;
        }

        /* Button hover effect */
        .stButton > button:hover {
            background-color: #0056b3;
        }

        /* Custom alert box styles */
        .alert-box {
            padding: 20px;
            margin-top: 20px;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }

        /* Bankruptcy risk alert (red) */
        .bankruptcy-risk {
            background-color: #f8d7da;
            color: #721c24;
        }

        /* No bankruptcy risk alert (green) */
        .no-bankruptcy-risk {
            background-color: #d4edda;
            color: #155724;
        }

        /* Footer style */
        .footer {
            color: #6c757d;
            text-align: center;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Main function for Streamlit web app
def main():
    # Sidebar section for inputs
    st.sidebar.markdown("<h3 style='text-align: center;'>🔧 Input Parameters</h3>", unsafe_allow_html=True)

    # Input options for each feature (default None to force user to choose)
    industrial_risk = st.sidebar.selectbox('Industrial Risk', [None, 0, 0.5, 1], index=0)
    management_risk = st.sidebar.selectbox('Management Risk', [None, 0, 0.5, 1], index=0)
    financial_flexibility = st.sidebar.selectbox('Financial Flexibility', [None, 0, 0.5, 1], index=0)
    credibility = st.sidebar.selectbox('Credibility', [None, 0, 0.5, 1], index=0)
    competitiveness = st.sidebar.selectbox('Competitiveness', [None, 0, 0.5, 1], index=0)
    operating_risk = st.sidebar.selectbox('Operating Risk', [None, 0, 0.5, 1], index=0)

    # Ensure all selections are made before allowing prediction
    if None not in [industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]:
        # Display the prediction button at the bottom of the sidebar
        if st.sidebar.button('Predict'):
            result = Prediction(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk)

            # Display result with customized style
            if result == 0:
                st.markdown("""
                    <div class='alert-box bankruptcy-risk'>
                        ❗ <strong>Prediction: Bankruptcy Risk</strong><br>
                        The financial indicators suggest a risk of bankruptcy.
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class='alert-box no-bankruptcy-risk'>
                        ✅ <strong>Prediction: No Bankruptcy Risk</strong><br>
                        The financial indicators suggest that the company is stable with no immediate bankruptcy risk.
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.sidebar.warning('⚠️ Please select all the values before predicting.')

    # Add a footer section
    st.markdown("""
        <div class='footer'>
            Developed by Rohit Maind | 2024 ©
        </div>
    """, unsafe_allow_html=True)

# Run the main function
if __name__ == '__main__':
    main()
