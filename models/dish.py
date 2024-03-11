from abc import ABC, abstractmethod

class Dish(ABC):
    def __init__(self, name, text, price):
        self._name = name
        self._text = text
        self._price = price
    
    @abstractmethod
    def info(self):
        return [self._name, self._text, self._price]
    
    @abstractmethod
    def type_info(self):
        pass
    
    def __hash__(self):     
        return hash(tuple(self.info()))
    
    def __str__(self):
        return '\n'.join(str(i) for i in self.info())
    
    def __eq__(self, other_dish):
        return self.info() == other_dish.info()
    
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
    
    def type_info(self):
        return 'Soup'
    
    def __str__(self):
        return f"{self._name}\n{self._text}\nweight: {self._mass}, price: {self._price}"
    
class Beverage(Dish):
    def __init__(self, name, text, price, volume):
        super().__init__(name, text, price)
        self._volume = volume
    
    def info(self):
        return super().info() + [self._volume]
    
    def type_info(self):
        return 'Beverages'
    
    def __str__(self):
        return f"{self._name}\n{self._text}\nvolume: {self._volume}, price: {self._price}"
    
class Snack(Dish):
    def __init__(self, name, text, price, mass):
        super().__init__(name, text, price)
        self._mass = mass
    
    def info(self):
        return super().info() + [self._mass]
    
    def type_info(self):
        return 'Snacks'

    def __str__(self):
        return f"{self._name}\n{self._text}\nweight: {self._mass}, price: {self._price}"

class MainDishe(Dish):
    def __init__(self, name, text, price, mass):
        super().__init__(name, text, price)
        self._mass = mass
    
    def info(self):
        return super().info() + [self._mass]
    
    def type_info(self):
        return 'Main Dishes'

    def __str__(self):
        return f"{self._name}\n{self._text}\nweight: {self._mass}, price: {self._price}"

class Garnier(MainDishe):
    def __init__(self, name, text, price, mass, sauce):
        super().__init__(name, text, price, mass)
        self._sauce = sauce
    
    def info(self):
        return super().info() + [self._sauce]
    
    def type_info(self):
        return 'Garnishes'
    
    def _str__(self):
        return f"{self._name}\n{self._text}\nsauce: {self._donenes_level}\nweight: {self._mass}, price: {self._price}"

class Steake(MainDishe):
    def __init__(self, name, text, price, mass, don_level):
        super().__init__(name, text, price, mass)
        self._donenes_level = don_level
    
    def info(self):
        return super().info() + [self._donenes_level]
    
    def type_info(self):
        return 'Steaks'

    def __str__(self):
        return f"{self._name}\n{self._text}\ndonenes level: {self._donenes_level}\nweight: {self._mass}, price: {self._price}"

class DishFactory:
    @staticmethod
    def get_dish(dish_type, *params):
        if dish_type == 'Soup':
            return Soup(*params)
        elif dish_type == 'Beverages':
            return Beverage(*params)
        elif dish_type == 'Snacks':
            return Snack(*params)
        elif dish_type == 'Main Dishes':
            return MainDishe(*params)
        elif dish_type == 'Garnishes':
            return Garnier(*params)
        elif dish_type == 'Steaks':
            return Steake(*params)
    
        
