# Упорядочить по возрастанию элементы каждой строки матрицы размером n х m.

input_file = "MatsaevDR_UB51_vvod.txt"
output_file = "MatsaevDR_UB51_vivod.txt"

def sort(matrix):
    for row in matrix:
        row.sort()

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

sort(matrix)

print(f"Запись результатов в файл: '{output_file}'")
with open(output_file, 'w', encoding='utf-8') as outfile:
    for row in matrix:
        outfile.write(" ".join(map(str, row)) + "\n")
print("Результат успешно записан")