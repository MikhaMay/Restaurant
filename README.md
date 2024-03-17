## Описание проекта
Этот проект — тренировочная программа, имитирующая часть функционала терминала в ресторане. Изначально созданный для отработки принципов объектно-ориентированного программирования и практики использования популярных паттернов проектирования, таких как Фабрика, Стратегия и Одиночка, проект был расширен за счёт интеграции с базой данных для хранения информации о блюдах.

Программа находится в стадии разработки и предназначена в основном для демонстрации навыков программирования.

## Структура проекта
Проект организован в несколько основных модулей, каждый из которых выполняет свою специфическую роль:

db/ - Модуль, отвечающий за работу с базой данных. Содержит все необходимые скрипты для создания, инициализации и управления базой данных проекта.

gui/ - Содержит графический интерфейс приложения, разработанный с использованием библиотеки PyQt5.

models/ - Модуль с классами, представляющими модели блюд. Определяет структуру данных блюд, используемых в приложении.

services/ - В этом модуле находятся классы, относящиеся к меню и заказам. Реализует логику взаимодействия с корзиной.

utils/ - Модуль содержит класс логера, позволяющего отслеживать выполнение программы.

## Начало работы

# Предварительные требования
Для запуска проекта убедитесь, что на вашем компьютере установлены:

Сервер PostgreSQL
Библиотека psycopg2
Библиотека PyQt5

# Установка и настройка

Клонируйте репозиторий с GitHub или скачайте исходный код в удобную для вас директорию.

Установите необходимые зависимости.

Настройте параметры подключения к базе данных в файле dbparams. Вам потребуется указать имя пользователя и пароль.

Запустите функции create_db_and_initialize_tables, fill_tables, fill_menu_table для создания и инициализации базы данных.

## Использование

После настройки и запуска программы откроется графический интерфейс меню ресторана, где пользователь может:

Перемещаться по категориям ресторана.

Добавлять выбранные блюда в корзину.

Редактировать содержимое корзины.

Следует отметить, что на графический интерфейс программы было уделено ограниченное внимание, так как основной акцент сделан на демонстрацию программных навыков.

