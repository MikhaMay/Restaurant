from utils.logger import FileLogger, LogManager
from services.menu_service import Menu
from services.order_service import Order
from models.dish import Soup, Beverage



LogManager().set_logger(FileLogger('log_file.txt'))

LogManager.log_message('_'*10 + 'start' + '_'*10 + '\n')
menu1 = Menu()
soup1 = Soup('borsch', 'its nice soup', 65, 250)
soup2 = Soup('Solyanka', 'with meat', 75, 250)
bev1 = Beverage('Hot water', 'from the culer', 0, 200)
bev2 = Beverage('Coffee', 'from Vanya or Nikita', 0, 200)
bev3 = Beverage('Cola', 'The Machine guns favorite drink', 95, 500)
soup3 = Soup('Solyanka', 'with meat', 75, 250)

dishes_names = {}
for d in soup1, soup2, bev1, bev2, bev3, soup3:
    dishes_names[d.get_name()] = d
    menu1.add_dish(d)

menu1.show_menu()

order1 = Order()

user_wants = {soup1:2, soup2:1, bev3:2}

for u_d, u_count in user_wants.items():
    order1.add_dish(u_d, u_count)

user_not_wants = {soup1:1, soup2:1, bev3:5, bev2:1}

for u_d, u_count in user_not_wants.items():
    order1.remove_dish(u_d, u_count)

# order1.show_order()

order2 = Order()
order2.show_order()
order2.add_dish(soup1, 2)
order2.add_dish(soup2, 2)
order2.add_dish(soup3, 2)
order2.show_order()

print(hash(soup2) == hash(soup3))               #True
dish_dict = {soup2:3}
print((soup3 in dish_dict) == (soup2 in dish_dict)) #False

