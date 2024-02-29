from utils.logger import FileLogger, LogManager
from services.menu_service import Menu
from models.dish import *
import sys
from gui.menu_viewer import MenuApp
from PyQt5.QtWidgets import QApplication



LogManager().set_logger(FileLogger('log_file.txt'))

LogManager.log_message('_'*10 + 'start' + '_'*10 + '\n')
menu = Menu()

for _ in range(10):
    menu.add_dish(Soup('soup'+str(_+1), 'some text about soup', 5+_*10, 6+_*7))

for _ in range(5):
    menu.add_dish(Beverage('beverage'+str(_+1), 'some text\nabout beverage', 15+_*11, 42+_*3))

for _ in range(14):
    menu.add_dish(Snack('snak'+str(_+1), 'some text\nabout snack', 7+_*13, 52+_*6))

for _ in range(24):
    menu.add_dish(MainCourse('Main Course'+str(_+1), 'some text about this main course', 151+_*6, 312+_*3))

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Создаем экземпляр приложения

    ex = MenuApp(menu.items())  # Создаем экземпляр окна приложения, передавая список блюд

    sys.exit(app.exec_())  # Запускаем цикл обработки событий приложения
