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
- **Matplotlib** & **Seaborn** for EDA and visualization

---



📦 Sample Request & Response
✅ Request (JSON Payload)
json
Copy
Edit
POST /predict
Content-Type: application/json

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
📤 Response
json
Copy
Edit
{
  "Loan Status": "Approved"
}
⚙️ Features
Real-time loan status prediction via API

Built with FastAPI for high-performance and asynchronous I/O

Preprocessing includes feature scaling using StandardScaler

Uses a pre-trained Logistic Regression model serialized with joblib

🚀 Performance Metrics
✅ Accuracy: 85% on validation dataset

⚡ API Latency: < 100 ms average response time

🔑 Important Features:

ApplicantIncome

CoapplicantIncome

LoanAmount

Loan_Amount_Term

Credit_History

Property_Area

Categorical Encoded Variables like Gender, Married, Education



Credit_History

Property_Area

Education, Married, etc.

