import numpy as np

PATH='Homework4/Zadanie_2.csv'

np_array = np.genfromtxt(PATH, delimiter=';')
w, v = np.linalg.eig(np_array)
print('a) Eigenvalues :', w)
print('   Eigenvectors :', v)

print('b) Inverse of matrix : ',np.linalg.inv(np_array))