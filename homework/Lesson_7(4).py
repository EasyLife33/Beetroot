import calendar as smth
week = {i + 1: smth.day_name[i] for i in range(0, 7)}
week1 = {smth.day_name[i]: i + 1 for i in range(0, 7)}
print(week)
print(week1)