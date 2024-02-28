class Drawer:
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance 

    def __init__(self, data):
        self._data = data

    def draw(self):
        for c in self._data:
            print(c, sep='\n')