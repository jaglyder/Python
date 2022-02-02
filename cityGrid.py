#==========================================================================
# PROGRAM PURPOSE:... Ch6 D1
# AUTHOR:............ Glyder, Jillian
# COURSE:............ CSC 131-002
# TERM:.............. Fall 2019
# COLLABORATION:..... 
# WORK TIME(h:mm):... 4:00
#==========================================================================


# Create a Turtle graphics window and draw a city grid of streets that run vertically and horizontally.  Place at least 4 turtles somewhere on the grid and have them conduct a random walk around the city.  Color your turtles so that they are easily differentiated among one another and have them leave a trail of their travels behind them of the same color.
# Decide on an objective for your "game" so that it ends at some point.  Some possible objectives are:
#
# ·        each time turtles meet, the meeting turtles get a point; game ends when the first turtle accrues x points
#
# ·        place a goal location on the grid, when a turtle finds the goal location that turtle wins and the game is over
#
# ·        place a wormhole on the grid, when a turtle finds the wormhole, suck them off the grid into another dimension; when all turtles have disappeared the game is over
#
# ·        place multiple wormholes on the grid, when a turtle finds a wormhole, transfer them to a random place on the grid; game could end after each turtle finds wormholes at least x times
#
# ·        use your imagination...
#
# Items you may consider having the user select:
#
# ·        size of the city block
#
# ·        number of turtles
#
# ·        speed of the turtles
#
# ·        use your imagination...
import turtle
import random
import time

print("Welcome to turtle City, In this game you get to choose the size of the city grid, the number of turtles to randomly roam the city, and the speed in which they roam. Once each turtle hits the randomly selected end-point on the grid, the turtle will disappear. The last turtle to find the point is the winner.")
city_grid_height = 0
while True:
    invalid_input1 = False
    city_grid_height = input("Enter the height in blocks of your city grid (EVEN Integer between 2 and 30 ): ")
    for x in city_grid_height:
        if (x != "0") and (x != "1") and (x != "2") and (x != "3") and (x != "4") and (x != "5") and (x != "6") and (x != "7") and (x != "8") and (x != "9"):
            print("*****Invalid Input: only enter postitive even Integers")
            invalid_input1 = True
            break
    if invalid_input1:
        continue
    city_grid_height = int(city_grid_height)
    if (city_grid_height < 2) or (city_grid_height > 30) or (city_grid_height%2==1):
        print("*******Invalid Input: enter EVEN integer in range (2 <= your number <=30)")
        continue
    print("")
    break


city_grid_width = 0
while True:
    invalid_input2 = False
    city_grid_width = input("Enter the width in blocks of your city grid (EVEN Integer between 2 and 40 ): ")
    for x in city_grid_width:
        if (x != "0") and (x != "1") and (x != "2") and (x != "3") and (x != "4") and (x != "5") and (x != "6") and (x != "7") and (x != "8") and (x != "9"):
            print("*****Invalid Input: only enter postitive even Integers")
            invalid_input2 = True
            break
    if invalid_input2:
        continue
    city_grid_width = int(city_grid_width)
    if (city_grid_width < 2) or (city_grid_width > 40) or (city_grid_width%2==1):
        print("*******Invalid Input: enter EVEN integer in range (2 <= your number <=40)")
        continue
    print("")
    break


print("")

number_of_turtles = 0
while True:
    invalid_input3 = False
    number_of_turtles = input("Enter the number of turtles you would like to compete (between 2 and 6): ")
    for x in number_of_turtles:
        if (x != "0") and (x != "1") and (x != "2") and (x != "3") and (x != "4") and (x != "5") and (x != "6") and (x != "7") and (x != "8") and (x != "9"):
            print("*****Invalid Input: only enter postitive Integer between 2 and 6")
            invalid_input3 = True
            break
    if invalid_input3:
        continue
    number_of_turtles = int(number_of_turtles)
    if (number_of_turtles < 2) or (number_of_turtles > 6):
        print("**********Invalid Input, only enter integer between 2 and 6.")
        continue
    print("")
    break

speed_of_turtles = 1
while True:
    invalid_input4 = False
    speed_of_turtles = input("Enter the speed that the turtles move (integer between 1 and 1000, the higher the number the faster): ")
    for x in speed_of_turtles:
        if (x != "0") and (x != "1") and (x != "2") and (x != "3") and (x != "4") and (x != "5") and (x != "6") and (x != "7") and (x != "8") and (x != "9"):
            print("**********Invalid Input, only enter integer between 1 and 1000")
            invalid_input4 = True
            break
    if invalid_input4:
        continue
    speed_of_turtles = int(speed_of_turtles)
    if (speed_of_turtles < 1) or (speed_of_turtles > 1000):
        print("*******Invalid input, only enter integer between 1 and 1000")
        continue
    print("")
    break

screen_height = 840
screen_width = 640
turtle.setup(screen_height, screen_width)

window = turtle.Screen()
window.title('Turtle City')

artist = turtle.Turtle()
artist.shape("arrow")
artist.color("black")
artist.speed(2000)
artist.setposition(0,0)
artist.forward(int(20*(city_grid_width/2)))
artist.right(90)
artist.forward(int(20*(city_grid_height/2)))
artist.left(180)
artist.forward(int(20*(city_grid_height)))
artist.left(90)
for x in range(city_grid_height):
    for k in range(city_grid_width):
        artist.forward(20)
        artist.left(90)
        artist.forward(20)
        artist.left(180)
        artist.forward(20)
        artist.left(90)
    artist.left(90)
    artist.forward(20)
    artist.left(90)
    artist.forward(int(20*city_grid_width))
    artist.left(180)
artist.hideturtle()

turtles = []
turtle_rank = []
colors = ["red", "blue", "green", "pink", "yellow", "orange"]
for k in range(number_of_turtles):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.shape('circle')
    # new_turtle.shape('arrow')
    new_turtle.shapesize(.4,.4)
    new_turtle.color(colors[k])
    new_turtle.speed(speed_of_turtles)
    integer1 = random.randint(int((city_grid_height/2)*-1),int(city_grid_height/2))
    integer2 = random.randint(int((city_grid_width/2)*-1),int(city_grid_width/2))
    # print(integer1)
    # print(integer2)
    new_turtle.setposition(int(integer2*20), int(integer1*20))
    new_turtle.pendown()
    turtles.append([new_turtle,[int(integer2*20),int(integer1*20)]])

end_point = []
invalid6 = False
while True:
    integer3 = int(random.randint(int((city_grid_height/2)*-1),int(city_grid_height/2)))
    integer4 = int(random.randint(int((city_grid_width/2)*-1),int(city_grid_width/2)))

    end_point = [int(integer4*20), int(integer3*20)]
    # print(end_point)
    # print(turtles)
    for x in turtles:
        if x[1] == end_point:
            invalid6 = True
            break
    if invalid6:
        continue
    break

end_point_turtle = turtle.Turtle()
end_point_turtle.penup()
end_point_turtle.shape('triangle')
end_point_turtle.shapesize(.4,.4)
end_point_turtle.color("black")
end_point_turtle.speed(1)
end_point_turtle.left(90)
end_point_turtle.setposition(end_point[0], end_point[1])
print("end_point")
print(end_point_turtle.pos())

right_border = int((city_grid_width/2)*20)
left_border = int(right_border*-1)
top_border = int((city_grid_height/2)*20)
bottom_border = int(top_border*-1)
print("right_border: " + str(right_border))
print("left_border: " + str(left_border))
print("top_border: " + str(top_border))
print("bottom_border: " + str(bottom_border))
incr = 0
for x in turtles:
    x.append([0,0,0,0])
    # colors = ["red", "blue", "green", "pink", "yellow", "orange"]
    x.append(colors[incr])
    incr += 1
# print()
game_continue = True
while game_continue:
    # setting border arrays for each remaining turtle
    for x in turtles:
        if x[1][0] == left_border:
            x[2][0] = 1
        else:
            x[2][0] = 0
            # print(x)
            # print("left_border")
        if x[1][0] == right_border:
            x[2][1] = 1
        else:
            x[2][1] = 0
            # print(x)
            # print("right_border")
        if x[1][1] == top_border:
            x[2][2] = 1
        else:
            x[2][2] = 0
            # print(x)
            # print("top_border")
        if x[1][1] == bottom_border:
            x[2][3] = 1
        else:
            x[2][3] = 0
            # print(x)
            # print("bottom_border")
    # print(turtles)
    # Random moves for each turtle
    for x in turtles:

        print("turtle before:")
        print(x)
        # left
        if (x[2][0] == 1) and (x[2][2] == 0) and (x[2][3] == 0):
            print("left: " + str(x))
            # 1 = right
            # 2 = up
            # 3 = down
            rand_move = random.randint(1,3)
            if rand_move == 1:
                x[0].forward(20)
            elif rand_move == 2:
                x[0].left(90)
                x[0].forward(20)
                x[0].right(90)
            elif rand_move == 3:
                x[0].right(90)
                x[0].forward(20)
                x[0].left(90)


        # right
        elif (x[2][1] == 1) and (x[2][2] == 0) and (x[2][3] == 0):
            print("right: " + str(x))
            #1 = left
            #2 = up
            #3 = down
            rand_move = random.randint(1,3)
            if rand_move == 1:
                x[0].left(180)
                x[0].forward(20)
                x[0].left(180)
            elif rand_move == 2:
                x[0].left(90)
                x[0].forward(20)
                x[0].right(90)
            elif rand_move == 3:
                x[0].right(90)
                x[0].forward(20)
                x[0].left(90)

        # top
        elif (x[2][2] == 1) and (x[2][0] == 0) and (x[2][1] == 0):
            print("top: " + str(x))
            # 1 = left
            # 2 = right
            # 3 = down
            rand_move = random.randint(1,3)
            if rand_move == 1:
                x[0].left(180)
                x[0].forward(20)
                x[0].left(180)
            elif rand_move == 2:
                x[0].forward(20)
            elif rand_move == 3:
                x[0].right(90)
                x[0].forward(20)
                x[0].left(90)

        # bottom
        elif (x[2][3] == 1) and (x[2][0] == 0) and (x[2][1] == 0):
            print("bottom: " + str(x))
            # 1 = left
            # 2 = right
            # 3 = up
            rand_move = random.randint(1,3)
            if rand_move == 1:
                x[0].left(180)
                x[0].forward(20)
                x[0].left(180)
            elif rand_move == 2:
                x[0].forward(20)
            elif rand_move == 3:
                x[0].left(90)
                x[0].forward(20)
                x[0].right(90)


        # left-top
        elif (x[2][0] == 1) and (x[2][2] == 1):
            print("left-top: " + str(x))
            #1 = right
            #2 = down
            rand_move = random.randint(1,2)
            if rand_move == 1:
                x[0].forward(20)
            elif rand_move == 2:
                x[0].right(90)
                x[0].forward(20)
                x[0].left(90)

        # right-top
        elif (x[2][1] == 1) and (x[2][2] == 1):
            print("right-top: " + str(x))
            # 1 = left
            # 2 = down
            rand_move = random.randint(1,2)
            if rand_move == 1:
                x[0].left(180)
                x[0].forward(20)
                x[0].left(180)
            elif rand_move == 2:
                x[0].right(90)
                x[0].forward(20)
                x[0].left(90)

        # left-bottom
        elif (x[2][0] == 1) and (x[2][3] == 1):
            print("left-bottom: " + str(x))
            # 1 = right
            # 2 = up
            rand_move = random.randint(1,2)
            if rand_move == 1:
                x[0].forward(20)
            elif rand_move == 2:
                x[0].left(90)
                x[0].forward(20)
                x[0].right(90)

        # right-bottom
        elif (x[2][1] == 1) and (x[2][3] == 1):
            print("right-bottom" + str(x))
            # 1 = left
            # 2 = up
            rand_move = random.randint(1,2)
            if rand_move == 1:
                x[0].left(180)
                x[0].forward(20)
                x[0].left(180)
            elif rand_move == 2:
                x[0].left(90)
                x[0].forward(20)
                x[0].right(90)
        else:
            rand_move = random.randint(1,4)
            # 1 = left
            # 2 = right
            # 3 = top
            # 4 = bottom
            if rand_move == 1:
                x[0].left(180)
                x[0].forward(20)
                x[0].left(180)
            elif rand_move == 2:
                x[0].forward(20)
            elif rand_move == 3:
                x[0].left(90)
                x[0].forward(20)
                x[0].right(90)
            elif rand_move == 4:
                x[0].right(90)
                x[0].forward(20)
                x[0].left(90)

                # left off here
        temp_var = list(x[0].pos())

        x[1] = [int(round(temp_var[0])), int(round(temp_var[1]))]
        # for x in turtles:
        #     x[0].speed(speed_of_turtles)
        #     if str(x[1][0])[-1] == "9":
        #         x[1][0] = (x[1][0] + 1)
        print("Turtle after:")
        print(x)
    replacement_turtles = []
    for x in turtles:
        if x[1] == end_point:
            x[0].hideturtle()
            x[0].penup()
            turtle_rank.append(x)
        else:
            replacement_turtles.append(x)
    turtles = replacement_turtles
    if len(turtles) == 0:
        print("game over")
        game_continue = False




    # game_continue = False
    # for x in turtles:
    #     print(x[0].pos())

    # print(end_point)
    # for x in turtles:
    #     if x[1] == end_point:
    #         print("hit the end point")



# left
# right
# top
# bottom
# left-top
# right-top
# left-bottom
# right-bottom


# artist2 = turtle.Turtle()
# artist2.shape("arrow")
# artist2.speed(1)
# artist2.color("red")
# artist2.setposition(0,0)
# artist2.forward(20)
# artist2.left(90)
# artist2.forward(20)
#
# artist.left(180)
# artist.forward(40)
# artist.left(180)
# artist.forward(60)
# print(list(turtles[0][0].pos()))
print("The rank of the game from first place to last is as follows: ")
incr2 = 1
for x in turtle_rank:
    print(str(incr2) + ". " + x[3])
    incr2 += 1
    # print(x[3])
