class AnagramChecker:
    def __init__(self) -> None:
        filename = 'sowpods.txt'
        with open(filename, 'r') as file:
            text = file.read()
            self.list_words = text.split('\n')
    def is_valid_word(self, word):
        word = word.upper()
        # print(self.list_words)
        if word in self.list_words:
            return True
        else:
            return False
    def get_anagrams(self, word):
        word = word.upper()
        anagram_list = []
        for i in self.list_words:
            list_word = list(i)
            list_my_word = list(word)
            
            if len(list_word) == len(list_my_word): 
                if list_word != list_my_word:                   
                    if set(word) == set(i):
                        anagram_list.append(i)
        return anagram_list
    