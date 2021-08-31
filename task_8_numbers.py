# Числовой ряд т 0 до 100
def number_0_100():
    number = 0
    while number <= 100:
        print(number)
        number += 1

#number_0_100()


# Числовой ряд от 0 до n
def number_0_n():
    number = 0
    n = int(input("Введите число: "))
    while number <= n:
        print(number)
        number += 1

#number_0_n() 

# Числовой ряд четных чисел от 0 до n
def even_number_0_n():
    number = 0
    n = int(input("Введите число: "))
    while number <= n:
        if number %2 == 0:
            print(number)
        number += 1

even_number_0_n()
