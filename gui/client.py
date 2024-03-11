import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QLineEdit
from PyQt5.QtCore import pyqtSlot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное меню")
        self.setGeometry(100, 100, 280, 100)

        layout = QVBoxLayout()

        self.btn_register = QPushButton("Регистрация")
        self.btn_register.clicked.connect(self.on_register)
        layout.addWidget(self.btn_register)

        self.btn_login = QPushButton("Авторизация")
        self.btn_login.clicked.connect(self.on_login)
        layout.addWidget(self.btn_login)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    @pyqtSlot()
    def on_register(self):
        print("Открытие формы регистрации...")
        register_dialog = RegisterDialog()
        register_dialog.exec_()

    @pyqtSlot()
    def on_login(self):
        print("Открытие формы авторизации...")
        login_dialog = LoginDialog()
        login_dialog.exec_()

class RegisterDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.setGeometry(100, 100, 200, 200)

        layout = QVBoxLayout()

        self.edit_name = QLineEdit(self)
        self.edit_name.setPlaceholderText("Имя пользователя")
        layout.addWidget(self.edit_name)

        self.edit_phone = QLineEdit(self)
        self.edit_phone.setPlaceholderText("Телефон")
        layout.addWidget(self.edit_phone)

        self.edit_password = QLineEdit(self)
        self.edit_password.setPlaceholderText("Пароль")
        layout.addWidget(self.edit_password)

        self.btn_register = QPushButton("Зарегистрироваться")
        self.btn_register.clicked.connect(self.register)
        layout.addWidget(self.btn_register)

        self.setLayout(layout)

    def register(self):
        name = self.edit_name.text()
        phone = self.edit_phone.text()
        password = self.edit_password.text()
        print(f"Регистрация пользователя: {name}, Телефон: {phone}, Пароль: {password}")
        # Здесь добавьте логику добавления пользователя в базу данных


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setGeometry(100, 100, 200, 150)

        layout = QVBoxLayout()

        self.edit_name = QLineEdit(self)
        self.edit_name.setPlaceholderText("Имя пользователя")
        layout.addWidget(self.edit_name)

        self.edit_password = QLineEdit(self)
        self.edit_password.setPlaceholderText("Пароль")
        layout.addWidget(self.edit_password)

        self.btn_login = QPushButton("Войти")
        self.btn_login.clicked.connect(self.login)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def login(self):
        name = self.edit_name.text()
        password = self.edit_password.text()
        print(f"Попытка авторизации пользователя: {name}, Пароль: {password}")
        # Здесь добавьте логику проверки пользователя в базе данных
