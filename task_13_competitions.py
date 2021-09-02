print("Соревноваия по PYTHON")
count = int(input("Введите количество участников: "))
i = count
participants = []

while i > 0:
    name = input("Кто занял {} место: ".format(i))
    participants.append(name)
    i -= 1
print("В соревнованиях участвовали: ",participants)

participants.reverse()
top_3 = participants[:3]
print("Победители: {}. Поздравляем!".format(top_3))
