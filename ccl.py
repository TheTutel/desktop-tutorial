while 1==1:
    num1 = float(input("num1: "))
    num2 = float(input("num2: "))

    action = int(input("Action\n1 - sum\n2 - sub\n3 - mul\n4 - div\n"))

    if action == 1:
        res = num1 + num2
    elif action == 2:
        res = num1 - num2
    elif action == 3:
        res = num1 * num2
    elif action == 4:
        res = num1 / num2
    #
    print(res)
    go = input("Again? ")
    if go == "yeah": print("ok")
    elif go == "nah": exit()
