import psycopg2
from utils.logger import LogManager

def insert_into_menu():
    try:
        with psycopg2.connect(dbname="restaurant", user="postgres", password="test123", host="localhost") as conn:
            with conn.cursor() as cur:

                cur.execute('SELECT id FROM dishes;')

                dishes_id = cur.fetchall()

                for i in dishes_id:
                    cur.execute('''INSERT INTO menu (dish_id) VALUES (%s);''', i)
                    conn.commit()
                    LogManager.log_message(f'into menu was added dish with id = {i}\n')



    except Exception as e:
        LogManager.log_message(f'Error with database operations: {e} \n')
        raise 



