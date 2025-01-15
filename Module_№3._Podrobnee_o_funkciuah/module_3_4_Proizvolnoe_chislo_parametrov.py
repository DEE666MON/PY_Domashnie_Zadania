def single_root_words(root_word, *other_words):
    same_words = []
    sovpadeniua = 0
    root_word = root_word.lower()
    other_words = list(other_words)
    for i in range(len(other_words)):
        other_words[i] = other_words[i].lower()
    for n in range(len(root_word)):
        for i in range(len(other_words)):
            # print(f"{root_word} = {other_words[i]}?")
            for j in range(len(other_words[i])):
                print(f"{root_word[n]} = {other_words[i][j]}?",end="")
                if root_word[n] == other_words[i][j] or other_words[i][j] == root_word[n]:
                    sovpadeniua += 1
                    n += 1
                    print(f" Совпадений = {sovpadeniua}")
                    if sovpadeniua == len(root_word) or sovpadeniua == len(other_words[i]):
                        same_words.append(other_words[i])
                        sovpadeniua = 0
                        n = 0
                        break
                else:
                    sovpadeniua = 0
                    n = 0
                    print()
        if len(same_words) > 0:
            break
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(f"\n{result1}")
print(result2)
