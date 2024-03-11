import psycopg2
from utils.logger import LogManager

def fill_menu_table(dbparams):
    try:
        with psycopg2.connect(**dbparams) as conn:
            with conn.cursor() as cur:

                cur.execute('SELECT id FROM dish;')

                dishes_id = cur.fetchall()

                for i in dishes_id:
                    cur.execute('''INSERT INTO menu (dish_id) VALUES (%s);''', i)
                    conn.commit()
                    LogManager.log_message(f'into menu was added dish with id = {i}\n')



    except Exception as e:
        LogManager.log_message(f'Error with database operations: {e} \n')
        raise 



