#Task 1
import re
class Email:
    def __init__(self):
        pass


    def validate(self, email):
        if re.match("^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email):
            return (f"{email} -- is correct syntax in email address")
        else:
            return (f"{email} -- is Wrong syntax in email address")



em = Email()

print(em.validate(("abc..def@mail.com")))
print(em.validate(("abc-@mail.com")))
print(em.validate((".abc@mail.com")))
print(em.validate(("abc#def@mail.com")))
print(em.validate(("abc.def@mail.c")))
print(em.validate(("abc.def@mail#archive.com")))
print(em.validate(("abc.def@mail")))
print(em.validate(("abc.def@mail..com")))
print(em.validate(("abc.def@mail.com")))
print(em.validate(("abc.def@mail.org")))
print(em.validate(("abc.def@mail-archive.com")))  # counts as wrong =(  need some check in regex list
print(em.validate(("abc.def@mail.cc")))
print(em.validate(("abc_def@mail.com")))
print(em.validate(("abc@mail.com")))
print(em.validate(("abc.def@mail.com")))
print(em.validate(("abc-d@mail.com")))


#Task 2
import random


class Boss:
    id_s = []  

    @classmethod
    def generate_id(cls):
        """Generation of UNIQUE id"""
        while True:
            id_ = random.randint(1000, 9999)
            if id_ not in cls.id_s:
                cls.id_s.append(id_)
                return id_

    def __init__(self, name: str, company: str):
        self.id = Boss.generate_id()
        self.name = name
        self.company = company
        self.__workers = []

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, new):
        if not isinstance(new, Worker):
            raise TypeError('You can only add workers')
        elif new.boss != self:
            raise ValueError('He doesnt work on you')
        else:
            self.__workers.append(new)

    def __str__(self):
        return f'{self.__class__.__name__}: Mr.{self.name} from {self.company}'

    def __repr__(self):
        return f'{self.id}-{self.name}'


class Worker(Boss):
    def __init__(self, name: str, company: str, boss: Boss):
        super().__init__(name, company)
        if isinstance(boss, Boss):
            self.__boss = boss
            self.__boss.workers = self
        else:
            raise TypeError('Boss must be a Boss instance')

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss: Boss):
        if isinstance(boss, Boss):
            self.__boss.workers.remove(self)  
            self.__boss = boss                
            self.__boss.workers.append(self)  
        else:
            raise TypeError('Boss must be a Boss instance')


b1 = Boss('Ostap', 'Pepsi')
b2 = Boss('Yura', 'Coca-Cola')

w1 = Worker('Oleg', 'Pepsi', b1)
w2 = Worker('Taras', 'Coca-Cola', b2)

print(b1.workers)
print(b2.workers)

w2.boss = b1
w1.boss = b2

print(b1.workers)
print(b2.workers)

w2.boss = b2

print(b1.workers)
print(b2.workers)

#Task 3
from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return int(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return str(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return bool(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return float(result)
            except ValueError:
                print('Convertion is not possible')
                return result
        return wrapper


@TypeDecorators.to_int
def add(a, b):
    return a + b


test_int_1 = add(10, 2.5)
print(test_int_1, type(test_int_1))

test_int_2 = add('a', 'b')
print(test_int_2, type(test_int_2))
