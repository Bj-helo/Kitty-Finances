# 💖 Kitty Finances

Kitty Finances is a simple desktop finance app built with Python and PyQt6.  
It helps you track expenses, view summaries, and visualize your financial data in a cute and easy way.

Features
- Dashboard with financial overview
- Expense tracking
- Monthly cost visualization
- SQLite database integration
- Cute UI design (Hello Kitty style 🎀)

How to Run (Development)
Install dependencies
tkinter; 
customtkinter; 
PyQt6;
PyQt6-WebEngine;
pythonnet; pywebview or pywebview==4.4.1
And used pip install -r requirements.txt

Run the app
python main.py

How to Build the .exe
python -m PyInstaller --onedir --windowed --icon=icon.ico --add-data "hello_kitty_finance_app.html;." main.py

