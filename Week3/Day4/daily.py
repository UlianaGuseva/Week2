from collections import Counter
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re

class Text():
    string_text = ''
    

    def __init__(self) -> None:
        pass
    @classmethod
    def put_string_text(self, string):
        Text.string_text = string
    @classmethod
    def frequency_word(self, word):
        text_list = Text.string_text.split(' ')
        count = 0
        for i in text_list:
            if word == i:
                count += 1
            else:
                count = count
        if count > 0:
            print('frequency of a word <', word, '> in the text -', count)
        else:
            return None
    @classmethod
    def most_common(self):
        text_list = Text.string_text.split(' ')            
        print('most common word -', Counter(text_list).most_common(1))
    @classmethod
    def unique(self):
        text_list = Text.string_text.split(' ')
        unique_words = set(text_list)
        print(unique_words)
    @classmethod
    def from_file(self, my_file):
        filename = my_file
        with open(filename, 'r') as file:
            Text.string_text = str(file.read())
        print(Text.string_text)
        
class TextModification(Text):
    def __init__(self) -> None:
        pass
    @classmethod
    def no_punctuation(self):
        new_text = Text.string_text.translate(str.maketrans('', '', string.punctuation))
        print(new_text)
    @classmethod
    def no_stop_words(self):
        stop_list = set(stopwords.words('english'))
        print(stop_list)
        text_list = Text.string_text.split(' ')
        new_text1 = ''
        for i in text_list:
            if i not in stop_list:
                new_text1 += i + ' '
        print(new_text1)
    @classmethod
    def no_specif(self):
        new_text = re.sub('\W+','', Text.string_text)
        print(new_text)


        
string_input = 'A good book would sometimes cost as much as a good house.'
Text.put_string_text(string_input)
print(Text.string_text)

Text.frequency_word('good')
Text.frequency_word('God')

Text.most_common()

Text.unique()

Text.from_file('the_stranger.txt')
Text.frequency_word('good')
Text.most_common()

# Text.unique()
TextModification.no_punctuation()
TextModification.no_stop_words()

TextModification.no_specif()