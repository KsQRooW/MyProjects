"""
В олимпиаде по информатике принимало участие N человек.
Определите школы, из которых в олимпиаде принимало участие больше всего участников.
В этой задаче необходимо считывать данные построчно, не сохраняя в памяти данные обо всех участниках,
а только подсчитывая число участников для каждой школы.

Структура файла:
    Фамилия Имя Школа Балл

Формат вывода:
    Выведите номера этих школ в порядке возрастания.
"""

doc = open('NaibChisloYchastnikov.txt', 'r', encoding='utf8')
schools = {}
for stroka in doc:
    nabor_slov = stroka.split()  # Фамилия[0] Имя[1] Школа[2] Балл[3]
    schools[int(nabor_slov[2])] = schools.setdefault(int(nabor_slov[2]), 0) + 1
max_value = max(schools.values())
print(*sorted([i[0] for i in schools.items() if i[1] == max_value]))
