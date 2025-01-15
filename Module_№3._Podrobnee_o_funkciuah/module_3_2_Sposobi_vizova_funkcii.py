def is_contains(stroka=""):
    stroka = stroka.lower()
    stroka = list(stroka)
    proverka = False
    stroka_ru = stroka[len(stroka) - 2] + stroka[len(stroka) - 1]
    stroka_net_com = stroka[len(stroka) - 3] + stroka[len(stroka) - 2] + stroka[len(stroka) - 1]
    if stroka[len(stroka) - 3] == "." or stroka[len(stroka) - 4] == ".":
        for i in range(len(stroka)):
            if stroka[i] != "@":
                proverka = False
            else:
                proverka = True
                break
        if proverka and (stroka_ru == "ru" or stroka_net_com == "net" or stroka_net_com == "com"):
            return True
        proverka = False
    return proverka


def send_email(soobshenie, polychatel, *, otpravitel="university.help@gmail.com"):
    if not (is_contains(otpravitel) and is_contains(polychatel)):
        print(f"Невозможно отправить письмо с адреса {otpravitel} на адрес {polychatel}.")
    elif otpravitel == polychatel:
        print("Нельзя отправить письмо самому себе!")
    elif otpravitel == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {otpravitel} на адрес {polychatel}.")
        # print(soobshenie)
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {otpravitel} на адрес {polychatel}.")
        # print(soobshenie)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.net')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', otpravitel='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', otpravitel='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', otpravitel='urban.teacher@mail.ru')
