import sqlite3


def init_db(func):
    def wrapper(*args, **kwargs):
        result = []
        try:
            conn = sqlite3.connect('shop.db')
            cursor = conn.cursor()

            cursor.execute('''
                           CREATE TABLE IF NOT EXISTS products (
                               id INTEGER PRIMARY KEY,
                               name TEXT,
                               price REAL,
                               stock INTEGER
                            )
                        ''')
            result = func(*args, **kwargs)
        except sqlite3.Error as e:
            print(f"Помилка: {e}")
        finally:
            if conn:
                conn.close()
        
        return result
    return wrapper


@init_db
def add_product(product: tuple) -> None:
        try:
            conn = sqlite3.connect('shop.db')
            cursor = conn.cursor()
            
            cursor.execute('INSERT INTO products VALUES(?, ?, ?, ?)', product)
            conn.commit()
            print("Товар додано")
        except sqlite3.Error as e:
            print(f"Помилка: {e}")
        finally:
            if conn:
                conn.close()


@init_db
def list_products() -> list:
    try:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM products')
        products: list = cursor.fetchall()
        conn.commit()
    except sqlite3.Error as e:
      print(f"Помилка: {e}")
    finally:
        if conn:
            conn.close()
        return products


@init_db
def update_price(id: int, price: float) -> None:
    try:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        cursor.execute('''UPDATE products 
                          SET price = ?
                          WHERE id = ?''', (price, id))
        conn.commit()
    except sqlite3.Error as e:
      print(f"Помилка: {e}")
    finally:
        if conn:
            conn.close()


@init_db
def delete_product_bad_stock(stock: int) -> None:
    try:
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM products WHERE  stock < ?', (stock, ))
        conn.commit()
        print("Товари видалено.")
    except sqlite3.Error as e:
      print(f"Помилка: {e}")
    finally:
        if conn:
            conn.close()


# if __name__ == "__main__":
    # print(list_products())
    # add_product((1, "ESP32", 300.0, 30))
    # add_product((2, "ESP8266", 50.0, 12))
    # add_product((3, "Граната свята Анітохійська", 99999.99, 3))
    # add_product((4, "Грааль святий", 1000, 1))
    # add_product((5, "Моє почуття гумору", 0.0, 0))
    # print(list_products())
    # update_price(1, 500.0)
    # print(list_products())
    # delete_product_bad_stock(5)
    # print(list_products())