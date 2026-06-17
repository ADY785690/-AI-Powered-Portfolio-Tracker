import streamlit as st
import pandas as pd

st.title("📈 AI-Powered Portfolio Tracker")

df = pd.read_csv("data/portfolio.csv")

st.subheader("Portfolio Holdings")
st.dataframe(df)

st.subheader("Add New Stock")

symbol = st.text_input("Stock Symbol")
qty = st.number_input("Quantity", min_value=1)
price = st.number_input("Buy Price", min_value=0.0)

if st.button("Add Stock"):
    st.success(f"{symbol} added successfully!")

st.subheader("Portfolio Summary")

total_investment = (df["Quantity"] * df["BuyPrice"]).sum()

st.metric("Total Investment", f"₹{total_investment:,.2f}")

st.bar_chart(df["Quantity"])
