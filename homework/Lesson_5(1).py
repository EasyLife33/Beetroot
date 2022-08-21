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