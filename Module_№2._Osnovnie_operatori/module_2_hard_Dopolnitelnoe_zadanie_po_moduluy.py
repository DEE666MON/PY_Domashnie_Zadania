from random import *
num_char = []
num_random = randint(3, 21)
print(num_random)
for i in range(1, 20):
    for j in range(2, 20):
        if num_random % (i + j) == 0 and i != j and i < j:
            num_char.append([])
            num_char[len(num_char)-1].append(str(i))
            num_char[len(num_char)-1].append(str(j))
        else:
            continue
for i in range(len(num_char)):
    for j in range(len(num_char[i])):
        print(num_char[i][j], end="")