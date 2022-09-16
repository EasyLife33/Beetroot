#Task 1
def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} called with {str(args)[1:-1]}")
        return func(*args)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


if __name__ == "__main__":
    result1 = add(1, 2)
    result2 = square_all(1, 2, 3, 4, 5)
    
    
#Task 2    
def stop_words(words: list):
    def inner(func):
        def wrapper(*args, **kwargs):
            s = func(*args, **kwargs)
            for i in words:
                s = s.replace(i, "*")
            return s
        return wrapper
    return inner


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == "__main__":
    assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


#Task 3
def arg_rules(type_: type, max_length: int, contains: list):
    def inner(func):
        def wrapper(*args, **kwargs):
            if len(args) != 0:
                for i in args:
                    if type(i) != type_ or len(i) > max_length or not all(k in i for k in contains):
                        return False
                    else:
                        return func(*args, **kwargs)
        return wrapper
    return inner


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == "__main__":
    assert create_slogan('johndoe05@gmail.com') is False
    assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
    assert create_slogan('SSH05') is False
    assert create_slogan(1) is False
