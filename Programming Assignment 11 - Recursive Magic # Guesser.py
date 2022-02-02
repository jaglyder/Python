#==========================================================================
# PROGRAM PURPOSE:... Recursive Magic
# AUTHOR:............ Glyder, Jillian
# COURSE:............ CSC 131-002
# TERM:.............. Fall 2019
# COLLABORATION:..... 
# WORK TIME(h:mm):... 1:30
#==========================================================================

import random
def rec(a,b,c):
   check=random.randint(x+1,y-1)
   if(z==check):
       print("Guess is"+" "+str(check)+"...Winner")
   else:
       if(check<z):
           print("Guess is"+" "+str(check)+"...Higher")
       elif(check>z):
           print("Guess is"+" "+str(check)+"...Lower")
       rec(x,y,z)
  
low=high=magic=check=0
while(True):
      
   print("Select a lower limit,upper limit,and the magic number")
   x=input("Lower limit:")
   y=input("Upper limit:")
   z=input("Magic number:")
   try:
       low=int(x)
       high=int(y)
       magic=int(z)
       if(magic<=low or magic>=high):
           print("Magic number must be > Lower Limit < Upper Limit")
       else:
           rec(low,high,magic)
           break;
          
   except:
       print("please provide, integer")
