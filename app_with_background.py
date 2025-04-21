import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from PIL import Image
import base64

# --- Set Page Config ---
st.set_page_config(page_title="Stock Portfolio Optimizer", layout="centered")

# --- Background Image as Fullscreen ---
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("spobanner.png")

# --- Title ---
st.title("📈 Stock Investment Portfolio Optimizer")

# --- Sidebar Inputs ---
st.sidebar.header("⚙️ Portfolio Settings")
ticker_input = st.sidebar.text_input("Enter stock tickers (comma separated):", "AAPL, MSFT, GOOGL, AMZN, META")
tickers = [t.strip().upper() for t in ticker_input.split(",") if t.strip()]

start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2024-01-01"))

run_button = st.sidebar.button("🚀 Optimize Portfolio")

if run_button:
    st.write(f"### Optimizing portfolio for: {', '.join(tickers)}")

    # --- Data Download ---
    data = yf.download(tickers, start=start_date, end=end_date)['Close']
    returns = data.pct_change().dropna()
    mean_returns = returns.mean() * 252
    cov_matrix = returns.cov() * 252

    # --- Portfolio Optimization ---
    def portfolio_performance(weights, mean_returns, cov_matrix):
        returns = np.dot(weights, mean_returns)
        std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        return returns, std_dev

    def negative_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate=0.01):
        p_return, p_std_dev = portfolio_performance(weights, mean_returns, cov_matrix)
        return -(p_return - risk_free_rate) / p_std_dev

    def check_sum(weights):
        return np.sum(weights) - 1

    num_assets = len(tickers)
    init_guess = num_assets * [1. / num_assets]
    bounds = tuple((0, 1) for _ in range(num_assets))
    constraints = ({'type': 'eq', 'fun': check_sum})

    optimized = minimize(negative_sharpe_ratio, init_guess,
                         args=(mean_returns, cov_matrix),
                         method='SLSQP', bounds=bounds, constraints=constraints)

    optimal_weights = optimized.x
    expected_return, expected_risk = portfolio_performance(optimal_weights, mean_returns, cov_matrix)
    sharpe_ratio = (expected_return - 0.01) / expected_risk

    # --- Display Results ---
    results_df = pd.DataFrame({
        'Ticker': tickers,
        'Weight': [f"{w:.2%}" for w in optimal_weights]
    })

    st.subheader("📊 Optimal Portfolio Allocation")
    st.dataframe(results_df.set_index('Ticker'))

    st.markdown(f"**Expected Annual Return:** `{expected_return:.2%}`")
    st.markdown(f"**Expected Volatility:** `{expected_risk:.2%}`")
    st.markdown(f"**Sharpe Ratio:** `{sharpe_ratio:.2f}`")

    # --- Pie Chart ---
    fig, ax = plt.subplots()
    ax.pie(optimal_weights, labels=tickers, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')
    st.pyplot(fig)

    st.success("✅ Optimization complete!")
