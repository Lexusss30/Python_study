#Алгоритмические задачи со счётными циклами

#Задача 1
# cube = int(input("Введите число: "))
# for number in range(1, cube//2 + 1):
    # number *= 2
    # print(number, "** 3 =", number ** 3)

#Задача 2
# n = int(input("Введите число: "))
# for number in range(1, n//2 + n % 2 + 1):
#     number = number * 2 - 1
#     print(number, "** 2 =", number ** 2)

#Функция range: start, stop, step

#Задача 1
# n = int(input("Введите число: "))
# for number in range(1,n,2):
#     print(number, "** 3 =", number ** 3)

#Задача 2
# chair = int(input("Введите количество кресел: "))
# for number in range(1, chair + 1, 5):
#     print("Номер стула:", number)

#Задача 3
# wake_up = int(input("Во сколько проснулся: "))
# water = 0 
# total_calories = 0
# for hour in range(wake_up,23,3):
#     water += 1
#     calories = int(input("Сколько калорий съедено: "))
#     total_calories += calories
# print("Количество съеденных калорий:", total_calories, "Количество выпитой воды:", water)

#8.4 Отрицательный шаг в функции range

#Задача 1
# second = int(input("Введите кол-во секунд: "))
# for sec in range(second, 0,-1):
#     print(sec)
# print("Я иду искать!")

#Задача 2
# second = int(input("Сколько секунд считать? "))
# even_n = second - second % 2  
# for i in range(even_n, 0, -2):
#     print(i)
# print("Я иду искать!")

#8.6 Практическая работа

#Задача 1
# print("Информация о запасах гречки:")
# stocks = 100
# mounths = 0
# for reserve in range(stocks, -4, -4):
#     mounths += 1
#     print("Через", mounths - 1, "месяц(ев):", reserve , "кг гречки в запасе")
# print("Запасы гречки закончились.")

#Задача 2
# quantity_debtors = int(input("Количество должников в банке: "))
# total_duty = 0
# for arrears in range(0,quantity_debtors + 1,5):
#     print("Должник с номером: ", arrears)
#     duty = int(input("Сколько вы должны банку? "))
#     total_duty += duty
# print("Общая сумма долга:", total_duty)

#Задача 3
# timer = int(input("Введите время для обратного отсчёта: "))
# print("Таймер установлен на:", timer, "секунд")
# for reverse_timer in range(timer, 0, -1):
#     print("Осталось:", reverse_timer, "секунд")
#     close = int(input("Введите 1, если еда готова, или 0, чтобы продолжить: "))
#     if close == 1: 
#         print("Ваша еда готова, можете забрать!", "Таймер был прерван на", reverse_timer, "секундах.")
#         break
# else:
#     print("Ваша еда готова. Осторожно, горячo!")

#Задача 4
# start = int(input("Введите начало отрезка: "))
# stop = int(input("Введите конец отрезка: "))
# step = int(input("Ввдетие шаг(отрицательный): "))
# answer = 0
# if step >= 0:
#     step *= - 1
# for count in range(start,stop - 1,step):
#     answer = (count ** 3 + 2 * count ** 2 - 4 * count + 1)
#     print (f"В точке {count} функция равно {answer}")

#Задача 5
# educational_grant = int(input("Введите ежемесячную стипендию: "))
# expenses = int(input("Введите ежемесячные расходы: "))
# mouths = 0
# helps = 0
# flaw = expenses - educational_grant
# print(f"1-й месяц: траты {expenses} рублей, не хватает {flaw} рублей.")
# helps += flaw
# for i in range(2, 10 + 1):
#     mouths += 1
#     expenses += expenses * 3 // 100
#     flaw = expenses - educational_grant 
#     print(f"{mouths}-й месяц: траты {expenses} рублей, не хватает {flaw} рублей.")
#     helps += flaw 
# print("Сумма денег, которую необходимо получить у родителей:", helps)

# 8.7 Итоги пройденных тем. Проверьте себя

#Задача 1
# boys = int(input('Введите кол-во мальчиков: '))
# girls = int(input('Введите кол-во девочек: '))
# answer = ''
# if (boys > 2 * girls) or (girls > 2 * boys):
#     print('Нет решения')
# elif boys >= girls:
#     k = boys - girls
#     for bgb in range(k):
#         answer += 'BGB'
#     for bg in range(girls - k):
#         answer += 'BG'
# else:
#     k = girls - boys
#     for gbg in range(k):
#         answer += 'GBG'
#     for gb in range(boys - k):
#         answer += 'GB'

# print(answer)

#Сравнение строк

#Задача 1
# answer = "Да, конечно, сделал."
# while True:
#     security_question = input("Задание за вчера сделано? ")
#     if (answer == security_question):
#         break

#Задача 2
# username = input("Как тебя зовут? ")
# print(f"{username}, купи слона!")
# while True:
#     user_answer = input("")
#     print(f"Все говорят {user_answer}, а ты купи слона")

#Задача 3
# text = input("Введите текст: ")
# for symbol in text:
#     print(symbol * 3)

#Задача 4
# text = input("Введите текст: ")
# capital_letter = 0
# small_letter = 0
# for symbol in text:
#     if symbol == "ы":
#         small_letter += 1
#     elif symbol == "Ы":
#         capital_letter += 1 
# print(f"Больших букв Ы: {capital_letter}")
# print(f"Маленьких букв ы: {small_letter}")

#9.6 Практическая работа

#Задача 1
# words_answer = 0
# for _ in range(10):
#     word = input("Введите слово: ").lower()
#     if word == "Карамба" or word == "карамба":
#         words_answer += 1
# print("Количество правильных ответов =" , words_answer)

#Задача 2
# rows = int(input("Введите количество рядов: "))
# seats = int(input("Введите количество сидений в ряде: "))
# metrs = int(input("Введите количество метров между рядами: "))
# print("")
# print("Сцена")
# print("")
# for i in range(rows + 1):
#     rows = "=" * seats
#     rows = rows + "*" * metrs + rows
#     print(rows)

#Задача 3
# coordinate_x = 8
# coordinate_y = 10
# while True:
#     print(f"[Программа]: Марсоход находится на позиции {coordinate_x},{coordinate_y}, введите команду:")
#     operator = input("[Оператор]: ")
#     if operator == "W" and coordinate_y != 15:
#         coordinate_y += 1
#     elif operator == "S" and coordinate_y != 0:
#         coordinate_y -= 1
#     elif operator == "D" and coordinate_x != 15:
#         coordinate_x += 1
#     elif operator == "A" and coordinate_x != 0:
#         coordinate_x -= 1

#Задача 4
# text = input("Введите текст: ")
# summ = 0 
# long_word = 0 
# for symbol in text: 
#     if symbol != " ": 
#         summ += 1
#         if summ > long_word: 
#             long_word = summ 
#     else: 
#         summ = 0 
# print(f"Самое длинное слово, {long_word} букв.")

#Задача 5
# stable = input("Введите 10 стойл в одну строку. a — свободное стойло, b — занятое: ")
# milk = 0
# count = 0 
# for symbol in stable:
#     count += 1
#     if symbol == "b":
#         milk += count * 2
#     else:
#         milk += count * 0   
# print(f"\nПроизведено молока за день: {milk}")

#10.1 Работа со вложенными циклами

#Задача 1 
# for fist_multiplier in range(1,10):
#     for second_multiplier in range(1,10):
#         print(fist_multiplier * second_multiplier, end = "\t")
#     print()

#Задача 2
# number = int(input("Введите число: "))
# for row in range(number + 1):
#     for cow in range(number + 1):
#         print(row + cow, end = "\t")
#     print()

#Задача 3
# for negative_number in range(10):
#     for positive_number in range(10):
#         print(negative_number - positive_number, end = "\t")
#     print()

#10.2 Использование if во вложенных циклах

#Задача 1 
# size = int(input("Введите размер матрицы: "))
# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if row % 2 == 0:
#             print(row, end = " ")
#         else:
#             print(col, end = " ")
#     print()

#Задача 2 
# size = int(input("Введите размер матрицы: "))
# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if col % 3 == 0:
#             print(col, end = "\t")
#         else:
#             print(row, end = "\t")
#     print()

#10.3 Работа с двумя счётчиками в условном операторе

#Задача 1
# for row in range(20):
#     for col in range(30):
#         if row == 0:
#             print("-", end = " ")
#         elif col == 0:
#             print("|", end = " ")
#         elif col == 29:
#             print("|", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

#Задача 2 
# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end = " ")
#         elif col == row + 30:
#             print("\\", end = " ")
#         elif col == - row + 19: 
#             print("/", end = " ")
#         elif col == 24:
#             print("|", end = " ")
#         else:
#             print(" ", end = " ")
#     print()

#Задача 3
# size = int(input("Введите размер матрицы: "))
# for row in range(size):
#     for col in range(size):
#         num_col = (size - 1) - row
#         if num_col > col:
#             print(0, end = "\t")
#         elif num_col == col:
#             print(1, end = "\t")
#         else:
#             print(2, end = "\t")
#     print()

#10.4 Решение задач с помощью вложенных циклов

#Задача 1
# people = int(input("Введите количество людей в очереди: "))
# for hour in range(people + 1):
#     print(f"Идет {hour} час")
#     for number in range(hour, people):
#         print(f"Номер в очереди: {number} ")
#     print()
# print("Очередь обслужена.")

#Задача 2
# digit = int(input("Количество чисел в последовательности: "))
# cipher_count = 0
# for _ in range(digit):
#     number = int(input("Введите число: "))
#     while number:
#         if number % 10 > 5:
#             cipher_count += 1
#         number //= 10

# print("Количество чисел больше 5 в последовательности:", cipher_count)

#Задача 3 
# size = int(input("Введите размер таблицы: "))
# for start in range(size + 1):
#     for num in range(start, size + 1):
#         print(num, end = "\t")
#     print()

#10.6 Практическая работа

#Задача 1
# for row in range(6):
#    for col in range(0, 12, 2):
#         print(row + col , end = "\t")
#    print()

#Задача 2
# number = int(input("Введите число: "))
# for row in range(1, number + 1):
#     for col in range(row):
#         print(row, end = " ")
#     print()

#Задача 3
# length = int(input("Введите длинну: "))
# height = int(input("Введите высоту: "))
# for row in range(length):
#     for col in range(height):
#         if col == 0 or col == height - 1:
#             print("|", end = " ")
#         elif row == 0 or row == length - 1:
#             print("-", end = " ")
#         else:
#             print(" ", end = " ")
#     print()


#Задача 4
# list_numbers = int(input("Количество чисел в последовательности: "))
# simple_number = 0
# for nums in range(list_numbers):
#     number = int(input("Введите число: "))
#     if number == 1 or number == 0:
#         simple_number -= 1 
#     for element in range(2, number):
#         if number % element == 0:
#             break
#     else:
#         simple_number += 1
# print()
# print("Простых чисел в последовательности:", simple_number)

#Задача 5
# quantity_numbers = int(input("Количество чисел в последовательности: "))
# max_summ = 0
# numeric = 0
# for elements in range(quantity_numbers):
#     number = int(input("Введите число: "))
#     summ = 0
#     temporary_number = number
#     while number > 0:
#         summ += number % 10
#         number //= 10   
#     if summ > max_summ:
#         max_summ = summ
#         numeric = temporary_number
# print(f"Число {numeric} имеет максимальную сумму цифр: {max_summ}")

#Задача 6
# height = int(input("Введите высоту пирамиды: "))
# size = (2 * height) - 2
# for row in range(0, height):
#     for col in range(0, size):
#         print(end = " ")
#     size = size - 1 
#     for el in range(0, row + 1):
#         print("#", end = " ")
#     print(" ")

#11.2 Ввод вещественного числа. Функции float и round

#Задача 1
# bet = int(input("Сколько ставим? "))
# coefficient = float(input("Какой коэффициент? "))

# win = round(bet * coefficient, 2)
# print(f"Потенциальный выигрыш: {win}")

#Задача 2 
# age = int(input("Сколько лет? "))
# temperature = float(input("Какая температура? "))

# present = round(age * 1.5 * temperature, 2)
# print(f"Сумма подарка сыну составит: {present} рублей")

#11.3 Приведение типов между int и float

#Задача 1 
# money = int(input("Сколько у вас чатлов? "))
# conversion = round(money / 2200, 2)
# print(f"Вы успешно перевели валюту в CR. У вас {conversion} CR")
# print(f"Можно купить кораблей: {money // 1100}")


#11.4 Математические функции. Работа с модулем math

#Задача 1 
# import math

# a = float(input("Введите длину стороны a: ")) 
# b = float(input("Введите длину стороны b: ")) 
# c = float(input("Введите длину стороны c: ")) 

# p = (a + b + c) / 2
# S = math.sqrt(p * (p - a)*(p - b)*(p - c))
# print(f"Площадь треугольника по формуле Герона = {S}")

#Задача 2 
# import math

# print("Добро пожаловать, положение персонажа: 0,0")
# distance = int(input("Введите пройденное расстояние: "))
# rotation_angle = float(input("Введите угол поворота: "))

# coordinate_x = distance * math.cos(rotation_angle)
# coordinate_y = distance * math.sin(rotation_angle)
# print(f"Местоположение персонажа: {coordinate_x}, {coordinate_y}")

#Задача 3 
# import math

# user_number = float(input("Введите число: "))
# print(math.floor(user_number))
# print(math.ceil(user_number))
# print(abs(user_number))
# print(math.sqrt(user_number))
# print(math.exp(user_number))
# print(math.log(user_number))
# print(math.log2(user_number))
# print(math.log10(user_number))
# print(math.sin(user_number), math.cos(user_number))
# if user_number >= 0:
#     print(math.factorial(int(user_number)))
# else:
#     print("Факториал отрицательного числа не определен")

#11.6 Практическая работа

#Задача 1 
# price = int(input("Стоимость покупки в евро: "))
# usd = 60.87
# euro_rub = 1.25 * usd
# price_rub = round(price * euro_rub, 4)
# print(f"Стоимость в рублях: {price_rub}")

#Альтернативное решение (Задача 1)
# price = int(input("Стоимость покупки в евро: "))
# usd = 60.87
# euro = 1.25
# price_rub = price * euro * usd
# print(f"Стоимость в рублях: {price_rub}")

#Задача 2
# import math

# quantity = int(input("Введите количество чисел: "))
# for _ in range(quantity):
#     number = float(input("Введите число: "))
#     if number <= 0:
#         number = math.floor(number)
#         print(f"x = {number} exp(x) = {math.exp(number)}")
#     else:
#         number = math.ceil(number)
#         print(f"x = {number} log(x) = {math.log(number)}")

#Задача 3
# import math

# file_size = int(input("Укажите размер файла для скачивания: "))
# speed = int(input("Какова скорость вашего соединения: "))
# download = 0
# second = 0
# while download < file_size:
#     second = second + 1
#     download = min(download + speed, file_size)
#     percent = round(download / file_size * 100)
#     print(f"Прошло {second} сек. Скачано {download} из {file_size} Мб ({percent} %)")

#Задача 4 
# number = float(input("Введите число: ")) 
# print("Первая цифра после десятичной точки:", int(number * 10) % 10)

#Задача 5
# import math 

# radius = float(input('Введдите радиус планеты: ')) 
# earth = 1.08321 * 10 ** 12 
# volume = 4/3 * math.pi * radius**3 
# if earth > volume: 
#   print("Обьем планеты земля больше в ", round(earth / volume, 3), "раз" ) 
# if earth < volume: 
#   print("Обьем планеты земля меньше в", round(volume / earth, 3), "раз" )

#12.2 Функции и их вызов

#Задача 1 
# def greeting():
#     print("Привет!")
#     print("Добро пожаловать!")
 
# while True:
#     user_choise = input("Зайдёте? Да/Нет: ")
#     if user_choise == "Да":
#         greeting()
#         print("Следующий.\n")
#     elif user_choise == "Нет":
#         print("Следующий.\n")

#Задача 2 
# def food_counting():
#     a = int(input())
#     b = int(input())
#     print("Всего", a+b, "шт.")

# print("Сколько мешков рыбы и мяса?")
# food_counting()
# print("Сколько вёдер воды и молока?")
# food_counting()
# print("Сколько вёдер воды и молока?")
# food_counting()

#Задача 3
# def data_request():
#     surname = input("Фамилия: ")
#     name = input("Имя: ")
#     street = input("Улица: ")
#     house = int(input("Дома: "))
#     print()

# data_request()
# data_request()
# data_request()

#12.3 Функции с одним параметром

#Задача 1
# def about_water(price):
#     print("Название: КлирВотер\n"
#           "Производитель: ВодЗавод\n"
#           "Цена:", price)

# for _ in range(3):
#     price_of_water = int(input("Введите цену "))
#     about_water(price_of_water)

#Задача 2
# import math

# def sphere_area(radius):
#     print(4 * math.pi * radius ** 2)

# def sphere_volume(radius):
#     print(4 / 3 * math.pi * radius ** 3)

# radius_of_planet = float(input("Введите радиус планеты: "))
# sphere_area(radius_of_planet)
# sphere_volume(radius_of_planet)

#Задача 3
# def is_prime(number):
#     if number < 2:
#         print("Не простое")
#     else:
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 print("Не простое")
#                 break
#         else:
#             print("Простое")

# n = int(input("Введите количество чисел в последовательности: "))
# for i in range(n):
#     new_number = int(input("Введите число: "))
#     is_prime(new_number)

#12.4 Функции с несколькими параметрами

#Задача 1
# import math

# def mean_calc(x, y):
#     sum_of_numbers, count_of_numbers = 0, 0
#     for i in range(x, y + 1):
#         sum_of_numbers += i
#         count_of_numbers += 1
#     print("Среднее:", round(sum_of_numbers / count_of_numbers, 2))
# a = int(input("Введите левую границу: "))
# b = int(input("Введите правую границу: "))

# mean_calc(a, b)

#Задача 2
# def print_all_info(surname, name, country, city, street, house, flat):
#     print("Фамилия:", surname)
#     print("Имя:", name)
#     print("Страна проживания:", country)
#     print("Город:", city)
#     print("Улица:", street)
#     print("Номер дома:", house)
#     print("Номер квартиры:", flat)

# user_surname = input("Введите фамилию: ")
# user_name = input("Введите имя: ")
# user_street = input("Введите улицу: ")
# user_house = input("Введите номер дома: ")

# for _ in range(3):
#     user_surname = input("Введите фамилию: ")
#     user_name = input("Введите имя: ")
#     user_country = input("Введите страну проживания: ")
#     user_city = input("Введите город: ")
#     user_street = input("Введите улицу: ")
#     user_house = input("Введите номер дома: ")
#     user_flat = input("Введите номер квартиры: ")

# print_all_info(user_surname, user_name, user_country, user_city, user_street, user_house, user_flat)

#Задача 3
# import math

# def my_distance(x, y):
#     distance = math.sqrt(x ** 2 + y ** 2)
#     print(distance)


# def their_distance(x_1, x_2, y_1, y_2):
#     distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
#     print(distance)


# user_choice = int(input("Найти расстояние от себя до точки (1) или найти расстояние между двумя произвольными точками (2)? "))
# if user_choice == 1:
#     target_x = float(input("Введите координату X цели: "))
#     target_y = float(input("Введите координату Y цели: "))
#     my_distance(target_x, target_y)
# elif user_choice == 2:
#     target_x_1 = float(input("Введите координату X цели 1: "))
#     target_y_1 = float(input("Введите координату Y цели 1: "))
#     target_x_2 = float(input("Введите координату X цели 2: "))
#     target_y_2 = float(input("Введите координату Y цели 2: "))
#     their_distance(target_x_1, target_x_2, target_y_1, target_y_2)
# else:
#     print("Ввод неверный")

#12.6 Практическая работа

#Задача 1 
# def summa_n(number):
#     sum_numbers = 0
#     for element in range(1, number + 1):
#         sum_numbers += element
#     print(f"Сумма чисел последовательности от 1 до {number} равна {sum_numbers}")

# number = int(input("Введите число: "))


# summa_n(number)


# summa_n()

#Задача 2
# def positive():
#     print("Положительное!")

# def negative():
#     print("Отрицательное!")

# def test():
#     number = int(input("Введите целое число: "))
#     if number > 0:
#         positive()
#     elif number == 0:
#         print("Введите любое число, кроме 0.")
#     else:
#         negative()


# test()

#Задача 3
# def summ_num(number): 
#     summ_num = 0 
#     while number > 0: 
#         summ_num += (number % 10) 
#         number //= 10 
#     print("Cумма цифр:",summ_num) 

# def max_num(number): 
#     max_num = -1 
#     while number > 0: 
#         if number % 10 > max_num: 
#             max_num = number % 10 
#         number //= 10 
#     print("Максимальная цифра этого числа:", max_num) 

# def min_num(number): 
#     min_num = 10 
#     while number > 0: 
#         if number % 10 < min_num: 
#             min_num = number % 10 
#         number //= 10 
#     print("Минимальная цифра этого числа:", min_num) 

# while True: 
#     number = int(input("Введите число: ")) 
#     action = int(input("Какое действие нужно сделать?\n1 - сумма цифр\n2 - максимальная цифра\n3 - минимальная цифра\n")) 
#     if action == 1: 
#         summ_num(number) 
#     elif action == 2: 
#         max_num(number) 
#     elif action == 3: 
#         min_num(number) 
#     else: 
#         print("Ошибка ввода.")

#Задача 4
# def count_letters():
#     number_count, letter_count = 0, 0
#     for symbol in text:
#         if symbol == letter:
#             letter_count += 1
#         elif symbol == str(number):
#             number_count += 1
#     print(f"\nКоличество цифр, {number}: {number_count}") 
#     print(f"Количество букв, {letter}: {letter_count}")

# text = input("Введите текст: ")
# number = int(input("Какую цифру ищем? "))
# letter = input("Какую букву ищём? ")

# count_letters()

#Задача 5
# from random import *

# def rock_paper_scissors(): 
#     user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ") 
#     computer_choice = choice(["камень", "ножницы", "бумага"]) 

#     if user_choice == computer_choice: 
#         print("Ничья!") 
#     elif (user_choice == "камень" and computer_choice == "ножницы") or (user_choice == "ножницы" and computer_choice == "бумага") or (user_choice == "бумага" and computer_choice == "камень"): 
#         print("Вы победили!") 
#     else: 
#         print("Вы проиграли!") 

# def guess_the_number(): 
#     number = randint(1, 100) 
#     guess = None 
#     attempts = 0 

#     while guess != number: 
#         guess = int(input("Угадайте число от 1 до 100: ")) 
#         attempts += 1 

#         if guess < number: 
#             print("Загаданное число больше.") 
#         elif guess > number: 
#             print("Загаданное число меньше.") 

#     print(f"Поздравляю! Вы угадали число за {attempts} попыток.") 

# def main_menu(): 
#     print("Добро пожаловать в игровое приложение!") 
#     print("Выберите игру:") 
#     print("1. Камень, ножницы, бумага") 
#     print("2. Угадай число") 

#     choice = input("Введите номер игры: ") 

#     if choice == "1": 
#         rock_paper_scissors() 
#     elif choice == "2": 
#         guess_the_number() 
#     else: 
#         print("Некорректный выбор.") 

# main_menu()


#13.2 Возврат значений из функций. Оператор return

#Задача 1 
# n = int(input("Введите N: "))

# def summa_n(n):
#     if n==0:
#         return n
#     else:
#         return(n+summa_n(n-1))
    
# y = summa_n(n)

# def summa_n(y):
#     if y==0:
#         return y
#     else:
#         return(y+summa_n(y-1)) 

# print(f"Сумма чисел от 1 до { n } = { summa_n(n) } ")
# print(f"Сумма чисел от 1 до { summa_n(n) } = { summa_n(y)}")

#Задача 2 
# def gcd(x, y):
#     if x > y:
#         small = y
#     else:
#         small = x
#     gcd_find = 1
#     for i in range(1, small + 1):
#         if (x % i == 0) and (y % i == 0):
#             gcd_find = i

#     return gcd_find


# first_number = int(input("Первое число: "))
# second_number = int(input("Второе число: "))
# print("НОД=", gcd(first_number, second_number))

#13.3 Представление вещественных чисел в программе

#Задача 1 
# x = 1 
# count = 0 
# while x != 0:
#     x /= 2 
#     count += 1 
#     print(x)
# print("Количество итераций:", count)

#Задача 2
 
# while True:
    # Если мы хотим проверить мантиссу - то нам нужно работать с числом как со строкой, поэтому float к input добавлять пока не будем
    # delta = input("Введите число в эксп. форме ")
    # проверка, что мантисса равна числу от 1 до 9
    # сперва получим отдельно часть строки до символа 'e'
    # mantissa = ''
    # for cipher in delta:
    #     if cipher == 'e':
    #         break
    #     mantissa += cipher
    # получив мантиссу - мы можем проверить, что она удовлетворяет условию (равна числу от 1 до 9)
    # так же мы сразу можем добавить проверку порядка - если порядок отрицательный, то введенное число будет меньше 1, это мы и проверим:
#     if 1 <= float(mantissa) <= 9 and float(delta) < 1:
#         print('Число введено верно!')
#         delta = float(delta)
#         break
#     else:
#         print("Число введено с ошибкой, мантисса всегда должна быть равна числу от 1 до 9, а порядок должен быть меньше нуля")


# start_number = 1
# count = 0
# while start_number <= 2:
#     start_number += delta
#     count += 1

# print("Кол-во прибавлений: ", count)

#13.4 Особенности работы с вещественными числами

#Задача 1
# import math

# def check_exponent_change(tax, new_tax):
#     total = tax + new_tax
#     degree_e_tax = math.floor(math.log10(tax))
#     degree_e_total = math.floor(math.log10(total))
#     if degree_e_tax != degree_e_total:
#         return True
#     else:
#         return False
 
# country_budget = float(input('Введите бюджет страны: '))
# budget_receipts = float(input('Введите новые поступления (налог): '))
# is_increase = check_exponent_change(country_budget, budget_receipts)

# if is_increase:
#     print('Бюджет увеличится')
# else:
#     print('Бюджет не изменится')

#Задача 2
# def eqv(a, b, c):
#     return abs((a + b) - c) <= 1e-15


# first = float(input("Введите первое число: "))
# second = float(input("Введите второе число: "))
# third = float(input("Введите третье число: "))
# print(eqv(first, second, third))


#13.6 Практическая работа

#Задача 1 

# def transformation(number):
#     degree = 0 
#     if number < 1:
#         while number < 1:
#             number *= 10
#             degree -= 1
#     elif number >= 10:
#         while number >= 10:
#             number /= 10
#             degree += 1
#         print("Формат плавающей точки x = ", number, "* 10 ** ", degree)

# number = float(input("Введите положительное число: "))
# if number > 0:
#     transformation(number)
# else:
#     print("Введите положительное число.")

#Задача 2 

# def max_of_two(first_numbers, second_numbers): 
#   return max(first_numbers, second_numbers) 

# def max_of_three (first_numbers, second_numbers, third_numbers): 
#   temporary = max_of_two(first_numbers, second_numbers) 
#   return max_of_two(temporary, third_numbers) 


# first_numbers = int(input("Введите первое число: ")) 
# second_numbers = int(input("Введите второе число: ")) 
# third_numbers = int(input("Введите третье: ")) 
# print("Самое большое число:", max_of_three(first_numbers, second_numbers, third_numbers )) 

#Задача 3

# def uspend(number):
#     temporary_number = 0
#     digit_number = 0  
#     while number > 0:
#         digit_number = number % 10
#         number //= 10
#         temporary_number *= 10
#         temporary_number = temporary_number + digit_number
#     return temporary_number

  
# number_n = int(input("Введите первое число: "))
# number_k = int(input("Введите второе число: "))
# print("Первое число наоборот:", uspend(number_n))
# print("Второе число наоборот:", uspend(number_k))


#Задача 4

# def count_numbers(number):
#     result = 0
#     while number > 0:
#         result += 1
#         number //= 10
#     return result

# def change_number(number, num_count):
#     last_digit = number % 10
#     first_digit = number // 10 ** (num_count - 1)
#     between_digits = number % 10 ** (num_count - 1) // 10
#     return last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit

# def main():
#     while True:
#         first_n = int(input("Введите первое число: "))
#         first_num_count = count_numbers(first_n)
#         if first_num_count < 3:
#             print("В первом числе меньше трёх цифр.")
#         else:
#             break

#     first_n = change_number(first_n, first_num_count)
#     print("Изменённое первое число:", first_n)

#     while True:
#         second_n = int(input("\nВведите второе число: "))
#         second_num_count = count_numbers(second_n)
#         if second_num_count < 4:
#             print("Во втором числе меньше четырёх цифр.")
#         else:
#             break

#     second_n = change_number(second_n, second_num_count)
#     print("\nИзменённое второе число:", second_n)
#     print("Сумма чисел:", first_n + second_n)

# main()

#Задача 5

# def amp_count(initial_amplitude, finite_amplitude):
#     count = 0
#     falloff_factor = 0.916
#     if initial_amplitude <= 0 or finite_amplitude <= 0:
#         print("Амплитуды должны быть положительными числами.")
#     elif initial_amplitude < finite_amplitude:
#         print("Начальная амплитуда должна быть больше конечной амплитуды.")
#     while initial_amplitude > finite_amplitude:
#         count += 1 
#         initial_amplitude *= falloff_factor
#     print(f"Маятник считается остановившимся через {count} колебаний.") 

# initial_amplitude = float(input("Введите начальную амплитуду: "))
# finite_amplitude = float(input("Введите амплитуду остановку: "))

# amp_count(initial_amplitude, finite_amplitude)

#2.1 Списки и их инициализация

#Задача 1 

# numbers = [3,7,5]

# while True:
#     number = int(input("Новое число: "))
#     numbers.append(number)
#     print("Текущий список чисел:", numbers)
#     for i in numbers:
#         print(i ** 2, i ** 3, i ** 4)

#Задача 2

# numbers = []
# for amount in range(0,100 + 1):
#     numbers.append(amount)
# print(numbers)

#Задача 3 

# count_of_workers = int(input("Кол-во сотрудников в офисе: "))
# workers_id = []
# for _ in range(count_of_workers):
#     worker_id = int(input("ID сотрудника: "))
#     workers_id.append(worker_id)

# search_id = int(input("Какого сотрудника ищем? "))

# search = False
# for id in workers_id:
#     if id == search_id:
#         search = True

# if search:
#     print("Сотрудник работает!")
# else:
#     print("Сотрудник не работает!")

# if search_id not in workers_id:  
#     print("Сотрудник не работает!")
# else:
#     print("Сотрудник работает!")

        