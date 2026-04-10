import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl


# 🔥 FUNÇÃO QUE FUNCIONA NO PYCHARM E NO EXE
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # quando está em .exe
    except Exception:
        base_path = os.path.abspath(".")  # quando está no PyCharm

    return os.path.join(base_path, relative_path)


def main():
    app = QApplication(sys.argv)

    view = QWebEngineView()

    # 📄 pega o HTML do jeito seguro
    file_path = resource_path("hello_kitty_finance_app.html")
    view.load(QUrl.fromLocalFile(file_path))

    # 🌐 carrega no navegador interno
    view.load(QUrl.fromLocalFile(file_path))

    view.setWindowTitle("💖 Kitty Finances")
    view.resize(1000, 700)
    view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
