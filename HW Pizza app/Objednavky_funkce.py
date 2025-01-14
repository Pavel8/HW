import pickle
import os
from Order_Sales import Order

ORDER_DATABASE_FILE = 'order_database.pkl'

def save_order():
    # Pokud soubor s databází objednávek existuje, načteme stávající objednávky
    if os.path.exists(ORDER_DATABASE_FILE):
        with open(ORDER_DATABASE_FILE, 'rb') as file:
            orders = pickle.load(file)
    else:
        orders = []

    # Přidáme novou objednávku do seznamu
    orders.append(Order)

    # Uložíme aktualizovaný seznam objednávek zpět do souboru
    with open(ORDER_DATABASE_FILE, 'wb') as file:
        pickle.dump(orders, file)

    print("Objednávka byla úspěšně uložena do databáze.")


def load_orders():
    if os.path.exists(ORDER_DATABASE_FILE):
        with open(ORDER_DATABASE_FILE, 'rb') as file:
            orders = pickle.load(file)
        return orders
    else:
        print("Databáze objednávek neexistuje.")
        return []
