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

garnish_details = [
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



def insert_dish_details(cur, details, table):
    LogManager.log_message(f'Starting to insert into {table}\n')
    for concrete_datails in details:
        # Вставка в таблицу dish
        cur.execute("""
            INSERT INTO dish (name, description, price)
            VALUES (%s, %s, %s) RETURNING id;
            """, (concrete_datails[0], concrete_datails[1], concrete_datails[2]))
        dish_id = cur.fetchone()[0]
        
        # Вставка в специфичные таблицы блюд
        if table in ['soup', 'snack', 'main_dish']:
            cur.execute(f"""
                INSERT INTO {table} (id, mass_g)
                VALUES (%s, %s);
                """, (dish_id, concrete_datails[3])) 
        elif table == 'garnish':
            cur.execute(f"""
                INSERT INTO {table} (id, mass_g, sauce)
                VALUES (%s, %s, %s);
                """, (dish_id, concrete_datails[3], concrete_datails[4])) 
        elif table == 'steak':
            cur.execute(f"""
                INSERT INTO {table} (id, mass_g, doneness)
                VALUES (%s, %s, %s);
                """, (dish_id, concrete_datails[3], concrete_datails[4])) 
        elif table == 'beverage':
            cur.execute("""
                INSERT INTO beverage (id, volume_ml)
                VALUES (%s, %s);
                """, (dish_id, concrete_datails[3]))
            
        LogManager.log_message(f'Inserted into {table}: {concrete_datails[0]}\n')

# Главная функция для запуска процесса заполнения
def fill_tables(dbparams):
    try:
        conn = psycopg2.connect(**dbparams)
        cur = conn.cursor()
        
        insert_dish_details(cur, soup_details, 'soup')
        insert_dish_details(cur, beverage_details, 'beverage')
        insert_dish_details(cur, snack_details, 'snack')
        insert_dish_details(cur, main_dish_details, 'main_dish')
        insert_dish_details(cur, garnish_details, 'garnish')
        insert_dish_details(cur, steak_details, 'steak')
        
        conn.commit()
        LogManager.log_message('All dishes have been inserted successfully.\n')
        
    except Exception as e:
        LogManager.log_message(f'Error while inserting dishes: {e}\n')
        raise
    finally:
        if conn is not None:
            conn.close()

