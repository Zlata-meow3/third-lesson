import sqlite3
def create_db():
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()
    conn.close()

def insert_into():
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO customers(name) VALUES ('Ivan')")
    cursor.execute("INSERT INTO customers(name) VALUES ('Peter')")
    cursor.execute("INSERT INTO customers(name) VALUES ('Kolya')")
    cursor.execute("INSERT INTO customers(name) VALUES ('Serj')")
    
    conn.commit()
    conn.close()
#create_db()
#insert_into()

def create_db1():
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.execute("CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY,customer_id INTEGER,amount REAL, FOREIGN KEY(customer_id) REFERENCES customers(id))")
    conn.commit()
    conn.close()

def insert_into1():
    conn=sqlite3.connect("database.db")
    cursor=conn.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.execute("INSERT INTO orders(customer_id,amount) VALUES (3,100500)")
    cursor.execute("INSERT INTO orders(customer_id,amount) VALUES (1,100.5)")
    cursor.execute("INSERT INTO orders(customer_id,amount) VALUES (4,123)")
    cursor.execute("INSERT INTO orders(customer_id,amount) VALUES (2,246)")
    cursor.execute("INSERT INTO orders(customer_id,amount) VALUES (1,369.5)")
    conn.commit()
    conn.close()

#create_db1()
#insert_into1()
'''
conn=sqlite3.connect("database.db")
cursor=conn.cursor()
cursor.execute("INSERT INTO orders(customer_id,amount) VALUES (999,66.6)")
conn.commit()
conn.close()'''
# чтобы удалять значения из первой таблицы и не попадать в ошибку нужно было:
'''CREATE TABLE orders(id INTEGER PRIMARY KEY,customer_id INTEGER,FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE CASCADE)'''
# вместо cascade можно ставить: restrict,cascade,set null,set default,no action
# значения функций немного отличаются, но смысл похожий



# конец sql- начало ORM - object Relational Mapping
#SQLAlchmy,Django ORM, PeeWee,SQLModel, TortoiseORM - варианты ORM
'''cursor.execute(f"SELECT * FROM students WHERE name='{user_input}'")'''
#a) Petya - все ок
#b)Petya 'and drop table students' - таблица удалится, т.к нет фильтров
from sqlalchemy import create_engine, insert
from sqlalchemy import MetaData,Table,Column,Integer,String,Float,Boolean
engine=create_engine('sqlite:///database.db',echo=True)#найти созданный файл сложно, но можно добавить / и написать полный путь до папки
#engine.connect()
metadata=MetaData()
students_table=Table('students',metadata, Column('id',Integer,primary_key=True),Column('name',String(100),nullable=False),Column('group',String(20)),Column('gpa',Float,default=0.0),Column('is_active',Boolean,default=True))
metadata.create_all(engine)
with engine.connect() as connection:
    something=insert(students_table).values(
        name='Ivanov.I.I.',
        group='ИУ10-33',
        gpa=4.5)
    result=connection.execute(something)
    connection.commit()
    print(f"Добавлена строка с id={result.inserted_primary_key[0]}")

#способ задачи данных      
smt=insert(students_table)
data=[
    {'name'='Petrov','group'='IU1-10-33','gpa'=3.8},
    {'name'='',group='',gpa=4.0}]
result=connection.execute(smt,data)









