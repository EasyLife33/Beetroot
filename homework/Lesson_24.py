#Task 1
from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:

    if exp < 0:
        raise ValueError

    if exp == 0:
        return 1

    return x * to_power(x, exp - 1)


print(to_power(2, 3))
print(to_power(3.5, 2))
print(to_power(2, -1))


#Task 2
def is_palindrome(looking_str: str, index: int = 0) -> bool:

    if len(looking_str) <= 1:
        return True

    if looking_str[index] != looking_str[-1]:
        return False

    return is_palindrome(looking_str[1:-1])


print(is_palindrome('mom'))


#Task 3
def mult(a: int, n: int) -> int:

    if n < 0:
        raise ValueError

    if n == 0:
        return 0

    return a + mult(a, n-1)


print(mult(2, 4))


#Task 4
def reverse(input_str: str) -> str:

    if len(input_str) == 1:
        return input_str

    return input_str[-1] + reverse(input_str[:-1])


print(reverse('hello'))


#Task 5
def sum_of_digits(digit_string: str) -> int:

    if not digit_string.isdigit():
        raise ValueError

    if len(digit_string) == 1:
        return int(digit_string)

    return int(digit_string[0]) + sum_of_digits(digit_string[1:])


print(sum_of_digits('26'))
