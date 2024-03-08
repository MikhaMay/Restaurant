import psycopg2
from utils.logger import LogManager


soup_details = [
    ('Tomato Soup', 'Rich and creamy tomato soup', 200, 300),
    ('Chicken Soup', 'Classic chicken soup with noodles', 150, 250),
    ('Mushroom Soup', 'Creamy mushroom soup with herbs', 200, 350)
]

beverage_details = [
    ('Coca-Cola', 'Classic Coca-Cola.', 200, 330),
    ('Green Tea', 'Refreshing green tea.', 70, 200),
    ('Espresso', 'Strong espresso coffee.', 120, 50),
    ('Orange Juice', 'Fresh orange juice.', 100, 250),
    ('Mineral Water', 'Sparkling mineral water.', 80, 500)
]

snack_details = [
    ('Chips', 'Salty potato chips.', 100, 100),
    ('Nuts Mix', 'Mixed nuts.', 200, 150),
    ('Cheese Sticks', 'Crispy cheese sticks.', 150, 120),
    ('Bruschetta', 'Tomato and basil bruschetta.', 200, 200)
]

main_dish_details = [
    ('Veggie Pizza', 'Vegetarian pizza with mozzarella.', 450, 450),
    ('Burger', 'Beef burger with fries.', 350, 350),
    ('Chicken Parmesan', 'Breaded chicken breast topped with marinara sauce and mozzarella cheese.', 500, 300),
    ('Seafood Paella', 'Traditional Spanish rice dish with shrimp, mussels, and clams.', 550, 350),
    ('Vegetable Stir Fry', 'Mixed vegetables stir-fried with soy sauce and sesame seeds.', 400, 250),
    ('Duck Confit', 'Slow-cooked duck leg with crispy skin.', 350, 280),
    ('Lamb Curry', 'Spicy lamb curry with potatoes and peas.', 300, 320),
    ('Mushroom Risotto', 'Creamy risotto with wild mushrooms and Parmesan cheese.', 400, 300),
    ('Pulled Pork Sandwich', 'Slow-cooked pulled pork with BBQ sauce on a brioche bun.',  300, 200),
    ('Salmon Tartare', 'Fresh salmon tartare with avocado and lime.', 300, 220),
    ('Eggplant Parmigiana', 'Layers of eggplant with tomato sauce, mozzarella, and Parmesan cheese.', 300, 260),
    ('Beef Tacos', 'Three tacos with marinated beef, salsa, and cheese.', 250, 180)
]

garnier_details = [
    ('Mashed Potatoes', 'Creamy mashed potatoes.', 150, 200, 'Butter'),
    ('Rice Pilaf', 'Rice pilaf with carrots.', 150, 250, 'Curry'),
    ('Grilled Vegetables', 'Assorted grilled vegetables.', 200, 300, 'Herb'),
    ('French Fries', 'Crispy french fries.', 150, 150, 'Ketchup'),
    ('Caesar Salad', 'Caesar salad with croutons.', 200, 180, 'Caesar')
]

steak_details = [
    ('T-Bone Steak', 'Grilled T-bone steak.', 500, 350, 'Medium'),
    ('Filet Mignon', 'Tender filet mignon.', 500, 200, 'Rare'),
    ('New York Strip', 'Juicy New York strip steak.', 500, 300, 'Well-done'),
    ('Porterhouse', 'Large porterhouse steak.', 600, 400, 'Medium rare'),
    ('Ribeye', 'Boneless ribeye steak.', 600, 350, 'Medium well')
]



def insert_into(cur, details, table):
    LogManager.log_message(f'Starting inserts into {table}\n')
    for concrete_details in details:
        LogManager.log_message(f'table = {table}, concrete_details = {concrete_details}\n')
        cur.execute( f"""
        INSERT INTO dishes (name, text, price)
        VALUES (%s, %s, %s) RETURNING id;
        """, (concrete_details[0], concrete_details[1], concrete_details[2]))

        dish_id = cur.fetchone()[0]  # Получаем id
        
        # Формируем запрос для вставки в конкретную таблицу
        if table == 'soup' or table == 'snacks' or table == 'main_dishes':
            cur.execute(f"""
            INSERT INTO {table} (id, mass)
            VALUES (%s, %s);
            """, (dish_id, concrete_details[3]))
        elif table == 'beverages':
            cur.execute(f"""
            INSERT INTO {table} (id, volume)
            VALUES (%s, %s);
            """, (dish_id, concrete_details[3]))
        elif table == 'garniers':
            cur.execute(f"""
            INSERT INTO {table} (id, mass, sauce)
            VALUES (%s, %s, %s);
            """, (dish_id, concrete_details[3], concrete_details[4]))
        elif table == 'steakes':
            cur.execute(f"""
            INSERT INTO {table} (id, mass, doneness_level)
            VALUES (%s, %s, %s);
            """, (dish_id, concrete_details[3], concrete_details[4]))
        LogManager.log_message(f'Inserted into {table}: {concrete_details[0]} \n')

def insert_data():
    try:
        with psycopg2.connect(dbname="restaurant", user="postgres", password="test123", host="localhost") as conn:
            with conn.cursor() as cur:

                insert_into(cur, soup_details, 'soup')
                insert_into(cur, beverage_details, 'beverages')
                insert_into(cur, snack_details, 'snacks')
                insert_into(cur, main_dish_details, 'main_dishes')
                insert_into(cur, garnier_details, 'garniers')
                insert_into(cur, steak_details, 'steakes')

                conn.commit()  # Фиксация транзакции

                LogManager.log_message('All data inserted successfully \n')


    except Exception as e:
        LogManager.log_message(f'Error with database operations: {e} \n')
        raise 

