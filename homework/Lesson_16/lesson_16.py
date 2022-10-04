#Task 1
class Person():

    def __init__(self, firstname, lastname, age):
        if age < 0:
            raise ValueError("Age can't be less than 0")

        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old")

class Student(Person):

    def __init__(self, firstname, lastname, age, speciality, course):
        super().__init__(firstname, lastname, age)
        self.speciality = speciality
        self.course = course

    def study(self):
        print(f"""{self.firstname} {self.lastname} is a {self.course} year {self.speciality}. 
{4 - self.course} years left until  degree""")

class Teacher(Person):

    def __init__(self, firstname, lastname, age, salary, teacher_degree):
        super().__init__(firstname, lastname, age)
        self.salary = salary
        self.teacher_degree = teacher_degree

    def work(self):
        print(f"{self.firstname} {self.lastname} has a {self.teacher_degree} and receives a salary of  {self.salary} UAH")


random_student = Student("Carlie", "Wolf", 20, "student of computer science", 2)

random_teacher = Teacher("Izabela", "Marques", 39, 40000, "doctorate in computer science")

random_teacher.talk()
random_teacher.work()

random_student.talk()
random_student.study()



#Task 2
class Mathematician(list):

    def square_nums(self, _list):
        return [i**2 for i in _list]

    def remove_positives(self, _list):
        return [i for i in _list if i < 0]

    def filter_leaps(self, _list):
        return [i for i in _list if i % 4 == 0]


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))

print(m.remove_positives([26, -11, -8, 13, -90]))

print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))



#Task 3
class Product:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price


class Article(Product):
    def __init__(self, product: Product, amount):
        self.name = product.name
        self.amount = amount
        self.discount = 0


class Store:
    def __init__(self, id):
        self.id: int = id
        self.profit: 'percent' = 30
        self.goods: dict = {}  
        self.departments: dict = {}
        self.income = 0

    def add(self, product: Product, amount: int):
        new = Article(product, amount)
        new.price = round(product.price + product.price * self.profit/100, 2)
        self.goods[new.name] = new
        if product.type not in self.departments.keys():
            self.departments[product.type] = [new]
        else:
            self.departments[product.type].append(new)

    def set_discount(self, identifier, percent, ident_type='name'):
        if percent >= 100:
            raise ValueError("Please pay for this")
        if ident_type == 'name':
            try:
                self.goods[identifier].discount = percent
            except KeyError:
                raise ValueError('There is no such product in the store')
        elif ident_type == 'type':
            if identifier not in self.departments:
                raise ValueError('There is no such department in the store')
            for article in self.departments[identifier]:
                article.discount = percent
        else:
            raise ValueError('Wrong identifier type')

    def sell(self, product_name, amount):
        try:
            goods = self.goods[product_name]
        except KeyError:
            raise ValueError('These product is currently unavaible in the store')
        goods.amount -= amount
        self.income += (goods.price - goods.price * goods.discount/100) * amount

    def get_income(self):
        print(self.income)

    def get_all_products(self):
        for department, goods in self.departments.items():
            print(f'---{department.upper()}---')
            for article in goods:
                print(f'Name: {article.name}')
                print(f'Available: {article.amount}')
                print(f'Price: {article.price}')
                if article.discount:
                    disc_price = round(article.price - article.price * article.discount/100, 2)
                    print(f'DISCOUNT {article.discount}%. ONLY FOR {disc_price}')
                print()

    def get_product_info(self, product_name):
        print(f'({self.goods[product_name].name}, {self.goods[product_name].amount})')


product1 = Product('Ramen', 'Food', 1.5)
product2 = Product('Apple', 'Food', 1.2)
product3 = Product('Soap', 'Household', 5)
product4 = Product('Fairy', 'Household', 8)
product5 = Product('T-shirt', 'Sport', 30)
product6 = Product('Ball', 'Sport', 20)
products = {product1: 20, product2: 200, product3: 64, product4: 41, product5: 240, product6: 10}

atb = Store(111)

for products, amount in products.items():
    atb.add(products, amount)
atb.get_all_products()

check = {'Apple': 12, 'Soap': 2, 'T-shirt': 1}
for name, amount in check.items():
    atb.sell(name, amount)
atb.get_income()

atb.set_discount('Household', 15, 'type')
atb.set_discount('Ball', 25)
atb.get_all_products()




#Task 4
class CustomException(BaseException):

    def __init__(self, msg):
        super().__init__(msg)
        with open('logs.txt', 'a') as file:
            file.write(msg + '\n')


raise CustomException("That's not good")
