def all_variants(text):
    for q in text:
        yield q
    for w in range(len(text)):
        for e in range(w+1, len(text)):
            yield text[w] + text[e]
            break
    yield text


a = all_variants("abc")
for i in a:
    print(i)
