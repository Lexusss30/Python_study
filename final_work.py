def main():
    print("\nГЛАВНОЕ МЕНЮ")
    print("1 - Вывести или обновить информацию\n2 - Вывести информацию\n0 - Завершить работу ")
    choice = int(input("Введите номер пункта меню: "))
    if choice == 1:
        information(name, age, phone_number, address_mail, postal_mail, postal_code_result, additionally)
    elif (choice == 2):
        print("ВЫВЕСТИ ИНФОРМАЦИЮ")
        print("1 - Общая информация\n2 - Вся информация\n0 - Назад ")
        option = input("Введите номер пункта меню: ")
        if option == 1:
        # вызов 
            information(name, age, phone_number, address_mail, postal_mail, postal_code_result, additionally)
        elif option == 2:
           entrepreneurship(ogrnip, inn, current_account, bank, bik, correspondent_account)
        elif option == 3:
            return main()    
    # elif choice == 0:
    #     break
        #выход из программы


name = ""
age = ""
phone_number = ""
address_mail = ""
postal_mail = ""
postal_code = ""
postal_code_result = ""
additionally = ""
def information(name, age, phone_number, address_mail, postal_mail, postal_code_result, additionally):
    print("ВЫВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ")
    print("1 - Личная информация\n2 - Информация о предпринимателе\n0 - Назад ")
    point = int(input("Введите номер пункта меню: "))
    if point == 1:
        #вызываем функцию которая хранит личную информацию
        name = input("Введите имя: ")
        age = int(input("Введите возраст: "))
        while age < 0:
            age = int(input("Введите возраст: "))
        phone_number = int(input("Введите номер телефона (+7ХХХХХХХХХХ): "))
        address_mail = input("Введите адрес электронной почты: ")
        postal_mail = input("Введите почтовый адрес(без индекса): ")
        postal_code = input("Введите почтовый индекс: ")
        postal_code_result = ""
        for i in postal_code:
            if i.isdigit():
                postal_code_result += i 
        additionally = input("Введите допольнительную информацию: ")
        return name, age, phone_number, address_mail, postal_mail, postal_code_result, additionally
    elif point == 2:
        #вызываем фукнцию где данные о предпринимателе 
        entrepreneurship(ogrnip, inn, current_account, bank, bik, correspondent_account)
    return main()
        
    
ogrnip = ""
inn = ""
current_account = ""
bank = ""
bik = ""
correspondent_account = ""    
def entrepreneurship(ogrnip, inn, current_account, bank, bik, correspondent_account):
    ogrnip = int(input("Введите ОГРНИП: "))
    if len(str(ogrnip)) < 15:
        print("ОГРНИП должен содержать больше 15 чисел")
        ogrnip = int(input("Введите ОГРНИП: "))
    inn = int(input("Введите ИНН: "))
    current_account = int(input("Введите расчётный счёт: "))
    bank = input("Введите название банка: ")
    bik = int(input("Введите БИК: "))
    correspondent_account = int(input("Введите корреспондентский счёт: "))
    return ogrnip, inn, current_account, bank, bik, correspondent_account
    
        

print("Приложение MyProfile.")
print("Сохраняй информацию о себе и выводи её в разных форматах.")

main()