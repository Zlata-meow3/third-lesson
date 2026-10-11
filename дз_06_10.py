import json
#открываем файл с пользователями для чтения
with open('users.json', 'r', encoding='utf-8') as f:
    users = json.load(f)
#создаем словарь городов
cities = {}
for us in users:
    city = us['address']['city'] #выделяем город
    cities[city]=[] #добавляем город в словарь
    cities[city].append(us['name']) #записываем имя пользователя
#создаем файл с этими значениями
with open('cities.json', 'w', encoding='utf-8') as f:
    json.dump(cities, f, ensure_ascii=False, indent=2)
