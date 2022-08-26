#Task 1
import random
it=random.randint(0, 10)
def main():
    x=int(input('Guess a number one through one hundred: '))
    if x == it:
        print("That is right! Congrats")
    elif x > it:
        print("Your answer is too high")
        main()
    else:
        print("Your answer is too low")
        main()
main()


#Task 2
name = input("Enter your name: ") 
current_age = int(input("Enter your age: ")) 
next_year =  ( current_age + 1)
print(f'Hello {name} on your next birthday you’ll be {next_year}.')


#Task 3
import random

s = input()
for i in range(5):
    print(''.join(random.choice(s) for j in range(len(s))))
