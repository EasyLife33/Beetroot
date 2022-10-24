from Lesson_26 import Stack


class ExtendedStack(Stack):

    def get_from_stack(self, value):
        for i, val in enumerate(self.items):
            if val == value:
                return self.items.pop(i)
        else:
            raise ValueError('There is no value like this in this stack')


es = ExtendedStack([1, 2, 3, 4, 5])
print(es.get_from_stack(2))
print(es)
