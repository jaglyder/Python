#==========================================================================
# PROGRAM PURPOSE:... 7-1
# AUTHOR:............ Glyder, Jillian
# COURSE:............ CSC 131-002
# TERM:.............. Fall 2019
# COLLABORATION:..... 
# WORK TIME(h:mm):... 1:30
#==========================================================================
# Program for Determining Palindromes

import stack
import letterCount

# welcome
print ('This program can determine if a given string is a palindrome\n')
print ('(Enter return to exit)')

# init
char_stack = stack.getStack()
empty_string = ''
longest_palindrome = ''

# get string from user
chars = input('Enter string to check: ')

while chars != empty_string:
    if len(chars) == 1:
        print('A one letter word is by definition a palindrome\n')
    else:
        # init
        is_palindrome = True

        # determine half of length. excluding any middle character
        compare_length = len(chars) // 2

        # push second half of input string on stack
        for k in range(compare_length, len(chars)):
            stack.push(char_stack, chars[k])

        # pop chars and compare to first half of string
        k = 0
        while k < compare_length and is_palindrome:
            ch = stack.pop(char_stack)
            if chars[k].lower() != ch.lower():
                is_palindrome = False

            k = k + 1

        # display results
        if is_palindrome:
            print (chars, 'is a palindrome\n')
            #Implemented here
            length_var = countLetters(chars)
            if length_var > longest_palindrome:
                longest_palindrome = chars
            print("Current longest palindrome: " + longest_palindrome)
        else:
            print (chars, 'is NOT a palindrome\n')

    # get string from user
    chars = input('Enter string to check: ')
