import numpy as np

PATH='Homework4/Zadanie_1.csv'

np_array = np.genfromtxt(PATH, delimiter=';')


print('a) Number of records: ', np_array.size)
print('b) Number of rows and columns: ', np_array.shape)

np_array_masked = np.ma.masked_invalid(np_array)

print('c) Median: ', np.median(np_array_masked))
print('   Mean: ', np.mean(np_array_masked))
print('   Variance: ', np.var(np_array_masked))

np_array = np_array[np.logical_not(np.isnan(np_array))]

print('d) Median: ', np.median(np_array))
print('   Mean: ', np.mean(np_array))
print('   Variance: ', np.var(np_array))