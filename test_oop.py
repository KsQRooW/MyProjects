class DescrInt:
    def __set_name__(self, owner, name):
        self.x = name

    def __get__(self, instance, owner):
        print('__get__')
        return instance.__dict__[self.x]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Ошибка')
        instance.__dict__[self.x] = value


class Test:
    a = DescrInt()
    b = DescrInt()
    ...

    def __init__(self, a, b):
        self.a = a
        self.b = b


x = Test(1, 2)
x.a = 'qwerty'
print(x.a)
print(x.b)
