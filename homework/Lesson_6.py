#Task 1
import random
list_abc = [random.randint(100,200) for i in range(10)]
print(list_abc)
print('The highest number is ',max(list_abc))


#Task 3
abc=[]
for x in range(1, 100):
    if (x%7==0) and (x%5==0):
        abc.append(str(x))
print (','.join(abc))
