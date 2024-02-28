from utils.logger import FileLogger, LogManager
from services.menu_service import Menu
from services.order_service import Order
from models.dish import Soup, Beverage
import sys
from gui.menu_viewer import MenuApp
from PyQt5.QtWidgets import QApplication



LogManager().set_logger(FileLogger('log_file.txt'))

LogManager.log_message('_'*10 + 'start' + '_'*10 + '\n')
menu = Menu()
soup1 = Soup('borsch', 'its nice soup', 65, 250)
soup2 = Soup('Solyanka', 'with meat', 75, 250)
bev1 = Beverage('Hot water', 'from the culer', 0, 200)
bev2 = Beverage('Coffee', 'from Vanya', 0, 200)
bev3 = Beverage('Cola', 'The Machine guns favorite drink', 95, 500)
soup3 = Soup('Solyanka', 'with meat', 75, 250)
bev4 = Beverage('Cumpot', 'for overprice', 25, 250)
soup4 = Beverage('Doshirak', 'from Ashan', 30, 150)
soup5 = Beverage('Lapsha with chiken', 'nraitsa', 65, 250)

dishes_names = {}
for d in soup1, soup2, soup3, soup4, soup5, bev1, bev2, bev3, bev4:
    dishes_names[d.get_name()] = d
    menu.add_dish(d)

# menu.show_menu()

# order1 = Order()

# user_wants = {soup1:2, soup2:1, bev3:2}

# for u_d, u_count in user_wants.items():
#     order1.add_dish(u_d, u_count)

# user_not_wants = {soup1:1, soup2:1, bev3:5, bev2:1}

# for u_d, u_count in user_not_wants.items():
#     order1.remove_dish(u_d, u_count)

# # order1.show_order()

# order2 = Order()
# order2.show_order()
# order2.add_dish(soup1, 2)
# order2.add_dish(soup2, 2)
# order2.add_dish(soup3, 2)
# order2.show_order()

print(menu.items())

if __name__ == '__main__':
    app = QApplication(sys.argv)  # Создаем экземпляр приложения

    ex = MenuApp(menu.items())  # Создаем экземпляр окна приложения, передавая список блюд

    sys.exit(app.exec_())  # Запускаем цикл обработки событий приложения
