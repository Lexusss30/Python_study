SEPARATOR = "------------------------------------------------------------"
name = ""
age = 0
phone = ""
email = ""
postal_index = ""
address = ""
information = ""
ogrnip = ""
inn = ""
current_account = ""
bank_name = ""
bik = ""
correspondent_account = ""

def personal_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, postal_index_parameter, address_parameter):
    print(SEPARATOR)
    print("Имя:", name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = "лет"
    elif age_parameter % 10 == 1:
        years_parameter = "год"
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = "года"
    else:
        years_parameter = "лет"

    print("Возраст:", age_parameter, years_parameter)
    print("Телефон:", phone_parameter)
    print("E-mail:", email_parameter)
    print("Индекс:", postal_index_parameter)
    print("Адрес:", address_parameter)


print("Приложение MyProfile")
print("Сохраняй информацию о себе и выводи ее в разных форматах")

while True:
    print(SEPARATOR)
    print("ГЛАВНОЕ МЕНЮ")
    print("1 - Ввести или обновить информацию")
    print("2 - Вывести информацию")
    print("0 - Завершить работу")

    option = int(input("Введите номер пункта меню: "))
    if option == 0:
        break

    if option == 1:
        while True:
            print(SEPARATOR)
            print("ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ")
            print("1 - Личная информация")
            print("2 - Информация о предпринимателе")
            print("0 - Назад")

            choice = int(input("Введите номер пункта меню: "))
            if choice == 0:
                break
            if choice == 1:
                name = input("Введите имя: ")
                while 1:
                    age = int(input("Введите возраст: "))
                    if age > 0:
                        break
                    print("Возраст должен быть положительным")

                user_number = input("Введите номер телефона (+7ХХХХХХХХХХ): ")
                phone = ""
                for number in user_number:
                    if number == "+" or ("0" <= number <= "9"):
                        phone += number

                email = input("Введите адрес электронной почты: ")
                index = input("Введите почтовый индекс: ")
                for numeric in index:
                    if numeric.isdigit:
                        postal_index = postal_index + numeric
                address = input("Введите почтовый адрес (без индекса): ")
                information = input("Введите дополнительную информацию: ")
            elif choice == 2:
                ogrnip = input("Введите ОГРНИП: ")
                while len(ogrnip) < 15:
                    print("ОГРНИП должен содержать больше 15 цифр")
                    ogrnip = input("Введите ОГРНИП: ")
                inn = input("Введите ИНН: ")
                current_account = input("Введите расчётный счёт: ")
                while len(current_account) < 20:
                    print("Рассчётный счёт должен содержать больше 20 цифр")
                    current_account = input("Введите расчётный счёт: ")
                bank_name = input("Введите название банка: ")
                bik = input("Введите БИК: ")
                correspondent_account = input("Введите корреспондентский счёт: ")
            else:
                print("Введите корректный пункт меню")
    elif option == 2:

        while True:
            print(SEPARATOR)
            print("ВЫВЕСТИ ИНФОРМАЦИЮ")
            print("1 - Личная информация")
            print("2 - Вся информация")
            print("0 - Назад")

            choice = int(input("Введите номер пункта меню: "))
            if choice == 0:
                break
            if choice == 1:
                personal_info_user(name, age, phone, email, postal_index, address)

            elif choice == 2:
                personal_info_user(name, age, phone, email, postal_index, address)
                print("Информация о предпринимателе")
                print("ОГРНИП:", ogrnip)
                print("ИНН:", inn)
                print("Расчётный счёт:", current_account)
                print("Название банка:", bank_name)
                print("БИК:", bik)
                print("Корреспондентский счёт:", correspondent_account)

            else:
                print("Введите корректный пункт меню: ")
    else:
        print("Введите корректный пункт меню: ")