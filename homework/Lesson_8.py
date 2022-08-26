#Task 1
def favorite_movie(movie):
    print("My favorite movie is: " + movie)
favorite_movie(" hard to choose one.") 


#Task 2
def make_country(**kwargs):
        for name, capital in kwargs.items():
            print(f"{name}:{capital}")
make_country(Italy="Rome",Greece="Athens")


#Task 3
def make_operation(operator, *numbers):
    
    if operator == '+':
        num_result = 0
        for num in numbers:
            num_result += num
    
    elif operator == '-':        
        num_result = 2*numbers[0]
        for num in numbers:
            num_result -= num 
        
    elif operator == '*':
        num_result = 1
        for num in numbers:            
            num_result *= num
    return num_result

print(make_operation('+', 7, 7, 2))  
print(make_operation('-', 5, 5, -10, -20))  
print(make_operation('*', 7, 6))  

