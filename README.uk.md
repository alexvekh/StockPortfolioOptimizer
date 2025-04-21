# 📈 Stock Investment Portfolio Optimizer

Оптимізатор Інвестиційного Портфеля Акцій

Це інтерактивний додаток на базі Data Science, який допомагає оптимізувати розподіл інвестицій між акціями на основі історичної прибутковості та ризику.


[![Streamlit App](https://img.shields.io/badge/Live%20App-Open%20Now-brightgreen?style=for-the-badge)](https://stockportfoliooptimizer-vekh.streamlit.app/)



### 🧠 Що робить додаток
- Завантажує котирування акцій з Yahoo Finance
- Розраховує очікувану прибутковість і ризик (волатильність)
- Знаходить оптимальні ваги для акцій на основі коефіцієнта Шарпа
- Показує:
    - Розподіл ваг в портфелі
    - Очікувану річну прибутковість, ризик і Sharpe Ratio
    - Кругову діаграму


### 🛠 Використані технології
- Streamlit
- yfinance
- NumPy
- pandas
- matplotlib
- SciPy


## 🚀 Як запустити

1. Клонуй репозиторій

        git clone https://github.com/твой-профиль/stock-optimizer.git
        cd stock-optimizer

2. Створи та активуй віртуальне середовище

        python -m venv venv
        venv\Scripts\activate

3. Встанови залежності

        pip install -r requirements.txt

4. Запусти застосунок

        streamlit run app.py





Розроблено з ❤️ для інвесторів та аналітиків