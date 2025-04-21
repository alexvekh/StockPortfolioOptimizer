# 📈 Stock Investment Portfolio Optimizer

Это интерактивное Streamlit-приложение помогает оптимизировать распределение инвестиций между акциями на основе исторической доходности и риска (волатильности).

[![Streamlit App](https://img.shields.io/badge/Live%20App-Open%20Now-brightgreen?style=for-the-badge)](https://stockportfoliooptimizer-vekh.streamlit.app/)

## 🧠 Что делает приложение
- Загружает котировки выбранных акций через yfinance
- Вычисляет доходность, ковариацию и оптимизирует портфель
- Отображает:
  - Идеальные веса в портфеле
  - Годовую доходность, риск и Sharpe Ratio
  - Круговую диаграмму распределения

## 🚀 Как запустить локально

1. Клонируй репозиторий
        
        git clone https://github.com/твой-профиль/stock-optimizer.git
        cd stock-optimizer

2. Создай и активируй venv

        python -m venv venv
        venv\Scripts\activate

3. Установи зависимости

        pip install -r requirements.txt

4. Запусти приложение

        streamlit run app.py

## 🛠 Используемые библиотеки
   - Streamlit
   - yFinance
   - NumPy
   - pandas
   - Matplotlib
   - SciPy

Разработано с ❤️ для частных инвесторов и аналитиков.