import psycopg2
import sys
from utils.logger import FileLogger, LogManager
from services.menu_service import Menu, upload_menu
from gui.menu_viewer import MenuApp
from PyQt5.QtWidgets import QApplication
from db.db_setup import create_db_and_initialize_tables
from db.fill_dishes import fill_tables
from db.fill_menu import fill_menu_table
from gui.client import MainWindow

dbparams = {'dbname':"restaurant", 'user':"postgres", 'password':"test123", 'host':"localhost"}


    


if __name__ == '__main__':
    LogManager().set_logger(FileLogger('log_file.txt'))


    # create_db_and_initialize_tables(dbparams)
    # fill_tables(dbparams)
    # fill_menu_table(dbparams)

    # menu = Menu()

    # upload_menu(dbparams)

    
    # print(Menu().items().keys())
    app = QApplication(sys.argv)  # Создаем экземпляр приложения

    # ex = MenuApp(Menu().items())  # Создаем экземпляр окна приложения, передавая список блюд

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())  # Запускаем цикл обработки событий приложения
