from utils.logger import FileLogger, LogManager
from services.menu_service import Menu
from models.dish import Soup, Beverage



LogManager().set_logger(FileLogger('log_file.txt'))

LogManager.log_message('_'*10 + 'start' + '_'*10 + '\n')
menu1 = Menu()
soup1 = Soup('borsch', 'its nice soup', 65, 250)
menu1.add_dish(soup1)
menu1.show_menu()


