import psycopg2
import sys
from utils.logger import FileLogger, LogManager
from services.menu_service import Menu, upload_menu
from gui.menu_viewer import MenuApp
from PyQt5.QtWidgets import QApplication
from db.db_setup import create_db_and_initialize_tables
from db.fill_dishes import fill_tables
from db.fill_menu import fill_menu_table

dbparams = {'dbname':"restaurant", 'user':"postgres", 'password':"test123", 'host':"localhost"}


    


if __name__ == '__main__':
    LogManager().set_logger(FileLogger('log_file.txt'))


    # create_db_and_initialize_tables(dbparams)     # инициализация базы данных и заполнение таблиц
    # fill_tables(dbparams)                         # используется при первом запуске
    # fill_menu_table(dbparams)                     # приложения

    menu = Menu()

    upload_menu(dbparams)

    
    # print(Menu().items().keys())
    app = QApplication(sys.argv) 

    ex = MenuApp(Menu().items())  # Создаем экземпляр окна приложения, передавая список блюд


    sys.exit(app.exec_())  
