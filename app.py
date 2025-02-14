import streamlit as st
import pandas as pd
import pickle

with open('sales_forecasting_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title("Sales Forecasting App")
days = st.slider("Select number of days to forecast", 1, 60, 30)

future_predictions = model.forecast(steps=days)

st.write("Predicted Sales for next", days, "days")
st.line_chart(future_predictions)

