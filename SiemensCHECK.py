from pathlib import Path


def exist_folders(path):  # Проверяет наличие каталогов ft_run и ft_reference для теста
    folders_list = list(map(lambda x: x.stem, (path.iterdir())))
    if 'ft_reference' not in folders_list and 'ft_run' not in folders_list:
        with path.joinpath('report.txt').open('w') as file:
            file.write('directory missing: ft_run\n')
            file.write('directory missing: ft_reference')
        return False
    elif 'ft_reference' not in folders_list:
        with path.joinpath('report.txt').open('w') as file:
            file.write('directory missing: ft_reference')
    elif 'ft_run' not in folders_list:
        with path.joinpath('report.txt').open('w') as file:
            file.write('directory missing: ft_run')
        return False
    elif 'ft_run' in folders_list and 'ft_reference' in folders_list:
        return True


def fileset_equality(path):  # Проверяет на совпадение файлов ft_run и ft_reference
    file_list_ref = set(map(lambda x: x.stem, path.rglob('ft_reference/**/*.stdout')))
    file_list_run = set(map(lambda x: x.stem, path.rglob('ft_run/**/*.stdout')))
    list_missing_files = list(
        map(lambda x: "'" + x + '/' + x + ".stdout'", list(file_list_ref.difference(file_list_run))))
    list_extra_files = list(
        map(lambda x: "'" + x + '/' + x + ".stdout'", list(file_list_run.difference(file_list_ref))))
    if file_list_ref != file_list_run:
        with path.joinpath('report.txt').open('w') as file_out:
            if len(list_missing_files) != 0:
                file_out.write('In ft_run there are missing files present in ft_reference: ')
                file_out.writelines(', '.join(sorted(list_missing_files)) + '\n')
            if len(list_extra_files) != 0:
                file_out.write('In ft_run there are extra files not present in ft_reference: ')
                file_out.writelines(', '.join(sorted(list_extra_files)) + '\n')
        return False
    else:
        return True


def error_check(path):  # Проверяет отсутствие "error" в файле из ft_run
    files_ft_run = path.rglob('ft_run/**/*.stdout')
    for value in files_ft_run:
        with value.open() as file_input:
            counter = 0
            for line in file_input:
                counter += 1
                if any(map(lambda x: x.startswith('error'), line.lower().split())):
                    with value.parents[2].joinpath('report.txt').open('a') as file_out:
                        file_out.write(value.parent.stem + '/' + value.name + '(' + str(counter) + '): ' + line)


def solver_check(path):  # Проверяет наличие "Solver finished at" в файле из ft_run
    files_ft_run = path.rglob('ft_run/**/*.stdout')
    for value in files_ft_run:
        with value.open() as file_input:
            check_solver = False
            for line in file_input:
                if not check_solver:
                    if line.lower().startswith('solver finished at'):
                        check_solver = True
            if not check_solver:
                with value.parents[2].joinpath('report.txt').open('a') as file_out:
                    file_out.write(value.parent.stem + '/' + value.name + ': ' + "missing 'Solver finished at'\n")


"""
Можно было бы объединить функции solver_check и error_check в одну для более быстрой работы скрипта,
но для отладки удобнее было бы работать без объединения этих функций в одну

def solver_error_check(path):
    files_ft_run = path.rglob('ft_run/**/*.stdout')
    for value in files_ft_run:
        with value.open() as file_input:
            counter = 0
            check_solver = False
            for line in file_input:
                counter += 1
                if any(map(lambda x: x.startswith('error'), line.lower().split())):
                    with value.parents[2].joinpath('report.txt').open('a') as file_out:
                        file_out.write(value.parent.stem + '/' + value.name + '(' + str(counter) + '): ' + line)
                if not check_solver:
                    if line.lower().startswith('solver finished at'):
                        check_solver = True
            if not check_solver:
                with value.parents[2].joinpath('report.txt').open('a') as file_out:
                    file_out.write(value.parent.stem + '/' + value.name + ': ' + "missing 'Solver finished at'\n")
"""

"""
Если при анализе результатов Memory Working Set Peak речь идет действительно о максимальной значении
Memory Working Set Peak, то в функции max_total_and_memory необходимо изменить переменную memory на список,
а с помощью return возвращать max(memory), функция будет выглядеть следующим образом: 

def max_total_and_memory(file):
    memory = []
    total = 0
    for line in file:
        if line.lower().find('memory working set current') != -1:
            memory.append(float(line.lower().split()[-2]))
        if line.lower().find('mesh::bricks: total=') != -1:
            total = float(line.lower().split()[1].split('=')[1])
    return max(memory), total
    
Но если обратить внимание на файл reference_result.txt, то видимо при сравнении использовалось не максимальное
значение Memory Working Set Peak, а его последнее значение с файла *.stdout
"""


def max_total_and_memory(file):  # Поиск максимального значения Memory Working Set Peak и Total в файле
    memory = 0
    total = 0
    for line in file:
        if line.lower().find('memory working set current') != -1:
            memory = float(line.lower().split()[-2])
        if line.lower().find('mesh::bricks: total=') != -1:
            total = float(line.lower().split()[1].split('=')[1])
    return memory, total


"""
С функцией comparison_of_results аналогично: можно было бы разбить ее на 2 функции
Одна функция работала бы с Memory Working Set Peak
Вторая функция работала бы с Total из строки MESH::Bricks

Но было решено оставить цельную функцию comparison_of_results, чтобы не приходилось открывать
файлы из ft_run и ft_reference и пробегать по ним дважды, когда можно искать в файле параллельно 
информацию о Memory Working Set Peak и информацию о Total из MESH::Bricks
"""


def comparison_of_results(path):  # Сравнивает результаты файлов (Memory Working Set Peak, Total из MESH::Bricks...)
    files_ft_run = path.rglob('ft_run/**/*.stdout')
    files_ft_reference = path.rglob('ft_reference/**/*.stdout')
    for ft_run, ft_reference in zip(files_ft_run, files_ft_reference):
        with ft_run.open() as file_input_ft_run, ft_reference.open() as file_input_ft_reference:
            y_max, y_total = max_total_and_memory(file_input_ft_run)
            x_max, x_total = max_total_and_memory(file_input_ft_reference)
            if not 0.5 * x_max <= y_max <= 1.5 * x_max:
                with ft_run.parents[2].joinpath('report.txt').open('a') as file_out:
                    file_out.write(
                        ft_run.parent.stem + '/' + ft_run.name + ': ' + "different 'Memory Working Set Peak' (ft_run=" + str(
                            y_max)
                        + ', ft_reference=' + str(x_max) + ', rel.diff=' + str(round(y_max / x_max - 1, 2))
                        + ', criterion=0.5)\n')
            if not 0.9 * x_total <= y_total <= 1.1 * x_total:
                with ft_run.parents[2].joinpath('report.txt').open('a') as file_out:
                    file_out.write(
                        ft_run.parent.stem + '/' + ft_run.name + ': ' + "different 'Total' of bricks (ft_run=" + str(
                            y_total)
                        + ', ft_reference=' + str(x_total) + ', rel.diff=' + str(round(y_total / x_total - 1, 2))
                        + ', criterion=0.1)\n')


glob_paths = Path().glob("**/task1/logs/**")
for i_path in glob_paths:
    if len(i_path.parts) == 4:  # Именно столько имеют подкаталогов (до task1 включительно) ключевые каталоги ft_run/ft_references
        if exist_folders(i_path):  # Проверка на существование каталогов ft_run/ft_references
            if fileset_equality(i_path):  # Проверка на совпадение набора файлов ft_run и ft_references
                # solver_error_check(i_path)  # Проверка файлов ft_run на отсутствие "error" и присутствия "Solver finished at"
                solver_check(i_path)  # Проверка файлов ft_run на присутствие "Solver finished at"
                error_check(i_path)  # Проверка файлов ft_run на отсутствие "error"
                comparison_of_results(i_path)  # Сравнение результатов файлов (Memory Working Set Peak, Total из MESH::Bricks...)

        # Вывод для каждого теста вердикта в STDOUT

        if i_path.joinpath('report.txt').exists():
            with i_path.joinpath('report.txt').open() as file_report:
                print('FAIL: ' + i_path.relative_to('task1/logs/').as_posix() + '/')
                for i_line in sorted(file_report):
                    print(i_line.strip())
        else:
            print('OK: ' + i_path.relative_to('task1/logs/').as_posix() + '/')
