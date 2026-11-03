#к предыдущему уроку
'''
from sqlachemy import select
with engine.connect() as connection:
    statement=select(students)
    result=connection.execute(statement)
    for rom in result:
        print(row.id,row.name,row.is_active)
    statement2=select(students.c.name,students.c.gpa)
    result2=connection.execute(statement2)
    for row in result2:
        print(row.name,row.gpa)
from sqlachemy import update,delete
with engine.connect() as connection:
    statement=(update(students_table).where(students_table.c.name=='Petrov P.P.')
               .values(gpa=4.6))
    result=connection.execute(statement)
    connection.commit()
    print(f"обновление строк: {result.rowcount}")
    statement2=(delete(students_table).where(students_table.c.gpa<3.5))
    result=connection.execute(statement2)
    connection.commit()'''
#  в sqlalchemy также реализованы все возможности для работы с таблицами

#выполняем дз только с помощью sqlalchemy 
import json
from sqlalchemy import create_engine, insert, text
from sqlalchemy import MetaData, Table, Column, Integer, String, Float, ForeignKey

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
#создаем таблицу
engine = create_engine("sqlite:///shop1.db", echo=True)#создание файла
metadata = MetaData()
#таблица с категориями
categories_table = Table(
    "categories", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("description", String(200)))
#таблица с продуктами
products_table = Table(
    "products", metadata,
    Column("id", Integer, primary_key=True),
    Column("product_name", String(200)),
    Column("price", Float),
    Column("category_id", Integer, ForeignKey("categories.id")))

metadata.create_all(engine)
with engine.connect() as connection:
    connection.execute(text("PRAGMA foreign_keys = ON"))
    #преобразуем данные для таблиц в нужный формат
    data_categories = [
        {"id": cid, "name": name, "description": desc}
        for cid, name, desc in category]
    result = connection.execute(insert(categories_table), data_categories)
    #заполняем таблицы с помощью insert
    data_products = [
        {"product_name": name, "price": price, "category_id": cid}
        for name, price, cid in products]
    result2 = connection.execute(insert(products_table), data_products)

    connection.commit()

    print(f"Добавлено категорий: {result.rowcount}")
    print(f"Добавлено товаров: {result2.rowcount}")
               
