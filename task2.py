import random
import numpy as np

number = int(input("Введите ранг матрицы "))
rows = number
cols = number
com = rows*cols
random_list = np.random.randint( -10, 10, com)
#создаем и заполняем матрицу

mrx = []
index_list = 0
for i in range(rows):
    mrx.append([])
    for j in range(cols):
        mrx[i].append(random_list[index_list])
        index_list += 1
print(mrx)

for i in range(rows):
    for j in range(cols):
        print(mrx[i][j], end=' ')
    print()

sum_diagonal = 0
for i in range(rows):
    sum_diagonal += mrx[i][i]

sum_antidiagonal = 0
for i in range(rows):
    sum_antidiagonal += mrx[i][-i - 1]

print(sum_diagonal)
print(sum_antidiagonal)
