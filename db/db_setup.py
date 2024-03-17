import psycopg2
from utils.logger import LogManager

create_tables_sql = """
CREATE TABLE dish (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL
);

CREATE TABLE beverage (
    id INTEGER PRIMARY KEY REFERENCES dish(id),
    volume_ml INTEGER
);

CREATE TABLE soup (
    id INTEGER PRIMARY KEY REFERENCES dish(id),
    mass_g INTEGER
);

CREATE TABLE main_dish (
    id INTEGER PRIMARY KEY REFERENCES dish(id),
    mass_g INTEGER
);

CREATE TABLE snack (
    id INTEGER PRIMARY KEY REFERENCES dish(id),
    mass_g INTEGER
);

CREATE TABLE garnish (
    id INTEGER PRIMARY KEY REFERENCES dish(id),
    mass_g INTEGER,
    sauce VARCHAR(50)
);

CREATE TABLE steak (
    id INTEGER PRIMARY KEY REFERENCES dish(id),
    mass_g INTEGER,
    doneness VARCHAR(50)
);

CREATE TABLE menu (
    dish_id INTEGER PRIMARY KEY REFERENCES dish(id)
);

CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    client_id INTEGER REFERENCES client(id),
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    order_id INTEGER REFERENCES orders(id),
    dish_id INTEGER REFERENCES dish(id),
    quantity INTEGER NOT NULL,
    PRIMARY KEY (order_id, dish_id)
);
"""

def create_db_and_initialize_tables(dbparams):
    try:
        dbname = dbparams['dbname']
        dbparams['dbname'] = 'postgres'

        conn = psycopg2.connect(**dbparams)
        conn.autocommit = True
        cur = conn.cursor()
        try:
            cur.execute(f"CREATE DATABASE {dbname};")
            LogManager.log_message("Database created successfully.\n")
        except psycopg2.errors.DuplicateDatabase:
            LogManager.log_message("Database already exists.\n")
        finally:
            cur.close()
            conn.close()

        dbparams['dbname'] = dbname

        with psycopg2.connect(**dbparams) as conn:
            with conn.cursor() as cur:
                cur.execute(create_tables_sql)
                LogManager.log_message("Tables created successfully.")
                conn.commit()
    
    except Exception as e:
        LogManager.log_message(f"Error during database setup: {e}")
        raise

