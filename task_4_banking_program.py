"""Пользователь вводит сумму вклада и процент, который будет начисляться ежегодно. 
Отобразить размер вклада поочередно на ближайшие 5 лет."""

sum_contribution = int(input("Введите сумму вклада: "))
value_percent = int(input("Введите значение процента: "))
deposit_term = int(input("Введите срок вклада: "))

ears = 1

while ears <= deposit_term:
    sum_contribution = sum_contribution * (1 + 1 / 100 * value_percent)
    ears += 1
print("Срок депозита:", str(deposit_term) + ",","Сумма вкада:", sum_contribution)
