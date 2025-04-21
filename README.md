# 📈 Stock Investment Portfolio Optimizer

This interactive Streamlit app helps optimize your stock portfolio based on historical return and volatility.

[![Streamlit App](https://img.shields.io/badge/Live%20App-Open%20Now-brightgreen?style=for-the-badge)](https://stockportfoliooptimizer-vekh.streamlit.app/)

### 🧠 What it does
- Downloads adjusted close prices from Yahoo Finance
- Calculates expected return and risk (volatility)
- Uses SciPy to maximize the Sharpe Ratio
- Shows:
    - Optimal stock weights
    - Annual return, risk, Sharpe Ratio
    - Pie chart of allocation


### 🚀 Features

- 🧠 **Smart Portfolio Optimization** using the Sharpe Ratio
- 📉 Pulls **historical stock data** from Yahoo Finance
- 📊 Visualizes allocation with interactive **charts**
- 💼 Great for personal investors and finance students
- ☁️ Hosted on **Streamlit Community Cloud**



### 🛠 Technologies
- Streamlit
- yfinance
- NumPy
- pandas
- matplotlib
- SciPy

## 🚀 How to Run Local

1. Clone the repository

        git clone https://github.com/your-username/stock-optimizer.git
        cd stock-optimizer

2. Create and activate virtual environment
        python -m venv venv
        venv\Scripts\activate   # Windows

3. Install requirements

        pip install -r requirements.txt

4. Launch the app

        streamlit run app.py

Built with ❤️ by a passionate investor and data enthusiast