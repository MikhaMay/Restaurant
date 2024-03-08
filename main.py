import psycopg2
import sys
from utils.logger import FileLogger, LogManager
from services.menu_service import Menu
from models.dish import *
from gui.menu_viewer import MenuApp
from PyQt5.QtWidgets import QApplication
from migrations.insert_dishes_into_database import insert_data
from migrations.create_database import create_db_and_tables
from migrations.insert_dishes_into_menu import insert_into_menu


def upload_menu():
    menu = Menu()
    with psycopg2.connect(dbname="restaurant", user="postgres", password="test123", host="localhost") as conn:
        with conn.cursor() as cur:
            for table, dish_type in ('soup', 'Soup'), ('snacks', 'Snacks'), ('main_dishes', 'Main Dishes'):
                cur.execute('''
                                SELECT name, text, price, mass from dishes
                                JOIN %s on dishes.id = %s.id
                                JOIN menu on dishes.id = %s.dish_id; 
                            ''', (table, table, table))
                for name, text, price, mass in cur.fetchall():
                    menu.add_dish(DishFactory.get_dish(dish_type, name, text, price, mass))

            for table, dish_type in ('beverages', 'Beverages'):
                cur.execute('''
                                SELECT name, text, price, volume from dishes
                                JOIN %s on dishes.id = %s.id
                                JOIN menu on dishes.id = %s.dish_id; 
                            ''', (table, table, table))
                for name, text, price, volume in cur.fetchall():
                    menu.add_dish(DishFactory.get_dish(dish_type, name, text, price, volume))

            for table, dish_type in ('garniers', 'Garniers'):
                cur.execute('''
                                SELECT name, text, price, mass, sauce from dishes
                                JOIN %s on dishes.id = %s.id
                                JOIN menu on dishes.id = %s.dish_id; 
                            ''', (table, table, table))
                for name, text, price, mass, sauce in cur.fetchall():
                    menu.add_dish(DishFactory.get_dish(dish_type, name, text, price, mass, sauce))

            for table, dish_type in ('steaks', 'Steakes'):
                cur.execute('''
                                SELECT name, text, price, mass doneness_level from dishes
                                JOIN %s on dishes.id = %s.id
                                JOIN menu on dishes.id = %s.dish_id; 
                            ''', (table, table, table))
                for name, text, price, mass, doneness_level in cur.fetchall():
                    menu.add_dish(DishFactory.get_dish(dish_type, name, text, price, mass, doneness_level))


            
    
    


if __name__ == '__main__':
    LogManager().set_logger(FileLogger('log_file.txt'))


    # create_db_and_tables()

    # insert_data()

    # insert_into_menu()

    # menu = Menu()

    upload_menu()

    app = QApplication(sys.argv)  # Создаем экземпляр приложения

    ex = MenuApp(Menu().items())  # Создаем экземпляр окна приложения, передавая список блюд

    sys.exit(app.exec_())  # Запускаем цикл обработки событий приложения
