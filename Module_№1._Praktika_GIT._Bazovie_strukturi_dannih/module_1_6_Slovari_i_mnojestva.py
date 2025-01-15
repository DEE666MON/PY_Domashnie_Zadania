# Словарь

my_dict = {"Dmitriu": 2002, "Vladimir": 1998, "Peter": 1970, "Ivan": 2010}
print(my_dict)
print(my_dict.get("Ivan", "Отсутствует"))
print(my_dict.get("David", "Отсутствует"))
my_dict.update({"David": 2001, "Alexandr": 2023})
znach = my_dict.pop("Dmitriu")
print(znach)
print(my_dict)

# Множества

my_set = {1, 2, 3, 4, 5.9, 6, 7, 8, 9, 0.5, 6, 7, 8, 9, 0, 1.5, 2, 3, 4, 5, 5.9, True, False, 'Diamond', "Opaz", (1, 2, 3, 1.1, False, "True")}
print(my_set)
my_set.add(10)
my_set.add("False")
my_set.discard(0.5)  # my_set.remove(0.5)
print(my_set)