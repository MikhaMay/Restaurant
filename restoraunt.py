from abc import ABC, abstractmethod

class Dish(ABC):
    def __init__(self, name, text, price):
        self._name = name
        self._price = price
        self._text = text
    
    @abstractmethod
    def info(self):
        return [self._name, self._text, self._price]
    
    def __hash__(self):     
        return hash(tuple(self.info()))
    
    def get_price(self):
        return self._price
    
    def get_name(self):
        return self._name
    
class Soup(Dish):
    def __init__(self, name, text, price, mass):
        super().__init__(name, text, price)
        self._mass = mass
    
    def info(self):
        return super().info() + [self._mass]

class Beverage(Dish):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self._volume = volume
    
    def info(self):
        return super().info() + [self._volume]
    
class Order:
    def __init__(self):
        self._dishes = {}
        self._summ = 0
    
    def add_dish(self, dish, count):
        self._dishes[dish] = self._dishes.get(dish, 0) + count
        self._summ += dish.get_price * count
    
    def remove_dish(self, dish, count):
        self._summ -= self._dishes[dish] * dish.get_price()
        self._dishes[dish] = max(self._dishes.get(dish, 0) - count, 0)
        self._summ += self._dishes[dish] * dish.get_price()

        if self._dishes[dish] == 0:
            del self._dishes[dish]
    
    def sum_cost(self):
        return self._summ
        
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
                return 

        self._dishes.append(dish)
    
    def show_menu(self): #или лучше в рисователя передавать меню и рисовать
        Drawer(self._dishes).draw()

class Drawer:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance 

    def __init__(self, data):
        self._data = data

    def draw(self):
        pass

class Logger(ABC):
    @abstractmethod
    def log(self, string):
        pass
    
class ConsoleLogger(Logger):
    def log(self, string):
        print(string)

class FileLogger(Logger):
    def __init__(self, filename = 'output.txt'):
        self._filename = filename

    def log(self, string):
        with open(self._filename, 'w') as f:
            f.write(string)

class LogManager:
    _instance = None
    _logger = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def set_logger(self, new_logger):
        self._logger = new_logger
    
    def log(self, string):
        if not self._logger:
            return
        self._logger.log(string)