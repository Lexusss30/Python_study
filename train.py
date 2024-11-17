#Алгоритмические задачи со счётными циклами
# cube = int(input("Введите число: "))
# for number in range(1, cube//2 + 1):
    # number *= 2
    # print(number, "** 3 =", number ** 3)

# n = int(input("Введите число: "))
# for number in range(1, n//2 + n % 2 + 1):
#     number = number * 2 - 1
#     print(number, "** 2 =", number ** 2)

#Функция range: start, stop, step
# n = int(input("Введите число: "))
# for number in range(1,n,2):
#     print(number, "** 3 =", number ** 3)

# chair = int(input("Введите количество кресел: "))
# for number in range(1, chair + 1, 5):
#     print("Номер стула:", number)

# wake_up = int(input("Во сколько проснулся: "))
# water = 0 
# total_calories = 0
# for hour in range(wake_up,23,3):
#     water += 1
#     calories = int(input("Сколько калорий съедено: "))
#     total_calories += calories
# print("Количество съеденных калорий:", total_calories, "Количество выпитой воды:", water)

#8.4 Отрицательный шаг в функции range
# second = int(input("Введите кол-во секунд: "))
# for sec in range(second, 0,-1):
#     print(sec)
# print("Я иду искать!")

# second = int(input("Сколько секунд считать? "))
# even_n = second - second % 2  
# for i in range(even_n, 0, -2):
#     print(i)
# print("Я иду искать!")

#8.6 Практическая работа
# print("Информация о запасах гречки:")
# stocks = 100
# mounths = 0
# for reserve in range(stocks, -4, -4):
#     mounths += 1
#     print("Через", mounths - 1, "месяц(ев):", reserve , "кг гречки в запасе")
# print("Запасы гречки закончились.")

# quantity_debtors = int(input("Количество должников в банке: "))
# total_duty = 0
# for arrears in range(0,quantity_debtors + 1,5):
#     print("Должник с номером: ", arrears)
#     duty = int(input("Сколько вы должны банку? "))
#     total_duty += duty
# print("Общая сумма долга:", total_duty)

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

# start = int(input("Введите начало отрезка: "))
# stop = int(input("Введите конец отрезка: "))
# step = int(input("Ввдетие шаг(отрицательный): "))
# answer = 0
# if step >= 0:
#     step *= - 1
# for count in range(start,stop - 1,step):
#     answer = (count ** 3 + 2 * count ** 2 - 4 * count + 1)
#     print (f"В точке {count} функция равно {answer}")

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
# answer = "Да, конечно, сделал."
# while True:
#     security_question = input("Задание за вчера сделано? ")
#     if (answer == security_question):
#         break

# username = input("Как тебя зовут? ")
# print(f"{username}, купи слона!")
# while True:
#     user_answer = input("")
#     print(f"Все говорят {user_answer}, а ты купи слона")

# text = input("Введите текст: ")
# for symbol in text:
#     print(symbol * 3)

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











