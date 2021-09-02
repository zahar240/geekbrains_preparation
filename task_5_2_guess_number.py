import random

answer = random.randint(0, 100)

try_count = 0
while try_count <= 6:
    user_answer = int(input("Угадайте число от 1 до 100: "))
    try_count += 1
    print(f'Попытка № {try_count}')
    if user_answer == answer:
        print("Поздравляю, вы угадали!")
        break
    elif user_answer > answer:
        print("Вы ввели слишком большое число!")
    else:
        print("Вы ввели слишком маленькое число!")   
    
print("Конец игры!")
