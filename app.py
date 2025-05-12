from fastapi import FastAPI
from pydantic import BaseModel
import joblib 
import pandas as pd

# Load model and scaler
model = joblib.load('loan_status_predictor.pkl')
scaler = joblib.load('vector.pkl')

# Define FastAPI app
app = FastAPI()

# Numerical columns to scale
num_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

# Define the request body structure
class LoanApproval(BaseModel):
    Gender: float 
    Married: float
    Dependents: float
    Education: float
    Self_Employed: float
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float 
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: float

# Define prediction endpoint
@app.post("/predict")
async def predict_loan_status(application: LoanApproval):  
    input_data = pd.DataFrame([application.dict()])
    input_data[num_cols] = scaler.transform(input_data[num_cols])
    result = model.predict(input_data)
    return {'Loan Status': "Approved" if result[0] == 1 else "Not Approved"}