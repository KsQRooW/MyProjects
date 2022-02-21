def first_decorator_func(func):

    def decorator_func_helper(*args, **kwargs):
        print('first_START')
        func(*args, **kwargs)
        print('first_END')

    return decorator_func_helper


def second_decorator_func(func):

    def decorator_func_helper(*args, **kwargs):
        print('second_НАЧАЛО')
        func(*args, **kwargs)
        print('second_КОНЕЦ')

    return decorator_func_helper


@second_decorator_func
@first_decorator_func  # summa = second_decorator_func(first_decorator_func(summa))
def summa(a, b):
    print(a + b)


x = 3
y = 5
summa(x, y)
