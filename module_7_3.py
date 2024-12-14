import string
import itertools


class WordsFinder:
    result ={}
    def __init__(self, *file_names):
         self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                line_list = []
                for line in file:
                    line = line.translate(str.maketrans('','', string.punctuation)).replace(' — ', " ").lower().split()
                    line_list.append(line)
                    merged = [x for l in line_list for x in l]
                all_words[filename] = merged
        return all_words

    def find(self, word):
        words = self.get_all_words()
        word_search = word.lower()
        for key, value in words.items():
            if word_search in value:
                place = value.index(word_search) + 1
                self.result[key] = place
        return self.result

    def count(self,word):
        words = self.get_all_words()
        word_search = word.lower()
        for key, value in words.items():
            if word_search in value:
                word_count = value.count(word_search)
                self.result[key] = word_count
        return self.result




finder2 = WordsFinder('test.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))


