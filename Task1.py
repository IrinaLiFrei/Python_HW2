# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input('Enter any number: ')
num_list1 = list(num)
num_list2 = [s for s in num_list1 if s.isdigit()]
num_list3 = list(map(int,(num_list2)))
# print(num_list3)

sum = 0
for i in num_list3:
    sum = sum + i
print(f'Sum of all digits in the number entered = {sum}')