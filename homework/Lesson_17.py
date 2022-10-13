#Task 1
class Animal:
    def talk(self):
        raise NotImplementedError


class Dog(Animal):
    def talk(self):
        print('Woof woof')


class Cat(Animal):
    def talk(self):
        print('Meow')


def animal_talk(animal):
    animal.talk()


dog = Dog()
cat = Cat()

animal_talk(dog)
animal_talk(cat)
func(billy)
func(thomas)


#Task 2
class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Book:
    number_of_books = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.number_of_books += 1

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'{self.name}. {self.author}'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def new_book(self, name: str, year: int, author: Author) -> Book:
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        return book

    def group_by_author(self, author: Author) -> list:
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int) -> list:
        return [book for book in self.books if book.year == year]


l = Library('central')

g_r_r_martin = Author('George R. R. Martin', 'USA', 1948)
s_king = Author("Stephen King", 'USA', 1947)

l.new_book(" A Game of Thrones", 1996,g_r_r_martin )
l.new_book("Song of ice and fire", 1998, g_r_r_martin)
l.new_book("The Dark Tower IV: Wizard and Glass", 1997, s_king)

print(l.group_by_year(1997))
print(l.group_by_author(g_r_r_martin))


#Task 3


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        if self.numerator == 0:
            return '0'
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + '/' + str(self.denominator)

    def greatest_common_divisor(self, a, b):
        if a % b == 0:
            return b
        else:
            return self.greatest_common_divisor(b, a % b)

    def lowest_common_denominator(self, a, b):
        return a * b // self.greatest_common_divisor(a, b)

    def clean_fraction(self, numerator, denominator):
        gcd = self.greatest_common_divisor(numerator, denominator)
        numerator /= gcd
        denominator /= gcd
        return Fraction(int(numerator), int(denominator))

    def __add__(self, other):
        if self.denominator == other.denominator:
            numerator = self.numerator + other.numerator
            denominator = self.denominator
        else:
            denominator = self.lowest_common_denominator(self.denominator, other.denominator)
            numerator = self.numerator * denominator/self.denominator + other.numerator * denominator/other.denominator
        return self.clean_fraction(numerator, denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            numerator = self.numerator - other.numerator
            denominator = self.denominator
        else:
            denominator = self.lowest_common_denominator(self.denominator, other.denominator)
            numerator = self.numerator * denominator / self.denominator - other.numerator * denominator / other.denominator
        return self.clean_fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return self.clean_fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return self.clean_fraction(numerator, denominator)


x = Fraction(1, 2)
y = Fraction(1, 4)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
