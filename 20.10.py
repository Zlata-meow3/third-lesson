import sqlite3
'''
try:
    cursor.execute('UPDATE accounts SET balance=balance-1000 WHERE id=1')
    cursor.execute('UPDATE accounts SET balance=balance+1000 WHERE id=2')
    conn.commit()
exept:
    conn.rollback()'''
'''
def create_db():
    conn=sqlite3.connect("accounts.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS people(id INTEGER PRIMARY KEY,name TEXT,balance INTEGER)")
    conn.commit()
    conn.close()

def insert_into():
    conn=sqlite3.connect("accounts.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO people(name,balance) VALUES ('Petya',2500)")
    conn.commit()
    conn.close()
#create_db()
#insert_into()
try:#изменение баланса
    conn=sqlite3.connect("accounts.db")
    cursor=conn.cursor()
    cursor.execute('UPDATE people SET balance=balance+1000 WHERE id=1')
    raise Exception("Power Failure")# выключение света==прерывание операции
    cursor.execute('UPDATE people SET balance=balance-1000 WHERE id=2')
    conn.commit()
    #conn.close()
except:
    conn.rollback()'''
#1.Согласованность=нет ячеек без имени, можно устанавливать ограничения на значения в таблице(не может = 0)
#2. Транзакции в одно время, нет промежуточных значений, можно сделать через timeout или через очереди(запись в буфер и работа из него)


#Красивый способ закрытия
'''
from contextlib import closing
with closing(sqlite3.connect("database.db")) as conn:
    with conn:#после выполнения автоматически создасться коммит и закрытие
        cursor=conn.cursor()
        cursor.execute("INSERT INTO..")'''


#Вспоминаем  метод fetchall с прошлого задания
'''
cursor.execute("SELECT id,name,email FROM users")#извлечение данных
rows=cursor.fetchall()#запись в массив
users=[]
for row in rows:#перебор и запись имени в users
    users.append(row[1])

#другой вариант работы с этим методом, обращение по имени столбца, а не по индексу
conn.row_factory=sqlite3.Row
cursor=conn.cursor()
cursor.execute("SELECT id,name,email FROM users")
for row in cursor.fetchall():
    print(row['name'],row['email'])

'''
# связь между двумя таблицами
# оператор join
#    SELECT "поле"
#    FROM "таблица1"
#    JOIN "таблица2" ON "условие"

#создание 1 таблицы
'''
def create_db():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS games(id INTEGER PRIMARY KEY,user_id INTEGER,score INTEGER)")
    conn.commit()
    conn.close()

def insert_into():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO games(user_id,score) VALUES (3,1000)")
    cursor.execute("INSERT INTO games(user_id,score) VALUES (3,2000)")
    cursor.execute("INSERT INTO games(user_id,score) VALUES (3,3000)")
    
    conn.commit()
    conn.close()
#create_db()
insert_into()'''
#создание 2 таблицы
'''
def create_db():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)")
    conn.commit()
    conn.close()

def insert_into():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO users(name,age) VALUES ('Kolya',20)")
    cursor.execute("INSERT INTO users(name,age) VALUES ('Petya',21)")
    cursor.execute("INSERT INTO users(name,age) VALUES ('Ivan',20)")
    cursor.execute("INSERT INTO users(name,age) VALUES ('Sergey',19)")
    conn.commit()
    conn.close()

create_db()
insert_into()'''
# Дальше работали в браузере, там ввели команду "SELECT games.id,name,users.id,age,score FROM games JOIN users ON games.user_id=users.id" и получили объединенную таблицу по заданным условиям
# Из команды SELECT games.id,name,users.id,age,score FROM games,users получили 16 строк, т.к. для каждого значения таблица объединялась заново
# функция JOIN=INNER JOIN т.е, только объединение двух множеств, во втором случае без JOIN у нас получился FULL JOIN
# Еще есть RIGHT и LEFT JOIN, где только правое или левое множество
# GROUP BY user_id - использовали чтобы суммирование проходило правильно и добавлялось только нужному участнику а не только одному(самому первому)-группировка по id
# ORDER BY - сортировка, если DESC - по убыванию, ASC - по возрастанию, по умолчанию сортировка по возрастанию














