#Task 1
def abc():
    x = 5
    y = 10
    str1= "random text"
    print("Something")

print(abc.__code__.co_nlocals)

#Task2
def outer_func():
    print('Get inner func')

    def inner_func():
        print('Inner func')

    return inner_func


func = outer_func()  
func()

#Task 3
nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    lists = [i for i in nums if i > 0]
    if len(lists) == len(nums):
        print(func1(lists))
    else:
        print(func2(nums))

choose_func(nums1, square_nums, remove_negatives)
choose_func(nums2, square_nums, remove_negatives)
