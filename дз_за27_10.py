import json
import sqlite3

path = "catalog.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)
#создаем список с категорией и ее определением
categories = []
for i in data:
    name = i["category"]["name"]
    categories.append((name, i["category"]["description"]))
categories = list(set(categories))#добавляем номер
category = [(i + 1, n, d) for i, (n, d) in enumerate(categories)]

#список продуктов, их цена и номер категории
products = []
for i in data:
    idc = 0
    for n, name, d in category:
        if name == i["category"]["name"]:
            idc = n
            break
    products.append([
        i["product_name"],
        i["price"],
        idc])                  

#создание таблиц и их заполнение созданными списками с помощью executemany
def create_tbl():
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("""CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT)""")
    cursor.executemany("INSERT INTO categories (id, name, description) VALUES (?, ?, ?)", category)
    conn.commit()
    conn.close()


def create_tb2():
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("""CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        product_name TEXT,
        price REAL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id))""")
    cursor.executemany("INSERT INTO products (product_name, price, category_id) VALUES (?, ?, ?)", products)
    conn.commit()
    conn.close()


create_tbl()
create_tb2()
