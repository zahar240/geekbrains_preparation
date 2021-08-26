"""Сделать игру с двумя игроками и бесконечным числом попыток. Сделайте возможность выйти из игры по желанию одного из игроков."""

import math

number = input("Введите число: ")

#print(type(number))
print(math.isnan(number))

sum_number = 0
if int(number) < 0:
    print("Нужно было ввести положительное число!")
elif math.isnan(number):
    print("Нужно было ввести число!")
else:
    for i in range(0, int(number) + 1):
        if i <= int(number) + 1:
            sum_number += i
            print(i," ",sum_number)
            i += 1