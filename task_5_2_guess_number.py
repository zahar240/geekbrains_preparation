import random

answer = random.randint(0, 100)
user_answer = int(input("Угадайте число от 1 до 100: "))

try_count = 0
while try_count <= 6:
    if user_answer == answer:
        print("Поздравляю, вы угадали!")
    elif user_answer > answer:
        print("Вы ввели слишком большое число!")
    elif user_answer < answer:
        print("Вы ввели слишком маленькое число!")
    break    
    try_count += 1

print("Конец игры!")
#print(answer)