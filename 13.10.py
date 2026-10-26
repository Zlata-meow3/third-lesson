'''
import json
#открываем файл с пользователями для чтения
with open('users.json', 'r', encoding='utf-8') as f:
    users = json.load(f)

#создаем файл с 10000 этими значениями
with open('people.json', 'w', encoding='utf-8') as f:
    for i in range(100000):
        json.dump(users, f, ensure_ascii=False, indent=2)'''


#это SQL команда для создания таблицы
# основные коматды: CREAT,LEAD,UPDATE,DELETE

'''
|id|name|mark|age|
|  |    |    |   |
'''
'''
CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    mark REAL,
    age INTEGER)
INSERT INTO students(name,mark,age) VALUES ("Иванов",4.1,19)
SELECT * FROM students WHERE #ВЫВОД ВСЕХ ДАННЫХ ИЗ ТАБЛИЦЫ
#можно задать условие: SELECT * FROM students WHERE age>19
UPDATE students SET age=20 WHERE name="Иванов" # внесенние изменений в таблицу
DELETE FROM students WHERE id=1 #удаление что-то определенного
'''
#теперь создадим таблицу с помощью питона
import sqlite3
'''
conn=sqlite3.connect("univercity.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,name TEXT,mark REAL,age INTEGER)")
conn.commit()
conn.close()'''
#чтобы проверить созданную таблицу,скачали sqlite на комп и просмотрели в нем созданный файл
'''
def create_tbl():
    conn=sqlite3.connect("univercity.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,name TEXT,mark REAL,age INTEGER)")
    conn.commit()
    conn.close()

def insert_into():
    conn=sqlite3.connect("univercity.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO students(name,mark,age) VALUES ('Maksimova',4.5,19)")
    conn.commit()
    conn.close()
    
def update_info():
    conn=sqlite3.connect("univercity.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE students SET age=29 WHERE id=1")
    conn.commit()
    conn.close()

#create_tbl()
#insert_into()
update_info()
'''
#красивый способ вставки значений в INSERT
'''
name1='Petrov'
mark1=4.0
age1=20
conn=sqlite3.connect("univercity.db")
cursor=conn.cursor()
cursor.execute("INSERT INTO students(name,mark,age) VALUES (?,?,?)",(name1,mark1,age1))
conn.commit()
conn.close()'''

#метод cursor.executemany()
'''
name2='Borovaya'
mark2=4.8
age2=19
name1='Ivanov'
mark1=4.9
age1=20
conn=sqlite3.connect("univercity.db")
cursor=conn.cursor()
cursor.executemany("INSERT INTO students(name,mark,age) VALUES (?,?,?)",[(name1,mark1,age1),(name2,mark2,age2)])
conn.commit()
conn.close()'''

#Принципы ACID:
#-Атомарность
#-Согласованность
#-Изолированность
#-Долговечность
''' '''
# что такое ORM?
#-- Object Relational Mapping - бибдиотека для работы с базами данных
def show_data():
    conn=sqlite3.connect("univercity.db")
    cursor=conn.cursor()
    cursor.execute("SELECT id,name FROM students WHERE age>18")
    rows=cursor.fetchall() #метод передающий массив с записями

    users=[]
    for row in rows:
        users.append(row[1])
    print(users)

show_data()

# при использовании ORM можно было бы написать так:
import sqlalchemy #надо устанавливать через pip install
users=sessiou.query(Student).filter(Student.age>18).all()
print(users)































