from __future__ import annotations

from abc import ABC, abstractmethod


class Kettlebell(ABC):
    """
    Базовая модель гири
    """

    def __init__(self, value: int):
        """
        :param value: вес гири в _default единицах измерениях
        """
        self.value = value

    @property
    @abstractmethod
    def _default(self) -> str:
        """ Возвращает сокращенное имя единицы измерения по умолчанию """

    @property
    @abstractmethod
    def _coefs(self) -> dict[str, int]:
        """ Возвращает маппинг коэффициентов перевода _default единицы измерения в другие """

    @abstractmethod
    def get(self, unit: str = None) -> float:
        """
        Возвращает вес гири в указанных единицах измерения

        :param unit: наименование единицы измерения
        :return: вес гири, переведенный из единицы измерения _default в unit единицу измерения
        """


class KettlebellSI(Kettlebell):
    """
    Модель гири, вес которой измеряется в единицах измерения СИ
    """

    @property
    def _default(self) -> str:
        pass

    @property
    def _coefs(self) -> dict[str, int]:
        pass

    def get(self, unit: str = None) -> float:
        pass


class KettlebellSGS(Kettlebell):
    """
    Модель гири, вес которой измеряется в единицах измерения СГС

    Единицы измерения по умолчанию - граммы

    Примеры использования:
        # kettlebell = KettlebellSGS(100)
        # kettlebell.get()  # return 100.0
        # kettlebell.get("кг")  # return 0.001
    """

    @property
    def _default(self) -> str:
        """ Возвращает имя единицы измерения"""
        return "г"

    @property
    def _coefs(self) -> dict[str, int]:
        return {
            self._default: 1,
            "кг": 1 * 10 ** 3,
            "ц": 1 * 10 ** 6,
            "т": 1 * 10 ** 9
        }

    def get(self, unit: str = None) -> float:
        unit = unit or self._default
        if unit not in self._coefs:
            raise ValueError(f"Переданное имя единицы измерения {unit} не существует. "
                             f"Попробуйте одно из {self._coefs.keys()}")
        return self.value / self._coefs[unit]


class BowlScales:
    """
    Модель весов с чашами

    Пример использования:
        # lite_kettlebell = KettlebellSGS(1)
        # bowl_scales = BowlScales(2, lite_kettlebell)
        # bowl_scales.resolve_algorithm(1000)
    """

    class Bowl:
        """
        Модель чаши весов

        Данная сущность не может существовать отдельно от весов

        TODO: существующая реализация работает лишь с одним грузом, одного веса
        """
        def __init__(self, kettlebell_weight: int | float, with_kettlebell: bool = False):
            """
            :param kettlebell_weight: вес гири
            :param with_kettlebell: флаг, в случае True - означает, что на чаше изначально имеется гиря
            """
            self._kettlebell_weight = kettlebell_weight

            self._with_kettlebell = with_kettlebell
            self.weight = 0 + kettlebell_weight

        @property
        def with_kettlebell(self):
            return self._with_kettlebell

        @with_kettlebell.setter
        def with_kettlebell(self, value: bool):
            """
            Устанавливаем/убираем гирю на чашу (в зависимости от ее наличия на чаше - меняется вес чаши)

            :param value: True - значит на чашу была установлена гиря
            """
            if not isinstance(value, bool):
                raise TypeError(f"Значение value может быть только bool. Полученный тип - {type(value).__name__}")
            self._with_kettlebell = value
            if value:
                self.weight += self._kettlebell_weight
            else:
                self.weight -= self._kettlebell_weight

        def __repr__(self):
            """
            Представление чаши, 2 варианта:
                1) "10" - означает, что на чаше лежит вес размером 10 единиц
                2) "10(1)" - означает, что на чаше лежит вес размером 10 единиц, но 1 из 10 единиц - это гиря
            """
            if self._with_kettlebell:
                return f"{int(self.weight)}({int(self._kettlebell_weight)})"
            return f"{int(self.weight)}"

    def __init__(self, n: int, kettlebell: Kettlebell):
        """
        **self.actions** - события, на которые нужно либо убрать гирю, либо наоборот опустить на 1 чашу
            (для событий с четным индексом - гирю нужно убрать)
        **self.n** - количество весовых чаш
        **self.bowls** - список весовых чаш, на которые будут выкладываться зерна

        :param n: количество чаш
        """
        self.actions: list[int] = []
        self.n = n
        self.bowls: list[BowlScales.Bowl] = [self.Bowl(kettlebell.get(), with_kettlebell=True)
                                             if i == 0 else
                                             self.Bowl(kettlebell.get())
                                             for i in range(n)]


    def resolve_algorithm(self, res_weight: int | float):
        """
        Метод печатает состояния чаш на каждом из этапов

        TODO: Данный метод пока работает лишь с 2 чашами

        TODO: Была попытка решить общую задачу, когда на вход можно дать любой res_weight, с любой гирей и
            весами с любым набором чаш... Пока данная попытка терпит крах, но некоторые кейсы решает (не буду спорить,
            что в основном это совпадение, поэтому даже не буду их приводить).

        :param res_weight: вес, который нужно получить с помощью взвешивания на весах
        """
        degree = self._bowles_degree(res_weight)
        self._solve_actions(self.n ** degree - res_weight)

        for i in range(0, degree):
            if i == 0:
                self.bowls[1].weight = self.bowls[0].weight
            elif i not in self.actions:
                self.equalization_bowls()
            else:
                if self.actions.index(i) % 2 == 0:
                    self.bowls[0].with_kettlebell = False
                    self.equalization_bowls()
                else:
                    self.bowls[0].with_kettlebell = True
                    self.equalization_bowls()
            print(f"State - {i}", self.bowls)

        # обнуляем состояние весов и событий
        self.reset_bowls()
        self.actions = []


    def equalization_bowls(self):
        """
        Из чаш без гири перекладываем все в чашу с гирей, а чаши без гири после этого - заполняем весом,
        который эквивалентен текущему весу чаши с гирей
        """
        for bowl in self.bowls[1:]:
            self.bowls[0].weight += bowl.weight
            bowl.weight = self.bowls[0].weight

    def reset_bowls(self):
        """
        Возвращает состояние чаш весов в исходное:
            - на одной чаше лежит гиря и более никакого веса
            - на всех остальных чашах не лежит ничего
        """
        self.bowls[0].weight = 0
        self.bowls[0].with_kettlebell = True

        for bowl in self.bowls[1:]:
            bowl.weight = 0

    def _bowles_degree(self, res_weight: int | float) -> int:
        """
        Вычисляем максимальную степень в которую нужно возвести количество чаш весов, чтобы получить значение, которое
        будет >= res_weight

        :param res_weight: вес, который нужно получить с помощью взвешивания на весах
        :return: степень для числа, равного количествам чаш весов
        """
        degree = 0
        while self.n ** degree < res_weight:
            degree += 1
        return degree

    def _solve_actions(self, difference: int | float):
        """
        Определяем события, на которых нужно положить/забрать гирю

        На событиях, которые стоят на четных позициях списка - гирю нужно забрать
        Для событий на нечетных позициях - гирю нужно положить

        :param difference: разница между (количество_чаш ** _bowles_degree) - (вес_который_нужно_получить)
        """
        i = 0
        while (val := self.n ** i) < difference:
            i += 1
        else:
            if val == difference:
                # отсчет данного действия начинается с предыдущего действия по номеру
                self.actions.append(sum(self.actions) - 1 + i)
            else:
                self.actions.append(sum(self.actions) + i)
                self._solve_actions(val - difference)


lite_kettlebell = KettlebellSGS(1)
bowl_scales = BowlScales(2, lite_kettlebell)
bowl_scales.resolve_algorithm(1000)

# P.S. hint kettlebell: Kettlebell - и есть то самое dependency injection, пока писал этот код - само вспомнилось.
# На созвоне назвал неверное определение. Проще говоря - не стоит завязываться на реализацию, завязываться нужно на
# абстракции.

# P.P.S. Скажу одно, эту элементарную задачу и ее проектирование я бы мог развивать большое количество времени...
# Даже на такой примитивной задаче с 2-3 сущностями - можно не хило развернуться.
# Тот же класс Bowl можно реализовать еще кучей вариантов, например, если развернуться через дескриптор,
# то можно было бы избавиться от уродской конструкции типа [index].attribute.
# В общем, это было любопытное занятие. В данной реализации представлено не мало недочетов, я бы весь свой код мог бы
# покрыть еще тонной TODO.
# Но лучше остановлюсь на том, что уже есть. За один вечер, думаю, этого будет достаточно.
