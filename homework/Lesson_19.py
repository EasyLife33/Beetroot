#Task 1
def with_index(iterable, start=0):
    for i in iterable:
        yield start, i
        start += 1


test = 'Yura'
for index, value in with_index(test, 1):
    print(index, value)

test2 = with_index(test)
print(next(test2))
print(next(test2))
print(next(test2))


#Task 2
def in_range(start, end, step=1):
    while start != end:
        yield start
        start += step


for i in in_range(0, 10):
    print(i, end=' ')

print()

for i in in_range(10, 0, -1):
    print(i, end=' ')

print()

for i in in_range(0, 50, 2):
    print(i, end=' ')


#Task 3
class Iter:
    def __init__(self, num: int):
        self.num = num
        self.seq = Iter.num_to_seq(num)
        self.index = 0

    def __repr__(self):
        return ''.join([str(n) for n in self.seq])

    @classmethod
    def num_to_seq(cls, num: int) -> list:
        seq = []
        while num != 0:
            seq.append(num % 10)
            num //= 10
        seq.reverse()
        return seq

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.seq[self.index]
        except IndexError:
            raise StopIteration
        finally:
            self.index += 1

    def __getitem__(self, item):
        return self.seq[item]

    def __setitem__(self, key, value):
        self.seq[key] = value


i = Iter(102436)

print('My view - ', i)

print('Iteration in for loop:')
for item in i:
    print(item, end='   ')
print()

print('Getting item - ', i[4])

i[0] = 8
print('Setting item - ', i)
