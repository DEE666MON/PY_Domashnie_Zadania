calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(stroka=""):
    count_calls()
    stroka_count = len(stroka)
    stroka_up = stroka.upper()
    stroka_low = stroka.lower()
    all_kortej = (stroka_count, stroka_up, stroka_low)
    return all_kortej


def is_contains(stroka="", spisok=[]):
    proverka = True
    count_calls()
    stroka = stroka.lower()
    for i in range(len(spisok)):
        for j in range(len(spisok)):
            spisok[j] = spisok[j].lower()
        if stroka != spisok[i]:
            proverka = False
        else:
            proverka = True
            break
    return proverka


print(string_info("Topor"))
print(string_info("Bransbout"))
print(is_contains("TopoR", ["toP", "Or", "ToPoR"]))
print(is_contains("Bransbout", [""""BransBOUt",""" "OuT", "Bra", "boy"]))
print(calls)
