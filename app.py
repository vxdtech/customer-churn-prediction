import streamlit as st
import joblib
import numpy as np

# ==========================
# 🎯 LOAD TRAINED MODEL
# ==========================
model = joblib.load(r"E:\data science\projects\Llyod_bank\rf_lloyd_churn_model.pkl")

# ==========================
# 🎮 APP CONFIG
# ==========================
st.set_page_config(
    page_title="Lloyd Bank Churn Predictor 🎯",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================
# 💅 CUSTOM STYLING (improved readability)
# ==========================
st.markdown("""
    <style>
    /* --------- APP BACKGROUND --------- */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }

    /* --------- TITLES --------- */
    .main-title {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        color: #00ffcc;
        text-shadow: 2px 2px 4px #000;
        margin-bottom: 0.2em;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2em;
        color: #ccc;
        margin-bottom: 2em;
    }

    /* --------- WIDGET LABELS --------- */
    label, .stSlider label, .stSelectbox label, .stNumberInput label, .stCheckbox label {
        color: white !important;
        font-weight: 500;
    }

    /* --------- INPUT TEXT / VALUES --------- */
    input, select, textarea, .stNumberInput input, .stSelectbox div[data-baseweb="select"] * {
        color: white !important;
        background-color: #1b2a33 !important;
        border-radius: 8px !important;
    }

    /* --------- DROPDOWN & SELECTBOX TEXT --------- */
    div[data-baseweb="select"] span {
        color: white !important;
    }

    /* --------- SLIDERS --------- */
    .stSlider span, .stSlider div {
        color: white !important;
    }

    /* --------- BUTTONS --------- */
    .stButton>button {
        background-color: #00ffcc;
        color: #000;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 0 10px #00ffcc44;
    }
    .stButton>button:hover {
        background-color: #00ccaa;
        transform: scale(1.05);
        box-shadow: 0 0 20px #00ffcc99;
    }

    /* --------- PREDICTION BOX --------- */
    .prediction-box {
        background-color: #ffffff10;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        color: white;
        font-size: 1.4em;
        margin-top: 1.5em;
        box-shadow: 0px 0px 10px #00ffcc55;
    }

    /* --------- SLIDER VALUE TEXT --------- */
    .css-1dp5vir, .css-10trblm, .stSlider, .stNumberInput {
        color: white !important;
    }

    /* --------- GENERAL TWEAKS --------- */
    ::placeholder {
        color: #ccc !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================
# 🏦 TITLE
# ==========================
st.markdown('<div class="main-title">Lloyd Bank Churn Prediction 💳</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Predict if a customer will churn based on their activity and demographics</div>', unsafe_allow_html=True)

# ==========================
# 🧩 INPUT FEATURES
# ==========================
st.header("🧠 Enter Customer Details")

col1, col2 = st.columns(2)

with col1:
    Age = st.slider("Age", 18, 90, 30)
    Total_Transactions = st.slider("Total Transactions", 0, 50, 5)
    Avg_Amount_Spent = st.number_input("Average Amount Spent ($)", 0.0, 10000.0, 500.0, step=50.0)
    Num_Product_Categories = st.slider("Number of Product Categories", 0, 10, 2)
    Total_Interactions = st.slider("Total Interactions", 0, 100, 20)
    Complaint_Count = st.slider("Complaint Count", 0, 10, 0)
    Unresolved_Count = st.slider("Unresolved Issues", 0, 10, 0)
    LoginFrequency = st.slider("Login Frequency", 0, 100, 10)
    Days_Since_Last_Login = st.slider("Days Since Last Login", 0, 365, 30)

with col2:
    Gender_M = st.selectbox("Gender", ["Female", "Male"])
    MaritalStatus = st.selectbox("Marital Status", ["Married", "Single", "Widowed"])
    IncomeLevel = st.selectbox("Income Level", ["Low", "Medium", "High"])
    ServiceUsage_Online_Banking = st.checkbox("Uses Online Banking")
    ServiceUsage_Website = st.checkbox("Uses Website")

# ==========================
# ⚙️ ENCODE INPUTS
# ==========================
Gender_M = 1 if Gender_M == "Male" else 0
MaritalStatus_Married = 1 if MaritalStatus == "Married" else 0
MaritalStatus_Single = 1 if MaritalStatus == "Single" else 0
MaritalStatus_Widowed = 1 if MaritalStatus == "Widowed" else 0
IncomeLevel_Low = 1 if IncomeLevel == "Low" else 0
IncomeLevel_Medium = 1 if IncomeLevel == "Medium" else 0

# Feature order must match training
features = np.array([[
    Age, Total_Transactions, Avg_Amount_Spent,
    Num_Product_Categories, Total_Interactions, Complaint_Count,
    Unresolved_Count, LoginFrequency, Days_Since_Last_Login,
    Gender_M, MaritalStatus_Married, MaritalStatus_Single,
    MaritalStatus_Widowed, IncomeLevel_Low,
    int(ServiceUsage_Online_Banking), int(ServiceUsage_Website)
]])

# ==========================
# 🧮 PREDICTION
# ==========================
if st.button("🎯 Predict Churn"):
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.markdown(
            f"<div class='prediction-box' style='color:#ff4b4b;'>🚨 Customer is <b>likely to churn</b>!</div>",
            unsafe_allow_html=True
        )
        st.snow()
    else:
        st.markdown(
            f"<div class='prediction-box' style='color:#00ffcc;'>✅ Customer is <b>not likely to churn</b>.</div>",
            unsafe_allow_html=True
        )
        st.balloons()

# ==========================
# 🎮 FOOTER
# ==========================
st.markdown("""
---
💡 **Tip:** Use sliders and toggles like a control panel — tweak values to see how customer behavior affects churn likelihood!
""")
