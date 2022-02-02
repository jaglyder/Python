#==========================================================================
# PROGRAM PURPOSE:... Ch3 M7
# AUTHOR:............ Glyder, Jillian
# COURSE:............ CSC 131-002
# TERM:.............. Fall 2019
# COLLABORATION:..... 
# WORK TIME(h:mm):... 1:00
#==========================================================================
# Coin Change Exercise Program

import random

# program greeting
print('The purpose of this exercise is to enter a number of coin values')
print('that add up to a displayed target value.\n')
print('Enter coins values as 1-penny, 5-nickel, 10-dime and 25-quarter')
print("Hit return after the last entered coin value.")
print('----------------')

# init
terminate = False
empty_str = ''

# start game
while not terminate:
    amount = random.randint(1,99)
    numQ = amount// 25
    numR = amount % 25
    numD = numR // 10
    numR = numR % 10
    numN = numR // 5
    numR = numR % 5
    numP = numR // 1
    numR = numR % 1
    numcoins= numQ + numD + numN + numP
    print(numcoins)

    print('Enter coins that add up to', amount, 'cents, one per line.\n')
    game_over = False
    total = 0
    usercoin = 0
    while not game_over:
        valid_entry = False
        
        while not valid_entry:
            if total == 0:
                entry = input('Enter first coin: ')
            else:
                entry = input('Enter next coin: ')
            if entry in (empty_str,'1','5','10','25'):
                valid_entry = True
               
            else:
                print('Invalid entry')
        
        if entry == empty_str:
            if total == amount:
                if numcoins == usercoin:
                    print('Correct!')
                else:
                    print(' Sorry - too many coins.')
                
                
        
            
            else:
                print('Sorry - you only entered', total, 'cents.')
                
            game_over = True
            
        else:
            total = total + int(entry)
            usercoin = usercoin + 1
            if total > amount:
                print('Sorry - total amount exceeds', amount, 'cents.')
                game_over = True
                
        if game_over:
            entry = input('\nTry again (y/n)?: ')
            
            if entry == 'n':
                terminate = True

print('Thanks for playing ... goodbye')
    


