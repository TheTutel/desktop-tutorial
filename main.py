print("Рад приветствовать, это я, бот Георгий! Хочешь фатальную ошибку? Да - 1 / Нет - 2")
talk_style=int(input('1/2:'))
if talk_style==2:
    print("Бот Григорий:")
    print("Тогда введи логин: ")
    login=input()
    print("Показать пароль? Да - 1 / Нет - 2")
    setting=input()
    if setting==1:
        print("Теперь введи пароль: ")
        pass1=input()
        print("Подтверди пароль, введя его ещё раз: ")
        pass2=input()
        if pass1==pass2:
            print("Ура! Вы преодолели все стадии шизофрении! Ваш логин -",login,", ваш пароль -",pass1)
            exit()
        else: print("Пароли не совпадают. Руки трясутся, по клавишам не попадаем?")
    else:         print("Теперь введи пароль: "); pass1=input(); print("Подтверди пароль, введя его ещё раз: "); pass2=input()
    if pass1==pass2:
        print("Ура! Вы преодолели все стадии шизофрении! Ваш логин -",login,", ваш пароль - ****")
        exit()
    else: print("Пароли не совпадают. Руки трясутся, по клавишам не попадаем?")
else: print("CRITICAL, FATAL, TACTICAL, STRATEGICAL ERROR!!!")
exit()

#dsdfsdfsdfsdfsdfsdfsdf