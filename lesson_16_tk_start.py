from tkinter import *


window = Tk()
window.title("lesson15")
window.geometry("980x720")



lab_text_1 = Label(text="Привет" , bg="#f40dd1" , font=("Segoe Print" , 18) , fg="#b2f704")
lab_text_1.place(x=280 , y=90 , width=300 , height=50)



lab_text_2 = Label(text="Ты лучший", font=("Ink Free" , 15))
lab_text_2.place(x=340 , y=250,)



def fun_1():
    print("ok")
    lab_text_2.config(bg="#ffd084" , text="Я ")
    button_1.place(x=100 , y=200)
button_1 = Button(text= "ТКНИ НА МЕНЯ" , command=fun_1, font=("MV Boli", 10), bg="#070000", fg="#2e05fa")
button_1.place(x=370 , y =300)


def fun_2():
    print(window.geometry())
    lab_text_2.configure(text= window.geometry())
button_2 = Button(text= "geometry win" , command=fun_2)
button_2.place(x=10 , y=80)





window.mainloop()