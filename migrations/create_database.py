import psycopg2


conn = psycopg2.connect(dbname = 'postgres',  user = 'postgres', password = 'test123', host = 'localhost')
conn.autocommit = True
cur = conn.cursor()

# Создание базы данных
try:
    cur.execute("CREATE DATABASE restaurant;")
    print("Database created successfully")
except psycopg2.errors.DuplicateDatabase:
    print("Database already exists")

# Подключение к новой базе данных для создания таблиц
conn.close()


conn = psycopg2.connect(dbname = 'restaurant',  user = 'postgres', password = 'test123', host = 'localhost')
conn.autocommit = True
cur = conn.cursor()

# SQL для создания таблиц
create_tables_sql = """
CREATE TABLE dishes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    text TEXT,
    price NUMERIC NOT NULL
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
    sauce VARCHAR(20)
);

CREATE TABLE steaks (
    id INTEGER PRIMARY KEY REFERENCES dishes(id),
    mass INTEGER,
    don_level VARCHAR(10)
);

CREATE TABLE menu (
    dish_id INTEGER PRIMARY KEY REFERENCES dishes(id)
);

CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
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

cur.execute(create_tables_sql)

print("Tables created successfully")

conn.close()

