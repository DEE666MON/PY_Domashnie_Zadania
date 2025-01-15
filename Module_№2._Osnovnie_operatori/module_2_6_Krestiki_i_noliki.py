def proverka_pobeditelia_KN():
    if (pole_KN[0][0] == "X" and pole_KN[0][1] == "X" and pole_KN[0][2] == "X") or (
            pole_KN[1][0] == "X" and pole_KN[1][1] == "X" and pole_KN[1][2] == "X") or (
            pole_KN[2][0] == "X" and pole_KN[2][1] == "X" and pole_KN[2][2] == "X") or (
            pole_KN[0][0] == "X" and pole_KN[1][0] == "X" and pole_KN[2][0] == "X") or (
            pole_KN[0][1] == "X" and pole_KN[1][1] == "X" and pole_KN[2][1] == "X") or (
            pole_KN[0][2] == "X" and pole_KN[1][2] == "X" and pole_KN[2][2] == "X") or (
            pole_KN[0][0] == "X" and pole_KN[1][1] == "X" and pole_KN[2][2] == "X") or (
            pole_KN[0][2] == "X" and pole_KN[1][1] == "X" and pole_KN[2][0] == "X"):
        return "X"
    elif (pole_KN[0][0] == "0" and pole_KN[0][1] == "0" and pole_KN[0][2] == "0") or (
            pole_KN[1][0] == "0" and pole_KN[1][1] == "0" and pole_KN[1][2] == "0") or (
            pole_KN[2][0] == "0" and pole_KN[2][1] == "0" and pole_KN[2][2] == "0") or (
            pole_KN[0][0] == "0" and pole_KN[1][0] == "0" and pole_KN[2][0] == "0") or (
            pole_KN[0][1] == "0" and pole_KN[1][1] == "0" and pole_KN[2][1] == "0") or (
            pole_KN[0][2] == "0" and pole_KN[1][2] == "0" and pole_KN[2][2] == "0") or (
            pole_KN[0][0] == "0" and pole_KN[1][1] == "0" and pole_KN[2][2] == "0") or (
            pole_KN[0][2] == "0" and pole_KN[1][1] == "0" and pole_KN[2][0] == "0"):
        return "0"
    else:
        return "*"


def pechat_pole_KN():
    for i in pole_KN:
        print(*i)
    print()


pole_KN = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("Добро пожаловать в игру 'Крестики и Нолики'.")
print()
pechat_pole_KN()
for hod in range(1, 10):
    print(f"Ход: {hod}")
    if hod % 2 == 0:
        hod_char = "0"
        print("Ходит Нолик.")
    else:
        hod_char = "X"
        print("Ходит Крестик.")
    user_stroka = int(input("Введите номер строки(1, 2, 3): ")) - 1
    user_stolb = int(input("Введите номер столбца(1, 2, 3): ")) - 1
    if pole_KN[user_stroka][user_stolb] == "*":
        pole_KN[user_stroka][user_stolb] = hod_char
    else:
        print("Ячейка занята. Пропуск хода.")
        pechat_pole_KN()
        continue
    pechat_pole_KN()
    if proverka_pobeditelia_KN() == "X":
        print("Победа Крестика!")
        break
    elif proverka_pobeditelia_KN() == "0":
        print("Победа Нолика!")
        break
    elif proverka_pobeditelia_KN() == "*" and hod == 9:
        print("Ничья!")
