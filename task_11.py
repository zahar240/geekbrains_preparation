"""2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 10, но меньше 100.
После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4."""

number = int(input("Введите число: "))

while number <= 10 or number >= 100:
    if number <= 10:
        print("Нужно больше 10")
        number = int(input("Введите число: "))
    elif number >= 100:
        print("Нужно меньше 100")
        number = int(input("Введите число: "))  
print(number ** 2)