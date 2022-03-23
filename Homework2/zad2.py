dict_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
dict_list.sort(key=lambda d: d['make']) 
print('Sorted by make:' + str(dict_list))
dict_list.sort(key=lambda d: d['model']) 
print('Sorted by model:' + str(dict_list))
dict_list.sort(key=lambda d: d['color']) 
print('Sorted by color:' + str(dict_list))