n #==========================================================================
# PROGRAM PURPOSE:... Ch4 P5
# AUTHOR:............ Glyder, Jillian
# COURSE:............ CSC 131-002
# TERM:.............. Fall 2019
# COLLABORATION:..... 
# WORK TIME(h:mm):... 1:00
#==========================================================================

#prompt the user to enter a list of words

#store a list of words whose first letter occurs again within the word


a = input('Enter first word: ')
b = input('Enter second word: ')
c = input('Enter third word: ')
mylist = [a, b, c]
print(mylist)

#word.find(first_letter) => number (if it is there) else -1 (if it is not)
first_letter = a[0] #first letter
word = a
if(word.find(first_letter, 1) < 0):
    del mylist[mylist.index(word)]
            
 #  print(first letter)
first_letter = b[0] 
word = b
if(word.find(first_letter, 1) < 0):
    del mylist[mylist.index(word)]

first_letter = c[0] 
word = c
if(word.find(first_letter, 1) < 0):
    del mylist[mylist.index(word)]
print(mylist)
