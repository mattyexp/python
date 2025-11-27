# Дана действительная матрица размером n х m, все элементы которой различны.
# В каждой строке выбирается элемент с наименьшим значением. Если число четное, то заменяется нулем,
# нечетное - единицей. Вывести на экран новую матрицу.

input_file = "MatsaevDR_UB51_vvod.txt"
output_file = "MatsaevDR_UB51_vivod.txt"

def processing(matrix):
    new_matrix = []

    for row in matrix:
        min_elem = row[0]
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

print(f"Чтение данных из файла: '{input_file}'")
with open(input_file, 'r', encoding='utf-8') as infile:
    n = int(infile.readline().strip())
    m = int(infile.readline().strip())

    matrix = []
    for i in range(n):
        addrow = infile.readline().strip()
        row = [int(s) for s in addrow.split()]
        matrix.append(row)
print("Данные успешно прочитаны")

new_matrix = processing(matrix)

print(f"Запись результатов в файл: '{output_file}'")
with open(output_file, 'w', encoding='utf-8') as outfile:
    for row in new_matrix:
        outfile.write(" ".join(map(str, row)) + "\n")
print("Результат успешно записан")
