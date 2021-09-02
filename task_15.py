"""Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке."""

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for i in my_list_2:
    if i in my_list_1:
        my_list_1.remove(i)
print(my_list_1)

my_list_3 = list(set(my_list_1)-set(my_list_2))
print(my_list_1:= list(set(my_list_1)-set(my_list_2)))
print(my_list_1)