def all_variants(text):
    yield text[0]
    yield text[1]
    yield text[2]
    for w in range(len(text)):
        for e in range(w+1, len(text)):
            yield text[w: e+1]
            break
    yield text


a = all_variants("abc")
for i in a:
    print(i)
