# 🏦 Loan Status Prediction API

This project predicts whether a loan application will be **approved** or **not approved** using a **Machine Learning model** deployed via a **FastAPI** backend. The model is trained on real-world loan data and provides predictions through a RESTful API interface.

---

## 🔍 Project Overview

- Trained a **Logistic Regression** model to predict loan approval status.
- Achieved **85%+ accuracy** using key applicant features such as income, credit history, and property area.
- Built an **interactive API** using **FastAPI** to serve the model and handle prediction requests.
- Tested the API using **Postman**, ensuring fast and reliable predictions.
- Structured the backend for easy scaling, deployment, and microservice integration.

---

## ⚙️ Technologies Used

- **Python** (Pandas, NumPy, Scikit-learn, Joblib)
- **FastAPI** for API development
- **Pydantic** for input data validation
- **Postman** for testing API endpoints

---



# 🏦 Loan Approval Prediction API

A high-performance **FastAPI**-based REST API that predicts loan approval status using a **machine learning model** trained on financial and demographic data. Built to demonstrate real-world application of data science and MLOps in production environments.

---

## 🚀 Features

- ✅ Loan Approval Prediction (Approved / Not Approved)
- 🧠 ML Model: Logistic Regression
- ⚙️ Preprocessing with `StandardScaler` for numerical features
- 🔁 Built with **FastAPI** for fast, asynchronous API calls
- 📦 Model and scaler loaded using `joblib`
- 📊 Features used: Income, Credit History, Loan Amount, Property Area, and more

---

## 📈 Model Performance

| Metric         | Value     |
|----------------|-----------|
| Accuracy       | 85%       |
| Response Time  | < 100 ms  |
| Algorithm      | Logistic Regression |
| Scaler         | StandardScaler |

---

## 🧪 Sample API Request (via POST)

### Endpoint
### JSON Payload

```json
{
  "Gender": 1,
  "Married": 1,
  "Dependents": 0,
  "Education": 0,
  "Self_Employed": 0,
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 2000,
  "LoanAmount": 150,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Property_Area": 2
}
{
  "Loan Status": "Approved"
}
