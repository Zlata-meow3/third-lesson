'''
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    #def __str__(self):
     #   return f"{self.name},возраст: {self.age}"
    def __repr__(self):
        return f"Cat(name='{self.name}',age='{self.age}')"
cat=Cat('Vaciy',3)
print(cat)

def my_shiny_new_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()
        print("А я - код, который отработает после")
    return the_wrapper_around_the_original_function
def stand_alone_function():
    print("Я простая функция, и я не хочу изменений")
stand_alone_function_decorated=my_shiny_new_decorator(stand_alone_function)
stand_alone_function_decorated()
# Два варианта вызова фунуции: через @ и через присваивание
@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставьте меня в покое!!!")
another_stand_alone_function()'''

#cтроим бутерброд
'''
def bread(func):
    def wrapper():
        print()
        func()
        print("<\_____/>")
    return wrapper
def ingredients(func):
    def wrapper():
        print("#помидоры")
        func()
        print("~салат~")
    return wrapper
def sandwich(food="--ветчина--"):
    print(food)
sandwich=bread(ingredients(sandwich))
sandwich()


@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)
sandwich()


@ingredients
@bread
def sandwich(food="--ветчина--"):
    print(food)
sandwich()
'''
'''
def decorator_passing_argm(function_to_decorate):
    def wrapper_accepting_argm(arg1,arg2):
        print("Смотри, что я получил:",arg1,arg2)
        function_to_decorate(arg1,arg2)
    return wrapper_accepting_argm
@decorator_passing_argm
def print_full_name(first_name,last_name):
    print("Меня зовут",first_name,last_name)
print_full_name("Vasya","Pupkin")'''

# Статические методы
'''
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def is_valid_age(age):
        return isinstance(age,int) and 0<age<150
    @staticmethod
    def is_valid_name(name):
        return isinstance(name,str) and len(name)>0
if User.is_valid_age(25) and User.is_valid_name("Vanya"):
    user=User("Vanya",25)
    print(user.age,user.name)'''

# наследование
'''
class Shape:
    def area(self):
        print("Метод должен быть определен")
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
circle=Circle(10)
circle.area()
'''  
# абстрактный метод
'''
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def describe(self):
        print("Я фигура площадью",self.area())
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
#shape=Shape() - не работает, нужно переопределить метод area в дочернем классе
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
sq=Square(10)
print(sq.area())#100
print(sq.describe())'''

# наследование+методы
'''
from abc import ABC,abstractmethod
class DataProcessor(ABC):
    def __init__(self,data):
        self.data=data
    @abstractmethod
    def process(self):
        pass
    @staticmethod
    def validate_data(data):
        return isinstance(data,list) and len(data)>0
    @staticmethod
    def format_output(result):
        return f"Результат:{result}"

class NumProcessor(DataProcessor):
    def process(self):
        if not self.validate_data(self.data):
            print("Некрасивые данные")
        return sum(self.data)

processor=NumProcessor([1,2,3,4,5])
result=processor.process()
print(NumProcessor.format_output(result))
print(DataProcessor.format_output(result))'''


















