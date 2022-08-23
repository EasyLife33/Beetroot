abc=[]
for x in range(1, 100):
    if (x%7==0) and (x%5==0):
        abc.append(str(x))
print (','.join(abc))