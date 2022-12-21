# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а также сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44] 
# (1 + (1/1) ** 1 = 2; 1 + (1/2) ** 2 = 2,25; 1 + (1/3) **3 = 2,37; 1 + (1/4) **4)
# Сумма 9.06

num = int(input('Enter any number: '))
num_list = []
num_2 = 1
for i in range(num):
    i = (1 + (1/num_2)) ** num_2
    num_list.append(round(i, 2))
    num_2+=1
print(num_list)

print(f'Sum of all the elements in list = {sum(num_list)}')
