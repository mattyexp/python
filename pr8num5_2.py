# Дана действительная матрица размером n х m, все элементы которой различны.
# В каждой строке выбирается элемент с наименьшим значением. Если число четное, то заменяется нулем,
# нечетное - единицей. Вывести на экран новую матрицу.

def processing(matrix):
    new_matrix = []

    for row in matrix:
        min_elem= row[0]
        min_num = 0
        for i in range(1, len(row)):
            if row[i] < min_elem:
                min_elem = row[i]
                min_num = i
        if min_elem % 2 == 0:
            tochange = 0
        else:
            tochange = 1
        new_row = list(row)
        new_row[min_num] = tochange
        new_matrix.append(new_row)
    return new_matrix

n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

matrix = []
print(f"Введите элементы матрицы {n}x{m} построчно, разделяя пробелами:")
for i in range(n):
    addrow = input(f"Введите элементы {i+1}-й строки: ")
    row = [int(s) for s in addrow.split()]
    matrix.append(row)

print("\nИсходная матрица:")
for row in matrix:
    print(" ".join(map(str, row)))

new_matrix = processing(matrix)

print("\nНовая матрица после обработки:")
for row in new_matrix:
    print(" ".join(map(str, row)))