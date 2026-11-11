'''
HTTP-методы: GET,POST,PUT,DELETE
коды ответов:
404-ошибка клиента
400
429-too many requests
500-внутренняя ошибка сервера
503-сервис недоступен
301-страница перемещена '''
#библиотека requests-синхронная. асинхронные библиотеки для работы с web тоже существуют
'''
import requests
response=requests.get('https://jsonplaceholder.typicode.com/posts/13')
print(f"Статус код:{response.status_code}")
print(f"Текст ответа:{response.text}")
data=response.json()
print(f"Заголовок поэта:{data['title']}")

payload={'user':'Ivan','age':25}
response=requests.get('https://httpbin.org/get',params=payload)
print(response.url)
print(response.text)

url='https://httpbin.org/post'
payload={'title':'foo','body':'bar','userID':13}
response1=requests.post(url,json=payload)
print(response1.text)

payload_form={'username':'admin','password':'secret'}
response2=requests.post(url,data=payload_form)
print(response2.text)'''

import requests
'''
headerz={
    'User_Agent':'MyAwesomeUserAgent/1.0',
    'Authorization':'Bearer gth_token'}
response=requests.get('https://api.github.com/user',headers=headerz)
print(response.text)
# почитать дома про сессии, метод Sessions
# обработка ошибок
try:
    response=requests.get('url',timeout=5)
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("Сервер залип, время вышло!")
except requests.exceptions.HTTPError as e:
    print(f"Ошибка http {e}")
except requests.exceptions.ConnectionError:
    print("Нет связи с сервером")
except requests.exeptionsRequestException as e:
    print(f"Непредвиденная ошибка {e}")
#скачивание фильма 
url='http:site.com/dounloads/large_movie.mp4'
with requests.get(url,stream=True) as r:
    r.raise_for_status()
    with open('vidos.mp4','wb')as f:
        for chunk in r.itek_content(chunk_size=8192):
            f.write(chunk)'''
'''
name="Саша"
try:
    agee=requests.get('https://api.agify.io?name=Саша',timeout=20)
    agee.raise_for_status()
    agee=agee.json()
    genger=requests.get('https://api.genderize.io?name=Саша',timeout=20)
    genger.raise_for_status()
    genger=genger.json()
except requests.exceptions.Timeout:
    print("превышено время ожидания ответа от API")
    exit(1)
except requests.exceptions.ConnectionError:
    print("не удалось подключиться к API")
    exit(1)
except requests.exceptions.HTTPError as e:
    print(f"Ошибка HTTP: {e}")
    exit(1)
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
    exit(1)

age = agee.get("age")
gender = genger.get("gender")
prob = genger.get("probability")

female_prob = prob if gender == "female" else 1 - prob if prob is not None else None
print(f"Цель: {name}. Вероятный возраст {age}, вероятность женского пола {female_prob}")

'''
import requests

name = "Sofa"

agee=requests.get('https://api.agify.io?name=',params={'name': name},timeout=20)
agee.raise_for_status()
agee=agee.json()

genger=requests.get('https://api.genderize.io?name=',params={'name': name},timeout=20)
genger.raise_for_status()
genger=genger.json()


age = agee.get("age")
gender = genger.get("gender")
prob = genger.get("probability")

female_prob = prob if gender == "female" else 1 - prob if prob is not None else None
print(f"Цель: {name}. Вероятный возраст {age}, вероятность женского пола {female_prob}")








    
