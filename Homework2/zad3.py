pow2 = lambda x: x*x
pow3 = lambda x: x*x*x

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pow2_list = []
pow3_list = []

for element in my_list:
    pow2_list.append(pow2(element))
    pow3_list.append(pow3(element))

print (pow2_list)
print (pow3_list)