import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="AI Portfolio Intelligence Platform", layout="wide")

st.title("📈 AI-Powered Portfolio Intelligence Platform")

# Sample Portfolio Data
portfolio = pd.DataFrame({
    "Stock": ["RELIANCE", "TCS", "INFY", "HDFCBANK"],
    "Quantity": [10, 5, 8, 6],
    "Buy Price": [2500, 3800, 1500, 1600],
    "Current Price": [2900, 4100, 1800, 1900]
})

portfolio["Investment"] = portfolio["Quantity"] * portfolio["Buy Price"]
portfolio["Current Value"] = portfolio["Quantity"] * portfolio["Current Price"]
portfolio["Profit/Loss"] = portfolio["Current Value"] - portfolio["Investment"]

st.subheader("📋 Portfolio Holdings")
st.dataframe(portfolio, use_container_width=True)

# Portfolio Summary
total_investment = portfolio["Investment"].sum()
current_value = portfolio["Current Value"].sum()
profit = portfolio["Profit/Loss"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Investment", f"₹{total_investment:,.0f}")
col2.metric("Current Value", f"₹{current_value:,.0f}")
col3.metric("Profit / Loss", f"₹{profit:,.0f}")

st.markdown("---")

# Health Score
st.subheader("🏆 Portfolio Health Score")

score = 88

st.metric("Portfolio Score", f"{score}/100")

if score >= 80:
    st.success("Excellent Diversification")
elif score >= 60:
    st.warning("Moderate Diversification")
else:
    st.error("High Risk Portfolio")

# Risk Analysis
st.subheader("⚠ Risk Analysis")

if score >= 80:
    st.success("Risk Level : Low")
elif score >= 60:
    st.warning("Risk Level : Medium")
else:
    st.error("Risk Level : High")

# Pie Chart
st.subheader("🥧 Portfolio Allocation")

fig = px.pie(
    portfolio,
    values="Current Value",
    names="Stock",
    title="Portfolio Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# Top Performer
st.subheader("🚀 Portfolio Insights")

best_stock = portfolio.loc[portfolio["Profit/Loss"].idxmax()]
worst_stock = portfolio.loc[portfolio["Profit/Loss"].idxmin()]

col4, col5 = st.columns(2)

with col4:
    st.success(
        f"Top Performer: {best_stock['Stock']} (₹{best_stock['Profit/Loss']:,.0f})"
    )

with col5:
    st.error(
        f"Worst Performer: {worst_stock['Stock']} (₹{worst_stock['Profit/Loss']:,.0f})"
    )

# AI Recommendation
st.subheader("🤖 AI Investment Recommendation")

st.info("""
• Portfolio is moderately diversified.

• Consider increasing Banking exposure.

• FMCG stocks can reduce volatility.

• Long-term growth outlook is positive.

• Maintain SIP discipline.
""")

# Investment Simulator
st.subheader("💰 Investment Simulator")

sip = st.number_input(
    "Monthly SIP (₹)",
    min_value=1000,
    value=5000
)

years = st.slider(
    "Years",
    1,
    30,
    10
)

rate = st.slider(
    "Expected Return (%)",
    1,
    20,
    12
)

future_value = sip * (((1 + rate/100/12)**(years*12) - 1)/(rate/100/12))

st.success(
    f"Estimated Future Value : ₹{future_value:,.0f}"
)

# Benchmark Comparison
st.subheader("📊 NIFTY Benchmark Comparison")

portfolio_return = 18
nifty_return = 12

col6, col7 = st.columns(2)

col6.metric("Portfolio Return", f"{portfolio_return}%")
col7.metric("NIFTY Return", f"{nifty_return}%")

if portfolio_return > nifty_return:
    st.success(
        f"Portfolio Outperformed NIFTY by {portfolio_return - nifty_return}%"
    )
else:
    st.warning(
        "Portfolio Underperformed NIFTY"
    )

# Download Report
st.subheader("📥 Download Portfolio Report")

csv = portfolio.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download CSV Report",
    csv,
    "portfolio_report.csv",
    "text/csv"
)
