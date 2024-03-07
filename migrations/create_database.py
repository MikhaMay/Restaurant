import psycopg2
from utils.logger import LogManager

# SQL для создания таблиц
create_tables_sql = """
CREATE TABLE dishes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    text TEXT,
    price NUMERIC(10, 2) NOT NULL
);

CREATE TABLE beverages (
    id INTEGER PRIMARY KEY REFERENCES dishes(id),
    volume INTEGER
);

CREATE TABLE soup (
    id INTEGER PRIMARY KEY REFERENCES dishes(id),
    mass INTEGER
);

CREATE TABLE main_dishes (
    id INTEGER PRIMARY KEY REFERENCES dishes(id),
    mass INTEGER
);

CREATE TABLE snacks (
    id INTEGER PRIMARY KEY REFERENCES dishes(id),
    mass INTEGER
);

CREATE TABLE garniers (
    id INTEGER PRIMARY KEY REFERENCES dishes(id),
    mass INTEGER,
    sauce VARCHAR(50)
);

CREATE TABLE steaks (
    id INTEGER PRIMARY KEY REFERENCES dishes(id),
    mass INTEGER,
    doneness_level VARCHAR(50)
);

CREATE TABLE menu (
    dish_id INTEGER PRIMARY KEY REFERENCES dishes(id)
);

CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    contact_info TEXT
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES client(id),
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    order_id INTEGER REFERENCES orders(id),
    dish_id INTEGER REFERENCES dishes(id),
    quantity INTEGER NOT NULL,
    PRIMARY KEY (order_id, dish_id)
);
"""

def create_db_and_tables():
    # Инициализация соединения
    try:
        conn = psycopg2.connect(dbname='postgres', user='postgres', password='test123', host='localhost')
        cur = conn.cursor()
        conn.autocommit = True

        # Создание базы данных
        try:
            cur.execute("CREATE DATABASE restaurant;")
            LogManager.log_message("Database created successfully\n")
        except psycopg2.errors.DuplicateDatabase:
            LogManager.log_message("Database already exists\n")
        finally:
            # Подключение к новой базе данных для создания таблиц
            conn.close()


        # Подключение к созданной базе данных
        conn = psycopg2.connect(dbname='restaurant', user='postgres', password='test123', host='localhost')
        cur = conn.cursor()

        
        cur.execute(create_tables_sql)
        LogManager.log_message("Tables created successfully\n")
        conn.commit()
    
    except Exception as e:
        LogManager.log_message(f"Error during database setup: {e}\n")
        raise  # Проброс исключения выше

    finally:
        if conn is not None:
            conn.close()


