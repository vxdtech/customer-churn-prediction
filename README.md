# Customer Churn Prediction(Retail Banking Customer Risk Analytics)

## 📌 Project Overview

This project focuses on predicting **customer churn** using machine learning techniques.
The goal is to identify customers who are likely to leave the service so that businesses can take proactive retention actions.

The project uses a real-world style dataset (Lloyds Banking–inspired) and follows an **end-to-end ML workflow**, including data cleaning, feature engineering, model training, and evaluation.

---

## 🎯 Problem Statement

Customer churn leads to revenue loss and increased acquisition costs.
By predicting churn in advance, companies can:

* Target high-risk customers
* Improve retention strategies
* Optimize marketing and customer support efforts

---

## 🧠 Solution Approach

* Performed **Exploratory Data Analysis (EDA)** to understand customer behavior
* Cleaned and preprocessed raw data
* Engineered relevant features
* Trained a **Random Forest Classifier** for churn prediction
* Saved the trained model for reuse and deployment

---

## ⚙️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib
* **Model:** Random Forest Classifier
* **Environment:** Jupyter Notebook, Python script

---

## 📂 Project Structure

```
customer-churn-prediction/
│── README.md
│── app.py                      # Model loading & inference script
│── lloyd.ipynb                 # EDA + model training notebook
│── cleaned_lloyd_data.csv      # Preprocessed dataset
│── rf_lloyd_churn_model.pkl    # Trained ML model
│── .gitignore
│── LICENSE
```

---

## 📊 Model Performance

* Model trained to classify customers as **Churn / No Churn**
* Evaluation performed using accuracy and classification metrics
* Feature importance analyzed to understand key churn drivers

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone https://github.com/vxdtech/customer-churn-prediction.git
```

2. Install dependencies

```bash
pip install pandas numpy scikit-learn matplotlib
```

3. Run the notebook or script

```bash
python app.py
```

---

## 🔮 Future Improvements

* Add hyperparameter tuning
* Include SHAP for model explainability
* Deploy as a web app using Flask or Streamlit
* Add real-time prediction API

---

## 👤 Author

**Varad Nagilla**
Final-year Computer Engineering student
Interests: Data Science, Machine Learning, FinTech & Applied AI

---

## 📜 License

This project is licensed under the **MIT License**.

