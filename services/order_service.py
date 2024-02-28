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

    
    def add_dish(self, dish, count=1):
        self._dishes[dish] = self._dishes.get(dish, 0) + count
        self._summ += dish.get_price() * count
        LogManager.log_message(f'into order {self.id} was added {count} {dish.get_name()} and order summ is {self._summ}\n')
    
    def remove_dish(self, dish, count):
        tmp = self._dishes.get(dish, 0)

        if tmp <= count:
            self._summ -= tmp * dish.get_price()
            if tmp < count:
                LogManager.log_message(f'In order {self.id} was only {tmp} {dish.get_name()}\n')
            LogManager.log_message(f'All {dish.get_name()} was removed! New order summ is {self._summ}\n')

            if dish in self._dishes:
                del self._dishes[dish]
        else:
            self._summ -= count * dish.get_price()
            LogManager.log_message(f'In order now {tmp-count} {dish.get_name()}, new order summ is {self._summ}\n')       

    def get_total_cost(self):
        return self._summ
    
    def show_order(self): 
        LogManager.log_message(f"starting drawing order {self.id}...\n")
        Drawer([(d.get_name(), count) for d, count in self._dishes.items()]).draw()
        LogManager.log_message(f"ending drawing order {self.id}\n")