class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def __proverka_getAllWords(self, all_words, i, file):
        destSymbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        itogList = []
        for line in file:
            anotherStr = ''
            line = line.lower()
            for char in line:
                for symb in destSymbols:
                    if symb in char:
                        char = ''
                anotherStr += char
            for g in anotherStr.split():
                itogList.append(g)
            all_words[i] = itogList
        return all_words

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                self.__proverka_getAllWords(all_words, i, file)
        return all_words

    def __proverka_findOrCount(self, slovar, word, flagBreak):
        for key,value in self.get_all_words().items():
            countStr = 0
            for i in range(len(value)):
                if word in value[i]:
                    if flagBreak:
                        slovar[key] = i + 1
                        break
                    else:
                        countStr += 1
            if not flagBreak:
                slovar[key] = countStr
        return slovar

    def find(self, word):
        slovar = {}
        word = word.lower()
        self.__proverka_findOrCount(slovar, word, True)
        return slovar

    def count(self, word):
        slovar = {}
        word = word.lower()
        self.__proverka_findOrCount(slovar, word, False)
        return slovar


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
