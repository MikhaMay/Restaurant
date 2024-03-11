from utils.logger import LogManager
from collections import defaultdict
import psycopg2
from models.dish import DishFactory


class Menu:
    _instance = None
    _dishes = defaultdict(list)

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls) 
        return cls._instance
    
    def __init__(self):
        pass
    
    def add_dish(self, dish):
        if dish in self._dishes[dish.type_info()]:
            LogManager.log_message(f"{dish.get_name()} already in menu\n")
            return 

        self._dishes[dish.type_info()].append(dish)
        LogManager.log_message(f"{dish.get_name()} was added into menu\n")
    
    def show_menu(self): 
        LogManager.log_message("starting drawing menu...\n")
        LogManager.log_message("ending drawing menu\n")
    
    def items(self):
        return self._dishes
    

def upload_menu(dbparams):
    menu = Menu()
    with psycopg2.connect(**dbparams) as conn:
        with conn.cursor() as cur:
            # Загрузка супов
            cur.execute('''
                SELECT dish.name, dish.description, dish.price, soup.mass_g 
                FROM dish
                JOIN soup ON dish.id = soup.id
                JOIN menu ON menu.dish_id = soup.id;
            ''')
            for name, description, price, mass_g in cur.fetchall():
                menu.add_dish(DishFactory.get_dish("Soup", name, description, price, mass_g))

            # Загрузка напитков
            cur.execute('''
                SELECT dish.name, dish.description, dish.price, beverage.volume_ml 
                FROM dish
                JOIN beverage ON dish.id = beverage.id
                JOIN menu ON menu.dish_id = beverage.id;
            ''')
            for name, description, price, volume_ml in cur.fetchall():
                menu.add_dish(DishFactory.get_dish("Beverages", name, description, price, volume_ml))

            # Загрузка закусок
            cur.execute('''
                SELECT dish.name, dish.description, dish.price, snack.mass_g 
                FROM dish
                JOIN snack ON dish.id = snack.id
                JOIN menu ON menu.dish_id = snack.id;
            ''')
            for name, description, price, mass_g in cur.fetchall():
                menu.add_dish(DishFactory.get_dish("Snacks", name, description, price, mass_g))

            #Загрузка главных блюд
            cur.execute('''
                SELECT dish.name, dish.description, dish.price, main_dish.mass_g
                FROM dish
                JOIN main_dish on dish.id = main_dish.id
                JOIN menu ON menu.dish_id = main_dish.id;
            ''')
            for name, description, price, mass_g in cur.fetchall():
                menu.add_dish(DishFactory.get_dish('Main Dishes', name, description, price, mass_g))
            
            # Загрузка гарниров
            cur.execute('''
                SELECT dish.name, dish.description, dish.price, garnish.mass_g, garnish.sauce 
                FROM dish
                JOIN garnish ON dish.id = garnish.id
                JOIN menu ON menu.dish_id = garnish.id;
            ''')
            for name, description, price, mass_g, sauce in cur.fetchall():
                menu.add_dish(DishFactory.get_dish("Garnishes", name, description, price, mass_g, sauce))

            # Загрузка стейков
            cur.execute('''
                SELECT dish.name, dish.description, dish.price, steak.mass_g, steak.doneness 
                FROM dish
                JOIN steak ON dish.id = steak.id
                JOIN menu ON menu.dish_id = steak.id;
            ''')
            for name, description, price, mass_g, doneness in cur.fetchall():
                menu.add_dish(DishFactory.get_dish("Steaks", name, description, price, mass_g, doneness))

            
    