from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout

class MenuApp(QWidget):
    def __init__(self, menu_items):
        super().__init__()
        self.menu_items = menu_items
        self.current_page = 0
        self.items_per_page = 5
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.grid = QGridLayout()
        self.updateMenu()
        
        self.nextButton = QPushButton('Следующая страница')
        self.prevButton = QPushButton('Предыдущая страница')
        
        self.nextButton.clicked.connect(self.nextPage)
        self.prevButton.clicked.connect(self.prevPage)
        
        self.layout.addLayout(self.grid)
        self.layout.addWidget(self.prevButton)
        self.layout.addWidget(self.nextButton)
        
        self.setLayout(self.layout)
        self.setWindowTitle('Меню ресторана')
        self.resize(700, 500)
        self.show()

    def updateMenu(self):
        for i in range(self.grid.count()): 
            self.grid.itemAt(i).widget().deleteLater()
        
        start = self.current_page * self.items_per_page
        end = start + self.items_per_page
        for i, item in enumerate(self.menu_items[start:end], start=1):
            label = QLabel(str(item))
            self.grid.addWidget(label, i, 0)

    def nextPage(self):
        if (self.current_page + 1) * self.items_per_page < len(self.menu_items):
            self.current_page += 1
            self.updateMenu()

    def prevPage(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.updateMenu()