from utils.logger import LogManager
from utils.drawer import Drawer


class Menu:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._dishes = []
    
    def add_dish(self, dish):
        for d in self._dishes:
            if d.info() == dish.info():
                LogManager.log_message(f"{dish.get_name()} already in menu")
                return 

        self._dishes.append(dish)
        LogManager.log_message(f"{dish.get_name()} was added into menu")
    
    def show_menu(self): 
        LogManager.log_message("starting drawing menu...")
        Drawer(self._dishes).draw()
        LogManager.log_message("ending drawing menu")