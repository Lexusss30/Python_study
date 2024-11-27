# 1. Запросить у пользователя его возраст и определить, кем он 
# является: ребенком (0–2), подростком (12–18), взрослым 
# (18_60) или пенсионером (60– ...).

# num = int(input("ваш возраст? _"))
# if(num <=2):
#     print("ребенком")
# elif(num <=18):
#     print("подростком")
# elif(num <=60):
#     print("взрослым")
# else:
#     print("пенсионером")

# if
# if(num <=2):
#     print("ребенком")
# if(12<= num and num < 18):
#     print("подростком")
# if(18<= num and num <=60):
#     print("взрослым")
# if(num >= 60):
#     print("пенсионером")



#! Запросить у пользователя число от 0 до 9 и вывести ему 
#! спецсимвол, который расположен на этой клавише (1–!, 
#! 2–@, 3–# и т. д)



# Запросить у пользователя трехзначное и число и проверить, 
# есть ли в нем одинаковые цифры.

# num = int(input("123? _"))
# n3 = num % 10
# num = num // 10
# n2 = num % 10
# n1 = (num // 10) % 10
# print(n1,n2,n3)
# if(n1 == n2):
#     print("ок")
# elif(n1 == n3):
#     print("ок")
# elif(n2 == n3):
#     print("ок")

# boo = 1 == 1
# boo = 1 < 100
# boo = 1 > 100
# boo = 10 <= 100
# boo = 10 >= 10
# boo = 10 != 12
# boo = not(10 == 12)
# boo = not(True)

# hi

# print(boo)

# if (boo):
#     print("ok")



# num = 7
# if(num < 7):
#     print("ok")
#     print("num < 7")
# else:
#     print("не ok")
#     print("num >= 7")



# True или False или False = True
# True и False и False = False

# True или True или True = True
# True и True и True = True

# num = 6
# num2 = 4
# num3 = 8
# boo = num == 4 or num2 == 4
# print(boo)
# if(num == 4 or num2 == 5 or num3 > 6):
#     print("ok-ok-ok")