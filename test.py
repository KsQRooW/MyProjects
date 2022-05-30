# from urllib import parse
#
#
# class Site:
#     def __init__(self, url=''):
#         self.url = url
#         self._domain = ''
#         self._max_lvl = None
#
#     def domain_lvl(self, lvl):
#         if not self._max_lvl:
#             self._solve_domain()
#
#         if 1 <= lvl <= self._max_lvl:
#             return "lvl {lvl}: {domain}".format(lvl=lvl, domain=getattr(self, f"domain_lvl{lvl}"))
#         raise ValueError(f"\nЗапрошенное значение - {lvl}"
#                          f"\nМаксимально допустимый уровень - {self._max_lvl}"
#                          f"\nМинимально допустимый уровень - 1")
#
#     @property
#     def domain(self):
#         if self._domain:
#             return self._domain
#
#         self._solve_domain()
#         return self._domain
#
#     def _solve_domain(self):
#         print(">>> let's go solve domain <<<")
#         parts = parse.urlsplit(self.url).netloc.split('.')[::-1]
#         for i, part in enumerate(parts[:-1] if parts[-1] == 'www' else parts):
#             setattr(self, f'domain_lvl{i + 1}', part)
#             self._max_lvl = i + 1
#
#         for i, lvl in enumerate(filter(lambda x: x.startswith('domain_lvl'), self.__dict__)):
#             self._domain += f'lvl {i + 1}: {getattr(self, lvl)}\n'
#
#
# # import re
# #
# #
# # class Site:
# #     urlstring = ''
# #     mainDict = {}
# #
# #     def __init__(self, d):
# #         self.urlstring = d
# #         self.tupleURL = ()
# #
# #     def print1(self):
# #         for i in range(len(self.tupleURL) - 1, -1, -1):
# #             number = int(self.tupleURL[i][0])
# #             name = self.tupleURL[i][1]
# #             print(f'lvl {abs(number)}: ', name)
# #             Site.mainDict[number] = name
# #         return ''
# #
# #     def domain(self):
# #         if len(Site.mainDict) > 0:
# #             for i in Site.mainDict.keys():
# #                 print(f'lvl {abs(int(i))}: ', Site.mainDict[i])
# #         else:
# #             print('domain ')
# #             line = re.findall(r'\w+', self.urlstring)
# #             line = line[2:]
# #             tuple1 = tuple(enumerate(line, -len(line)))
# #             self.tupleURL = tuple1
# #             return self.print1()
# #         return ''
#
#
# my_site = Site('https://www.vk.messages.video.google.com/')
# new_site = Site('https://www.vk.messages.com/')
# print(my_site.domain)
# print(my_site.domain)
# print(new_site.domain_lvl(10))
# print()
# print(new_site.domain_lvl(2))
# print()
# print(new_site.domain)
# from abc import ABC, abstractmethod
#
#
# class People:
#     def method1(self):
#         print(self)
#
#     def method2(self):
#         print(self)
#
#
# class IntefaceMethod3(ABC):  # Интерфейс
#     @abstractmethod
#     def method3(self):  # Абстрактный метод
#         pass
#
#
# class PersonNew1(IntefaceMethod3):  # Абстркатный класс
#     def method3(self):
#         pass
#
#     def method4(self):
#         print(self)
#
#
# class PersonNew2(IntefaceMethod3):
#     def method3(self):
#         print(self)
#
#
# class PersonNew3(IntefaceMethod3):
#     def method3(self):
#         print(self)
#
#
# class Client1(People, PersonNew1):  # 1, 2, 3
#     """
#     class Client1
#     """
#
#
# class Client2(People):  # 1, 2
#     pass
#
#
# class Client3(People, PersonNew1):  # 1, 2, 3
#     pass
#
#
# im = Client1()
# im.method3()

# Абстрактный класс - набор абстрактных методов + набор реализованных методов
# Интерфейс - набор только абстрактных методов
# Нельзя создать экземпляр ни интерфейса, ни абстрактного класса
# Лучше много интерфейсов, чем один большой и общий интерфейс
# from abc import ABC, abstractmethod
# Чтобы нельзя было инициализировать класс - наследуй его от ABC
# Чтобы пометить метод как абстрактный - декоратор abstractmethod


# 10 or 5 - возвращаем первый попавшийся True, иначе вернем последнее
# 10 and 5 - возвращаем первый попавшийся False, иначе вернем последнее


class A:
    numb = 10

    def method1(self, a):  # >
        print('method1', locals())
        DeprecationWarning('метод 1 устарел')


class B:
    numb = 20

    def method1(self, a):  # <
        print('method1 -> B')
        return self.numb < a.numb


# > - __lt__, < - __gt__
def main():
    x = A()
    y = B()
    x.method1(y)
    print('main', locals())
# frozenset, namedtuple

print(locals())

# if __name__ == '__main__':
#     main()
#     print('__name__', locals())
