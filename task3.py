# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

import random

my_list = []
for i in range(5):
    my_list.append(random.randint(1, 100))
print(my_list)

new_list = random.sample(my_list, len(my_list))
print(new_list)

