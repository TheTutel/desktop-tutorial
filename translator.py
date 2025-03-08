words = {
    "лом":"APFSDS",
    "пробой":"penetration",
    "подвижность":"manoeuvrability",
    "задний ход":"reverse speed",
    "боевой рейтинг":"battle rating",
    "вектор тяги":"thrust vectoring",
    "КОЭП":"OEC"
}
count = 0
old = ""
while 1 == 1:
    count += 1
    translate = input("Чего нужно?")
    if translate in words:
        if translate.lower() == old.lower():
            print(f'Тупой? Я же сказал:\n{words.get(translate)}')
        else:
            print(f'Translated word:\n{words.get(translate)}')
            old = translate
    done = input("Еще чего-нить?")
    if done.lower() != "да":
        break
    if count >= 10:
        print("задолбали. У меня обед")
        exit()
print("до побачення")
