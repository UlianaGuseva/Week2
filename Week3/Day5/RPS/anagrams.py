from anagram_checker import AnagramChecker
def menu():
    wrong_word = 'yes'
    choise_list = []
    while wrong_word == 'yes':
        choise = input('input a word or print ’exit’ to exit: ')
        if choise != 'exit':
            choise_list = list(choise)
            while choise_list[0] == ' ':
                del choise_list[0]
            while choise_list[-1] == ' ':
                del choise_list[-1]
            wrong_word = 'no'
            if ' ' in choise_list:
                wrong_word = 'yes'
                print('wrong word. input 1 word')
            elif ''.join(choise_list).isalpha() == False:
                wrong_word = 'yes'
                print('wrong word. input only alphabetic characters')
        else:
            print('Good bye!')
            choise_list = list(choise)
            wrong_word = 'no'
            break         
    choise = ''.join(choise_list)          
    return choise
    
                    
     
def main():
    while True:
        choise = menu()
        if choise == 'exit':
            break
        else:
            my_anagram = AnagramChecker()
            valid = AnagramChecker.is_valid_word(my_anagram, choise) 
            if valid == True:
                anagram_list = AnagramChecker.get_anagrams(my_anagram, choise)
                print('Your word', choise, '\nthis is valid English word.\nAnagrams for your word: ', anagram_list)
            else:
                print('This is not a valid English word')

main()