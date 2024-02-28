from utils.drawer import Drawer
from utils.logger import LogManager


class Menu:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._dishes = []
    
    def add_dish(self, dish):
        if dish in self._dishes:
            LogManager.log_message(f"{dish.get_name()} already in menu\n")
            return 

        self._dishes.append(dish)
        LogManager.log_message(f"{dish.get_name()} was added into menu\n")
    
    def show_menu(self): 
        LogManager.log_message("starting drawing menu...\n")
        Drawer(self._dishes).draw()
        LogManager.log_message("ending drawing menu\n")
    
    def items(self):
        return self._dishes