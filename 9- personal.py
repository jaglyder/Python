#==========================================================================
# PROGRAM PURPOSE:... 9 - Personal translation dictionary
# AUTHOR:............ Glyder, Jillian
# COURSE:............ CSC 131-002
# TERM:.............. Fall 2019
# COLLABORATION:..... 
# WORK TIME(h:mm):... 1:30
#==========================================================================

word_dictionary={}
print('WELCOME TO YOUR PERSONAL DICTIONARY')
while True:
    print('Type[1] to add a new word')
    print('Type[2] to translate a word')
    print('Type[3] to print the current dictionary')
    print('Type[4] to exit')
    choice = input()
    if choice=='1':
        word=""
        while word.strip()=="":
            word=input('Enter the word:').strip().lower()
            if word_dictionary.get(word)==None:
                meaning=""
                while meaning.strip() == "":
                    meaning = input('Enter the meaning:').strip()
            else:
                print('Word already exists in the dictionary')
                break
        word_dictionary[word]=meaning
        print('Word',word,'added to your dictionary!\n')
    if choice=='2':
        search_word=input('Enter lookup word: ').strip()
        if word_dictionary.get(search_word)==None:
            print('No word found')
        else:
            print(word,'meaning:',word_dictionary.get(word))
    if choice=='3':
        for word,meaning in word_dictionary.items():
            print(word,':',meaning)
    if choice=='4':
        print('Thank you!')
        break
