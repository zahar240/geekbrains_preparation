""" Программа хранит в двух переменных курс доллара и евро. В первой переменной у вас 
хранится стоимость одного евро в рублях, во второй - стоимость одного доллара в рублях. 
Вы спрашиваете у пользователя, сколько рублей он хочет сконвертировать, получаете это число и считаете. 
Результат надо вывести на страницу с помощью alert(для JS). """

import math

dollar_course = 70
evro_course = 85

sum_converter = int(input("Какую сумму конвертировать: "))

dol_conv = sum_converter / dollar_course
evro_conv = sum_converter / evro_course

# Без округления
print("Доллары: " + str(sum_converter / dollar_course) + "; " + "Евро: " + str(sum_converter / evro_course))
print("Доллары:", str(sum_converter / dollar_course), "; ", "Евро:", str(sum_converter / evro_course))
print("Доллары: " + str(dol_conv) + "; " + "Евро: " + str(evro_conv))
print("Доллары:", dol_conv, "; ", "Евро:", evro_conv)
print("Доллары: %s Евро: %s" %(dol_conv, evro_conv))

# Округление с помощью функций: trunc(), floor(), ceil() модуля math
print("Доллары:", math.trunc(dol_conv), "; ", "Евро:", math.trunc(evro_conv))

print("Доллары:", math.floor(dol_conv), "; ", "Евро:", math.floor(evro_conv))

print("Доллары:", math.ceil(dol_conv), "; ", "Евро:", math.ceil(evro_conv))

# Округление с помощью функции round()
print("Доллары:", round(dol_conv), "; ", "Евро:", round(evro_conv))
print("Доллары:", round(dol_conv, 2), "; ", "Евро:", round(evro_conv, 4))
