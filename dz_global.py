
# задачи на строки (str):
# Номер 2.1
# var1 = "22"
# var2 = "2.2"
# var3 = "2_000_002"
# print(var1,var2,var3,sep=",")
# print(f"{var1},{var2},{var3}",sep= ",")

# Задачи на условия (if else):
# Номер 9.1
# input("Введите данные: ")
# c = ""
# int_wer = c 
# if not int_wer:
#    print(False)
# else:
#    print(True)

# Номер 9.2
#x1 = int(input("Введите делимое: "))
#x2 = int(input("Введите делитель: "))
#if (x2!=0):
#    print(x1/x2)
#else:
#    print("Erorr")

# Номер 9.3
#x = int(input("Введите число: "))
#if (x%3==0):
#    print("Yes")
#else:
#    print("No")

# Номер 9.4
#x = int(input("Введите сумму покупки: "))
#if (x>20):
#   print ((x*0.65),'','- сумма покупки со скидкой в 35%')
#else:
#    print("Скидка только при покупке от 20 у.е")

# Номер 9.5
#x = int(input("Введите число: "))
#if (x<9 and x>=0):
#    print("Введёная переменная является цифрой десятичной системы счисления")
#else:
#    print("Введённая переменная не является цифрой десятичной системы счисления")

# Номер 9.6
# x = int(input("Введите число: "))
# if x==0:
#   print(x, "- это ноль")
# elif x==1:
#   print(x, "- это один")
# elif x==2:
#   print(x, "- это два")
# elif x==3:
#   print(x, "- это три")
# elif x==4:
#   print(x, "- это четыре")
# elif x==5:
#   print(x, "- это пять")
# elif x==6:
#   print(x, "- это шесть")
# elif x==7:
#   print(x, "- это семь")
# elif x==8:
#   print(x, "- это восемь")
# elif x==9:
#   print(x, "- это девять")
# else:
#    print("Введите цифру 10-й СС")

# Номер 9.8
# x = int(input("Введите денежную сумму: "))
# if (x<0 or x%2!=0):
#     print("Извините, но размен невозможен")
# else:
#     hun = x // 100
#     x = x%100
#     tens = x//10
#     x = x%10
#     two = x//2
# print(f"Размен: 100x{hun}, 10x{tens}, 2x{two}")

# Номер 9.9
# x = 130
# y = 25
# z = 70
# if x>y>z:
#    print(z)
# elif x<y<z:
#     print(x)
# else:
#     print(y)

# Номер 9.10
# x= int(input("x="))
# y= int(input("y="))
# if x>0 and y>0:
#     print("1 четверть")
# elif x<0 and y>0:
#     print("2 четверть")
# elif x<0 and y<0:
#     print("3 четверть")
# elif x>0 and y<0:
#     print("4 четверть")

# Номер 9.11
# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
# if a + b > c and a + c > b and b + c > a and min(a, min(b, c)) > 0:
#    if a == b == c:
#     print("Равносторонний треугольник")
#    elif a == b or a == c or b == c:
#     print("Равнобедренный треугольник")
#    else:
#     print("Разносторонний треугольник")
# else:
#  print("Такого треугольника не существует")
     
# Номер 9.12
# num = int(input("Введите число: "))
# if num<1 or num>12:
#     print("Ошибка, введите другое число")
# elif num==1:
#  print("Январь, зима")
# elif num==2:
#  print("Февраль, зима")
# elif num==3:
#  print("Март, весна")
# elif num==4:
#  print("Апрель, весна")
# elif num==5:
#  print("Май, весна")
# elif num==6:
#  print("Июнь, лето")
# elif num==7:
#  print("Июль, лето")
# elif num==8:
#  print("Август, лето")
# elif num==9:
#  print("Сентябрь, осень")
# elif num==10:
#  print("Октябрь, осень")
# elif num==11:
#  print("Ноябрь, осень")
# elif num==12:
#  print("Декабрь, зима")


# задачи на циклы (for, while):
# Упражнение 1
# while True:
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     print("Сумма чисел: ",num1+num2)
#     nz = input ("Нажмите Y или y для завершения программы:")
#     if (nz == "Y" or nz=="y"): break

# задачи на списки (array):
# Упражнение 1 
# list1 = [1,2,10,13,22,25,77,89,20,94,93]
# index = list1.index(20)
# list1[index]=200
# print(list1)

#Упражнение 3
# x=[1,2,3,4,5,6,7]
# for i in (x):
#    x=i**2
#    print("Квадрат числа",i,"=",x)

#Упражнение 4
# list = [2,5,20,10,11,33,20,55]
# list.remove(20)
# print(list)

#Упражнение 5
# x = [2,5,20,10,11,33,20,55]
# list.reverse(x)
# print(x)

#Упражнение 6
# list = ["Ann","Jane","Mike","Koul","Tito"]
# list.extend(["Max","Alex"])
# list.pop()
# print(list)

#Упражнение 7
# mat = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 80]
# ]
# for i in range(3):
#     for a in range(3):
#         print(mat[i][a], end = " ")
#     print()

#Упражнение 8
# numbers = []
# squares = []
# cubes = []
# start = 1
# end = 10
# for count in range (start, end+1) :
#     numbers.append (count)
#     squares.append (count**2)
#     cubes.append (count**3)
# print ("numbers: ",numbers)
# print ("squares: ",squares)
# print ("cubes : ",cubes)

#Упражнение 9
# list_txt = [11, 22, 33, 44, 55]
# print("Список чисел:",list_txt)
# for i in (list_txt):
#     if (i%2==0):
#      list_txt.remove(i)
# print("Список с нечётными числами:" ,list_txt)

#Упражнение 10
# list_a=[1, 2, 3, 4]
# list_b=[5, 6, 7, 8]
# summed_list= list_a+list_b
# print(summed_list)

#Упражнение 3.4
# list = ['Санкт', '+', 'Петербург']
# del list[1]
# list.insert(1,'-')
# print(list[0],list [1], list [2])

#Упражнение 3.5
# list_obw = ['a', '1', 'b', '2', 'c', '3']
# list_num = []
# list_letters = []
# list_obw.clear
# print(list_num,list_letters)



# задачи на словари:
#Упражнение 5.1
# d = {'1': 0, 2: 0, '3': 0}
# print(d)
# for key,value in d.items():
#     print(key,"-",value)

# Упражнение 5.2
# dict = {"имя": "Антон","возраст": 29, "пол": "мужской"}
# print(dict)

# задачи на рекурсию (function):
# Упражнение 1
# def fun(num):
#     if num==1:
#         return(num)
#     return fun (num-1)*num
# print(fun(3))

#Упражнение 2
# def fun(n,m):
#     if (m==1):
#         return(n)
#     if (m!=1):
#         return(n*fun(n,m-1))
# n = int(input("Введите число: "))
# m = int(input("Введите степень: "))
# print(fun(n,m))

#Упражнение 3
# def fun_garmonic(n):
#     if n == 1:
#         return 1
#     else:
#         return 1/n+fun_garmonic(n-1)
# print(fun_garmonic(5))

# Упражнение 4
# def fun_prog(a,b,c, res=[]):
#     if c == 0:
#      return res + [a]
#     else:
#        return fun_prog(a*b,b,c-1,res+[a])
# print(fun_prog(5,10,7))

#Упражнение 5 
# def fun_nod(a,b):
#     if b==0:
#      return a
#     if a>b:
#      return fun_nod(b,a%b)
#     else:
#      return fun_nod(a,b%a) 
# print(fun_nod(a,b))

#Упражнение 6
# def fun_rec(b):
#     if b < 1:
#         return 0
#     else:
#         return b + fun_rec(b - 2)
# print(fun_rec(5))

# Упражнение 1 (2 сссылка)
# def fun_summ(arr,index=0,sum=0):
#     if(len(arr)!= index):
#         return fun_summ(arr,index+1,sum+arr[index])
#     else:
#         return(sum)
# list_one=[3,7,8,10,11,23,0]
# print(fun_summ(list_one))
        
#Упражнение 2 (2 ссылка)
# def convertion(a,b):
#     cstr = "1B2C4B6O7E"
#     if a<b:
#         return cstr[a]
#     else:
#         return convertion(a//b,b)+cstr[a%b]
# print(convertion(1357,16))

#Упражнение 4 (2 ссылка)
# def factor(n):
#     if n<=1:
#         return(n)
#     else:
#         return n*factor(n-1)
# print(factor(7))

#Упражнение 5
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(7))

# задачи на классы (class)    
# Номер 1
# class Cars:
#     def __init__(self,manuf,model,year,aspeed):
#         self.manuf = manuf
#         self.model = model
#         self.year = year
#         self.aspeed = aspeed
#         print(manuf, model,year,aspeed,sep= ",")
#     def aspd(self, dist):
#      return self.aspeed * dist
  
# car_red = Cars ("BMW","X5M","2024 г.в", 150)
# print(car_red.aspd(200))

# Номер 2
# class Calc:
#    def __init__(self,num1,num2):
#       self.num1 = num1
#       self.num2 = num2
#    def sum (self,num1,num2):
#       return self.num1 + self.num2
#    def mins (self,num1,num2):
#       return self.num1 - self.num2
#    def ymn (self,num1,num2):
#       return self.num1 * self.num2
#    def dele (self,num1,num2):
#       return self.num1 // self.num2
# c = Calc(50,22)
# print ("Сложение = ", c.sum(50,22))
# print ("Вычитание = ",c.mins(50,22))
# print ("Умножение =",c.ymn(50,22))
# print ("Деление = ",c.dele(50,22))

# Номер 3 
# class Soda:
#     def __init__(self, ingredient=None):
#         self.ingredient = ingredient
 
#     def show_my_drink(self):
#         if self.ingredient:
#             print(f'Газировка и {self.ingredient}')
#         else:
#             print('Обычная газировка')
# drink = Soda ()
# drink2 = Soda("Цитрус")
# print(drink,drink2)



# Номер 4 
# class Nikola():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         if self.name == "Николай":
#             self.name = name
#         else:
#             self.name = f"Я не {name}, а Николай!"
# person1 = Nikola ("Николай", 34)
# person2 = Nikola ("Владислав", 67)
# print(person1.name)
# print(person2.name)

# Задачи lambda 

#Задание 2
# my_list_1 = [1,2,3,4,"Япония",4,"Китай"]
# arr_2 = list(filter(lambda x: type (x) != str, my_list_1))
# arr_2 = list(filter(lambda x: isinstance (x, int), my_list_1)) #Второй вариант!
# print(arr_2)

#Задание 3 
# num = 2 
# arr_1 = [1,2,3,7,8]
# arr_answer = list(map(lambda x: x * (num + 1), arr_1 ))
# print(arr_answer)

#Задачи на файлы (open)

#Задание 1 
# Вариант 1
# text = input("Введите текст: ")
# with open("study.txt","a") as text_test:
#     text_test.write(text)

#Вариант 2 
# text = input("Введите текст: ")
# test_file = open("study.txt","w")
# print(test_file)
# test_file.write(text)
# test_file.close

#Задачи на JSON

#Задание 1

# import json

# list_data = {}
# print("Добро пожаловать!")
# text = input("Введите одну из доступных команд(new/del/exit): ")
# while (text != "exit" and text != "ex"):
#     if text == "new":
#         username = input("Введите свой никнейм: ")
#         password = input("Введите пароль: ")
#         list_data[username]=password   
#     elif text == "del":
#         user_del = input("Введите никнейм для удаления из базы данных: ")
#         list_data.pop(user_del)
#     with open("new.json" , "w") as file:
#         json.dump(list_data , file)   
#     text = input("Введите одну из доступных команд(new/del/exit): ")
    
# Задание 2

# import json

# answer = 0
# calculator_arr = []
# with open("calculator.json") as file:
#     calculator_arr = json.load(file)
# print("Добро пожаловать в калькулятор!")
# text = input("Введите start для начала работы калькулятора: ")
# while ( text == "start"):
#     number = int(input("Введите первое число: "))
#     number_two = int(input("Введите второе число: "))
#     action = input ("Действие: ")

#     if action == "*":
#         answer = number * number_two
#         print ("Произведение чисел = ", answer)
#     elif action == "/":
#         answer = number / number_two
#         print ("Частное чисел = ", answer)
    # elif action == "-":
    #     answer = number - number_two
    #     print ("Разность чисел = ", answer)
    # elif action == "+":
    #     answer = number + number_two
    #     print ("Сумма чисел = ", answer)
    # with open("calculator.json" , "w") as file:
    #     calculator_arr.append(f"{number} {action} {number_two} = {answer}") 
    #     json.dump(calculator_arr , file) 
    # text = input("Введите start для начала работы калькулятора: ")


# Задачи на TK start

# Задание 1 

# from tkinter import *

# def click_button():
#     global click
#     click += 1
#     label_clicer.configure(text=click)

# click = 0
# window = Tk()
# window.title("Кликер")
# window.geometry("980x720")

# label_clicer = Label(text= click , font=("Arial Black", 18))
# label_clicer.place(x=460 , y = 250)

# button_counter = Button(text= "Нажимай", command=click_button, font=("Segoe Print", 25), fg="#3d04f7")
# button_counter.place(x=380 , y = 300)


# window.mainloop()

#Задание 2 


# from tkinter import *
# from random import *

# window = Tk()
# window.title("Поймай кнопку")
# window.geometry("980x720")
# window["bg"] = "green"

# def movement():
#     x = randint(5, 980)
#     y = randint(5, 720)
#     button_mov.place_configure(x=x, y=y)

# label_clicer = Label(text="Хочешь повышения зарплаты?" , font=("Verdana", 18), fg="#0400fc", bg="#d0f402")
# label_clicer.place(x = 350 , y = 260)
# button_mov = Button(text="Поймай меня", command=movement, font=("Segoe Print", 15), fg="#0c0c0c")
# button_mov.place(x = 410 , y = 300)


# window.mainloop()

#Задача на entry

#Задание 1

# from tkinter import*

# window = Tk()
# window.title("Калькулятор")
# window.geometry("300x300")
# window.config(bg="#000")

# def addition():
#     print(int(first_number.get()) + int(second_number.get()))

# def subtraction():
#     print(int(first_number.get()) - int(second_number.get()))

# def division():
#         print(int(first_number.get()) / int(second_number.get()))

# def multiplication():
#     print(int(first_number.get()) * int(second_number.get()))


# first_text = Label(text="Введите первое число", font=("Segoe Print", 8), bg="white")
# first_text.place(x=90, y=20)

# first_number = Entry(width=5, font=("Arial", 13), bg="white", fg="lime")
# first_number.place(x=130, y=50)

# second_text = Label(text="Введите второе число", font=("Segoe Print", 8), bg="white")
# second_text.place(x=90, y=80)

# second_number = Entry(width=5, font=("Arial", 13), bg="white", fg="lime")
# second_number.place(x=130, y=110)

# info_text = Label(text="Выберите действие:",font=("Arial Black", 10), bg="purple" )
# info_text.place(x=80, y=150)

# addition_btn = Button(text="Сложение", command=addition, font=("Times New Roman", 9),  bg="green")
# addition_btn.place(x=130, y=185)

# subtraction_btn = Button(text="Вычитание", command=subtraction, font=("Times New Roman", 9),  bg="green")
# subtraction_btn.place(x=130, y=210)

# division_btn = Button(text="Деление", command=division, font=("Times New Roman", 9),  bg="green")
# division_btn.place(x=130, y=235)

# multiplication_btn = Button(text="Умножение", command=multiplication, font=("Times New Roman", 9),  bg="green")
# multiplication_btn.place(x=130, y=260)



# window.mainloop()

#Задание 2 

# from tkinter import*
# from tkinter import messagebox

# def click():
#     username = entry_login.get()
#     password = entry_password.get()
#     messagebox.showinfo("Авторизация пройдена!", f"User: {username} pass: {password}")

# window = Tk()
# window.title("Авторизация пользователя")
# window.geometry("900x700")
# window.config(bg="#000")


# greetings = Label(text="Добро пожаловать!", font=("monospaced", 25), fg="#33bb41", bg="black")
# greetings.place(x=310, y=10)

# login = Label(text="Логин", font=("Helvetica", 15), fg="aquamarine", bg="black")
# login.place(x=430, y = 160)

# entry_login = Entry(width=11, font=("Arial", 13), bg="black", fg="lime")
# entry_login.place(x=410, y = 200)

# password = Label(text="Пароль", font=("Helvetica", 15), fg="aquamarine", bg="black")
# password.place(x=420, y = 230)

# entry_password = Entry(width=11, font=("Arial", 13), bg="black", fg="lime")
# entry_password.place(x=410, y = 270)

# but_enter = Button(text="Войти", command=click, font=("Times New Roman", 17), fg="black", bg="purple")
# but_enter.place(x=420, y=320)


# window.mainloop()

#Задание на Listbox

# Задание 1

from tkinter import*

window = Tk()
window.title("Касса")
window.geometry("700x500")
window.config(bg="#c4efef")

def buy():
    roster_listbox.insert(0 , product_ent.get())
addition_btn = Button(text= "Добавить товар", fg="#000", command=buy)
addition_btn.place(x=330, y=345)


def delet_product():
    roster_listbox.delete(0, roster_listbox.curselection())
deleted_btn = Button(text= "Удалить товар", fg="#000", command=delet_product)
deleted_btn.place(x=335, y=385)

purchases_lbl = Label(text="Список покупок:", font =(" Arial", 12))
purchases_lbl.place(x=200, y=150)

array_product = []
roster_listbox = Listbox(listvariable= Variable(value=array_product))
roster_listbox.place(x=200, y=180)

product_ent= Entry(bg="#f7f7f7", fg="#0d0c0d", font=("Times New Roman", 9))
product_ent.place(x=200, y=345, height=27)

def cost_product():
#итоговая сумма покупок
    1.

result_lbl = Label(text="\nИтоговая сумма:\nрублей", font =(" Arial", 10))
result_lbl.place(x=50, y=345)

window.mainloop()




