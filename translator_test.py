import time
import turtle

def output_translate():
    if translate in words:
        if translate.lower() == old.lower():
            print(f'Тупой? Я же сказал:\n{words.get(translate)}')
        else:
            print(f'Translated word:\n{words.get(translate)}')
    else:
        print("Я такой фигни не знаю.")

words = {
    "лом": "APFSDS",
    "пробой": "penetration",
    "подвижность": "manoeuvrability",
    "задний ход": "reverse speed",
    "боевой рейтинг": "battle rating",
    "вектор тяги": "thrust vectoring",
    "КОЭП": "OEC"
}

count = 0
old = ""


while 1 == 1:
    count += 1
    translate = input("Чего нужно?")
    if translate == "вектор тяги":
        age = int(input("Тебе сколько лет?\n"))
        if 18 <= age < 20:
            output_translate()
#                print(f'{words.get(translate)}')
        elif age > 20:
            print("Иди работать!!!")
            exit()
        else:
            print("А мама знает что ты здесь?")
            print("Перевод: ***********")
            print("Но больше так не делай")
    else:
        output_translate()
#
#            if translate.lower() == old.lower():
#                print(f'Тупой? Я же сказал:\n{words.get(translate)}')
#            else:
#                print(f'Translated word:\n{words.get(translate)}')
        old = translate
    done = input("Еще чего-нить?")
    if done.lower() != "да":
        break
    if count >= 3:
        print("задолбали. У меня обед")
        exit()
print("до побачення")

turtle.left(45)
turtle.forward(50)
for repeat in range(2):
    turtle.left(22.5)
    turtle.forward(10)
turtle.left(45)
turtle.forward(10)
turtle.right(45)
turtle.forward(10)
for repeat in range(2):
    turtle.left(22.5)
    turtle.forward(10)
turtle.left(45)
turtle.forward(50)
input()