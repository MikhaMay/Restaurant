from utils.logger import LogManager
from utils.drawer import Drawer

class Order:
    _id_counter = 0  

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)  
        instance.id = cls._id_counter  
        cls._id_counter += 1  
        return instance  

    def __init__(self):
        LogManager.log_message(f'order {self.id} was created\n')
        self._dishes = {}
        self._summ = 0

    
    def add_dish(self, dish):
        self._dishes[dish] = self._dishes.get(dish, 0) + 1
        self._summ += dish.get_price()
        LogManager.log_message(f'into order {self.id} was added {dish.get_name()}. Order summ is {self._summ}\n')
    
    def remove_dish(self, dish):
        if dish not in self._dishes:
            LogManager.log_message(f'{dish.get_name()} not in order {self.id}! Order summ is {self._summ}\n')
        elif self._dishes[dish] == 0:
            LogManager.log_message(f'Count of {dish.get_name()} in order {self.id} is 0! Order summ is {self._summ}\n')
            del self._dishes[dish]
        elif self._dishes[dish] == 1:
            del self._dishes[dish]
            self._summ -= dish.get_price()
            LogManager.log_message(f'All {dish.get_name()} from order {self.id} was removed! New order summ is {self._summ}\n')
        else:
            self._dishes[dish] -= 1
            self._summ -= dish.get_price()
            LogManager.log_message(f'In order {self.id} now {self._dishes[dish]} {dish.get_name()}, new order summ is {self._summ}\n') 

    def get_total_cost(self):
        return self._summ
    
    def show_order(self): 
        LogManager.log_message(f"starting drawing order {self.id}...\n")
        Drawer([(d.get_name(), count) for d, count in self._dishes.items()]).draw()
        LogManager.log_message(f"ending drawing order {self.id}\n")

    def items(self):
        return self._dishes