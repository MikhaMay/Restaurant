import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout, QHBoxLayout

class MenuApp(QWidget):
    def __init__(self, menu_items):
        super().__init__()
        self.menu_items = menu_items  # Словарь типов блюд
        self.current_type = None
        self.current_page = 0
        self.items_per_page = 5
        self.order_cost = 0  # Стоимость заказа
        self.initUI()

    def initUI(self):
        self.mainLayout = QHBoxLayout()  # Основной горизонтальный лейаут
        self.typeLayout = QVBoxLayout()  # Лейаут для кнопок типов блюд
        self.menuLayout = QVBoxLayout()  # Лейаут для отображения меню и кнопок навигации

        # Создаем кнопки для типов блюд
        for dish_type in self.menu_items.keys():
            btn = QPushButton(dish_type.capitalize())
            btn.clicked.connect(lambda checked, t=dish_type: self.showDishesOfType(t))
            self.typeLayout.addWidget(btn)

        self.grid = QGridLayout()
        self.menuLayout.addLayout(self.grid)
        
        # Кнопки для навигации по страницам
        self.prevPageButton = QPushButton('Предыдущая страница')
        self.nextPageButton = QPushButton('Следующая страница')
        self.prevPageButton.clicked.connect(self.prevPage)
        self.nextPageButton.clicked.connect(self.nextPage)
        self.navLayout = QHBoxLayout()
        self.navLayout.addWidget(self.prevPageButton)
        self.navLayout.addWidget(self.nextPageButton)
        self.menuLayout.addLayout(self.navLayout)

        self.orderButton = QPushButton('Перейти к заказу')
        self.costLabel = QLabel('Стоимость заказа: 0')
        self.menuLayout.addWidget(self.orderButton)
        self.menuLayout.addWidget(self.costLabel)

        self.mainLayout.addLayout(self.typeLayout)
        self.mainLayout.addLayout(self.menuLayout)

        self.setLayout(self.mainLayout)
        self.setWindowTitle('Меню ресторана')
        self.resize(800, 500)
        self.show()

    def showDishesOfType(self, dish_type):
        self.current_type = dish_type
        self.current_page = 0
        self.updateMenu()

    def updateMenu(self):
        # Очистка текущих элементов меню
        for i in reversed(range(self.grid.count())): 
            self.grid.itemAt(i).widget().setParent(None)
        
        if self.current_type not in self.menu_items:
            return

        dishes = self.menu_items[self.current_type]
        start = self.current_page * self.items_per_page
        end = min(start + self.items_per_page, len(dishes))

        for i, dish in enumerate(dishes[start:end], start=1):
            label = QLabel(str(dish))
            addButton = QPushButton('Добавить в заказ')
            # Здесь будет подключена логика добавления в заказ
            addButton.clicked.connect(lambda checked, d=dish: self.addToOrder(d))
            self.grid.addWidget(label, i, 0)
            self.grid.addWidget(addButton, i, 1)

    def nextPage(self):
        if (self.current_page + 1) * self.items_per_page < len(self.menu_items[self.current_type]):
            self.current_page += 1
            self.updateMenu()

    def prevPage(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.updateMenu()

    def addToOrder(self, dish):
        # Здесь будет реализована логика добавления блюда в заказ
        print(f"Добавлено в заказ: {dish.info()[0]}")
        # Обновление стоимости заказа и т.д.
        # self.order_cost += ...
        # self.costLabel.setText(f'Стоимость заказа: {self.order_cost}')


