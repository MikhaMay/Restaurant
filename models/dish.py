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
    
    def __str__(self):
        return '\n'.join(str(i) for i in self.info())
    
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
    def __init__(self, name, text, price, volume):
        super().__init__(name, text, price)
        self._volume = volume
    
    def info(self):
        return super().info() + [self._volume]

