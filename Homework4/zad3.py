import numpy as np

PATH_A='Homework4/Zadanie_3_macierz_A.csv'
PATH_B='Homework4/Zadanie_3_macierz_B.csv'

A = np.genfromtxt(PATH_A, delimiter=',')
B = np.genfromtxt(PATH_B, delimiter=',')
print('A: \n', A)
print('B: \n', B)
arr = []

for row_A in A:
    row = []
    for row_B in B:
        row.append(np.sum(row_A*row_B)/(np.sqrt(np.sum((row_A)**2)) * np.sqrt(np.sum((row_B**2)))))
    arr.append(row)

print(np.array(arr))