from utils.logger import LogManager

class Order:
    def __init__(self):
        LogManager.log(f'order {self} was created\n')
        self._dishes = {}
        self._summ = 0
    
    def add_dish(self, dish, count):
        self._dishes[dish] = self._dishes.get(dish, 0) + count
        self._summ += dish.get_price() * count
        LogManager.log_message(f'into order {self} was added {count} {dish.get_name()} and order summ is {self._summ}\n')
    
    def remove_dish(self, dish, count):
        tmp = self._dishes.get(dish, 0)

        if tmp <= count:
            self._summ -= tmp * dish.get_price()
            if tmp < count:
                LogManager.log_message(f'In order {self} was only {tmp} {dish.get_name()}\n')
            LogManager.log_message(f'All {dish.get_name()} was removed! New order summ is {self._summ}\n')

            if dish in self._dishes:
                del self._dishes[dish]
        else:
            self._summ -= count * dish.get_price()
            LogManager.log_message(f'In order now {tmp-count} {dish.get_name()}, new order summ is {self._summ}\n')       

    def get_total_cost(self):
        return self._summ