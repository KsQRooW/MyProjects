# iter(a) -> __iter__
# next(a) -> __next__

# Чтобы итерироваться по объекту - нужен в объекте магический метод __iter__ или __getitem__

# Что такое итератор? Это объект итерейбл, у которого есть методы __next__ и __iter__ (или __getitem__)
# Что такое итерируемый объект? Это объект итерейбл, у которого есть метод __iter__ (или __getitem__)
# Любой итератор - это итерируемый объект
# По итератору можно пройтись лишь один раз

# # # # # # # # # # #
"""
Реализация цикла for и его подкапотной логики через while
"""

# for i in x:
#     print(i)
...

# while 1:
#     try:
#         i = next(x)
#         print(i)
#     except StopIteration:
#         break

# # # # # # # # # # #
# class MyIter:
#     """
#     Пример с __iter__ / __getitem__
#     """
#
#     def __init__(self):
#         self.a = [1, 2, 3, 4]
#         self.i = -1
#
#     # def __iter__(self):
#     #     print('__iter__')
#     #     return self
#
#     def __getitem__(self, item):
#         print('__getitem__')
#         return self.a[item]
#
#     def __next__(self):
#         print('__next__')
#         self.i += 1
#         if self.i >= len(self.a) - 1:
#             raise StopIteration
#         return self.a[self.i]
#
#
# myiter = MyIter()
# for i in myiter:
#     print(i)
# print(myiter.a)


# # # # # # # # # # #

# Полностью реализует в себе протокол итератора __iter__ + __next__ (или __getitem__)
# По генератору можно пройтись лишь один раз
# Чтобы создать генератор можно использовать yield или с помощью генераторного выражения

# 1 вариант - yield
# def func(x):
#     for i in x:
#         yield i
#
#
# z = func([1, 2, 3])
# print(type(z))
# for i in z:
#     print(i)

# 2 вариант - генераторное выражение
# z = (i for i in [1, 2, 3])
# print(type(z))
# for i in z:
#     print(i)

# # # # # # # # # # #
