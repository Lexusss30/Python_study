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




