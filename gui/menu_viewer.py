from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout, QHBoxLayout, QScrollArea, QWidget, QSizePolicy
from services.order_service import Order

class MenuApp(QWidget):
    def __init__(self, menu_items):
        super().__init__()
        self.menu_items = menu_items
        self.order = Order()
        self.isOrderView = False
        self.initUI()

    def initUI(self):
        self.mainLayout = QHBoxLayout()
        self.typeLayout = QVBoxLayout()
        self.menuLayout = QVBoxLayout()

        for dish_type in self.menu_items.keys():
            btn = QPushButton(dish_type)
            btn.clicked.connect(lambda checked, t=dish_type: self.showDishesOfType(t))
            self.typeLayout.addWidget(btn)

        self.menuContainer = QWidget()  # Контейнер для QScrollArea
        self.menuContainerLayout = QVBoxLayout()
        self.menuContainer.setLayout(self.menuContainerLayout)

        self.scrollArea = QScrollArea(self)  # ScrollArea для меню
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.menuContainer)

        self.orderButton = QPushButton('Перейти к заказу')
        self.orderButton.clicked.connect(self.toggleView)
        self.costLabel = QLabel('Стоимость заказа: 0')

        self.menuLayout.addWidget(self.scrollArea)
        self.menuLayout.addWidget(self.orderButton)
        self.menuLayout.addWidget(self.costLabel)

        self.mainLayout.addLayout(self.typeLayout)
        self.mainLayout.addLayout(self.menuLayout)

        self.showDishesOfType()

        self.setLayout(self.mainLayout)
        self.setWindowTitle('Меню ресторана')
        self.resize(800, 500)
        self.show()

    def toggleView(self):
        if self.isOrderView:
            self.backToMenu()
        else:
            self.showOrderView()

    def recreateScrollArea(self):
        #Удаляет и создает заново scrollArea и menuContainer.
        if hasattr(self, 'scrollArea'):  # Проверяем, существует ли scrollArea
            self.scrollArea.deleteLater()  # Удаляем существующий scrollArea
        self.menuContainer = QWidget()  # Создаем новый контейнер для элементов
        self.menuContainerLayout = QVBoxLayout(self.menuContainer)
        self.scrollArea = QScrollArea(self)  # Создаем новый scrollArea
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.menuContainer)
        self.menuLayout.insertWidget(0, self.scrollArea)  # Добавляем scrollArea на первое место в layout


    def showDishesOfType(self, dish_type=None):
        if dish_type == None:
            dish_type = list(self.menu_items.keys())[0]

        self.recreateScrollArea()  # Пересоздаем scrollArea и menuContainer

        dishes = self.menu_items[dish_type]
        for dish in dishes:
            label = QLabel(str(dish))
            addButton = QPushButton('Добавить в заказ')
            addButton.clicked.connect(lambda checked, d=dish: self.addToOrder(d))
            dishLayout = QHBoxLayout()
            dishLayout.addWidget(label)
            dishLayout.addWidget(addButton)
            self.menuContainerLayout.addLayout(dishLayout)

    def addToOrder(self, dish):
        # Логика добавления блюда в заказ
        self.order.add_dish(dish)
        self.costLabel.setText(f'Стоимость заказа: {self.order.get_total_cost()}')

    def setLayoutVisible(self, layout, visible):
        for i in range(layout.count()): 
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.setVisible(visible)

    def showOrderView(self):
        self.recreateScrollArea()  # Пересоздаем scrollArea и menuContainer
        for dish, count in self.order.items().items():
            dishLayout = QHBoxLayout()
            labeldish = QLabel(str(dish))
            labelcount = QLabel(str(count))
            addButton = QPushButton('+')
            removeButton = QPushButton('-')
            addButton.clicked.connect(lambda checked, d=dish: self.changeOrder(d, 1))
            removeButton.clicked.connect(lambda checked, d=dish: self.changeOrder(d, -1))
            dishLayout.addWidget(labeldish)
            dishLayout.addWidget(labelcount)
            dishLayout.addWidget(addButton)
            dishLayout.addWidget(removeButton)
            self.menuContainerLayout.addLayout(dishLayout)

        self.costLabel.setText(f'Стоимость заказа: {self.order.get_total_cost()}')
        
        self.orderButton.setText('Вернуться к меню')
        self.isOrderView = True

        # Скрываем кнопки разделов блюд
        self.setLayoutVisible(self.typeLayout, False)

    def changeOrder(self, dish, change):
        # Логика изменения количества блюда в заказе
        if change > 0:
            self.order.add_dish(dish)
        else:
            self.order.remove_dish(dish)
        self.showOrderView()

    def backToMenu(self):
        self.recreateScrollArea()
        self.showDishesOfType()

        # Обновляем текст и действие кнопки для перехода к заказу
        self.orderButton.setText('Перейти к заказу')
        self.isOrderView = False

        # Показываем кнопки разделов блюд
        self.setLayoutVisible(self.typeLayout, True)
