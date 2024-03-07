import psycopg2
import sys
from utils.logger import FileLogger, LogManager
from services.menu_service import Menu
from models.dish import *
from gui.menu_viewer import MenuApp
from PyQt5.QtWidgets import QApplication
from migrations.insert_dishes_into_database import insert_data
from migrations.create_database import create_db_and_tables





if __name__ == '__main__':
    LogManager().set_logger(FileLogger('log_file.txt'))

    # create_db_and_tables()

    # insert_data()

    

    # menu = Menu()

    # app = QApplication(sys.argv)  # Создаем экземпляр приложения

    # ex = MenuApp(menu.items())  # Создаем экземпляр окна приложения, передавая список блюд

    # sys.exit(app.exec_())  # Запускаем цикл обработки событий приложения
