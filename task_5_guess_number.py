"""Сделать игру с двумя игроками и бесконечным числом попыток. Сделайте возможность выйти из игры по желанию одного из игроков."""

number = int(input("Введите число: "))

sum_number = 0
for i in range(0, number + 1):
    if i <= number + 1:
        sum_number += i
        print(i," ",sum_number)
        i += 1