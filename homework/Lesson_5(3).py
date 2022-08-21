import random

s = input()
for i in range(5):
    print(''.join(random.choice(s) for j in range(len(s))))