# 📈 Stock Investment Portfolio Optimizer

Это интерактивное Streamlit-приложение помогает оптимизировать распределение инвестиций между акциями на основе исторической доходности и риска (волатильности).


## 🚀 Как запустить

1. Клонируй репозиторий
        
        git clone https://github.com/твой-профиль/stock-optimizer.git
        cd stock-optimizer

2. Активируй (Windows)

        python -m venv venv
        venv\Scripts\activate

Установи зависимости

        pip install -r requirements.txt

Сохрани список зависимостей
        
        pip freeze > requirements.txt

Запусти приложение

        streamlit run app.py

## 🧠 Что делает приложение
- Загружает котировки выбранных акций через yfinance
- Вычисляет доходность, ковариацию и оптимизирует портфель
- Отображает:
  - Идеальные веса в портфеле
  - Годовую доходность, риск и Sharpe Ratio
  - Круговую диаграмму распределения

## 🛠 Используемые библиотеки
   - Streamlit
   - yFinance
   - NumPy
   - pandas
   - Matplotlib
   - SciPy

Разработано с ❤️ для частных инвесторов и аналитиков.