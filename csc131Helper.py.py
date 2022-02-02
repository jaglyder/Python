#==========================================================================
# PROGRAM PURPOSE:... 7-2
# AUTHOR:............ Glyder, Jillian
# COURSE:............ CSC 131-002
# TERM:.............. Fall 2019
# COLLABORATION:..... 
# WORK TIME(h:mm):... 2:00
#==========================================================================
"""Doc String for csc131Helper.py, this module contains the methods: makeGrid(width, height, block_size, turtle_obj)"""
def makeGrid(width, height, block_size, turtle_obj):
    """Doc String for makeGrid(width, height, block_size, turtle_obj): this method draws a complete grid of the input size with the given turtle as the worker"""
    turtle_obj.penup()
    turtle_obj.setposition(0,0)
    turtle_obj.pendown()
    turtle_obj.forward(int(width/2))
    turtle_obj.right(90)
    turtle_obj.forward(int(height/2))
    turtle_obj.left(180)
    turtle_obj.forward(int(height))
    turtle_obj.left(90)
    for x in range(height/block_size):
        for k in range(width/block_size):
            turtle_obj.forward(block_size)
            turtle_obj.left(90)
            turtle_obj.forward(block_size)
            turtle_obj.left(180)
            turtle_obj.forward(block_size)
            turtle_obj.left(90)
        turtle_obj.left(90)
        turtle_obj.forward(block_size)
        turtle_obj.left(90)
        turtle_obj.forward(int(width))
        turtle_obj.left(180)
    turtle_obj.hideturtle()

def userInputInt(lower_limit, upper_limit):
    """Doc String for userInputInt(lower_limit, upper_limit)"""
    while True:
        user_input = str(input("Enter an integer between the the limits " + str(lower_limit) + " and " + str(upper_limit) + " :"))
        if user_input == "":
            print("You did not enter anything, try again...")
            continue
        invalid_input = False
        for x in user_input:
            if (x != "0") and (x != "1") and (x != "2") and (x != "3") and (x != "4") and (x != "5") and (x != "6") and (x != "7") and (x != "8") and (x != "9") and (x != "-"):
                invalid_input = True
                break
        if invalid_input:
            print("You entered invalid input, try again (Enter only integers with no extra characters)")
            continue
        if (int(user_input) >= lower_limit) and (int(user_input) <= upper_limit):
            return int(user_input)
        else:
            print("You entered input that was out of bounds there for it is invalid")
