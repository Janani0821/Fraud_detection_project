import streamlit as st
import joblib
import pandas as pd

model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction App")

st.markdown("Please enter the transaction details and use press the Predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("old Balance (sender)", min_value=0.0, value=10000.0)
newbalanceOrg = st.number_input("new Balance (sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("old Balance (receiver)", min_value=0.0, value=0.0) 
newbalanceDest = st.number_input("new Balance (receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame( [ {
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrg,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])
    
    prediction = model.predict(input_data)[0]
    
    st.subheader(f"Prediction: { int(prediction) }")
    
    if prediction == 1:
        st.error("This transaction can be fraud.")
    else: 
        st.success("This transaction can be not a fraud")    