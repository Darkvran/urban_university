class WordsFinder:
    def __init__(self, *filenames):
        self.filenames = filenames

    def get_all_words(self):
        chars_to_remove = [',', '.', '=', '!', '?', ';', ':', '-', '\n']
        all_words = {}
        for file in self.filenames:
            with open(file, 'r', encoding='utf-8') as f:
                all_words[file] = []
                file_strings = f.readlines()
                for string in file_strings:
                    for char in chars_to_remove:
                        string = string.replace(char, '').lower()
                    all_words[file] += [i for i in string.split(' ') if i]
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        fw_dict = {}
        for name, words in all_words.items():
            if word.lower() in words:
                fw_dict[name] = words.index(word.lower()) + 1
        return fw_dict

    def count(self, word):
        all_words = self.get_all_words()
        word_counter = {}
        for name, words in all_words.items():
            word_counter[name] = words.count(word.lower())
        return word_counter


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
