# =========================================== Turtles ===========================================

# Turtles are the name of a slow running visual program in Python
# A module in Python is a way of providing useful code to be used by another program (among other things, the module can contain functions we can use).
# Turtles are a module 
import turtle

# creating a canvas (a blank screen for turtle to draw on)
t = turtle.Pen()
# You should see a blank box with an arrow in the center, that arrow is the turtle
# If the turtle is an hourglass something is wrong, check that you have turtle installed, or try restarting the shell

# Making the turtle move 
# Turtles move by pixels, 50 pixels in this case 
t.forward(50)

# We have turned the turtle by 90 degrees, it should now be looking upwards
# Turning does not move the turtle, it only changes the direction the turtle is looking
t.left(90)

# Moved the turtle up by 50
t.forward(50)

# Turned the turtle left 
t.left(90)

# Moved left 50 pixels
t.forward(50)

# Turned the turtle downwards
t.left(90)

# Moved turtle down 50
t.forward(50)

# Turtle turned right
t.left(90)

# ----------------------------------
# The are good ways to keep the turtle open since it closes the moment it is done running. 
# Having the turtle open in a window and manually exit

# window = turtle.Screen()
# .......
# window.exitonclick()

# Set this up at the end (we'll go over inputs later)
# input("Press any key to exit ...")

# Slap this at the end, the easiest solution
# turtle.done()
# ---------------------------------

# Used to erase the canvas and puts turtle at starting position
# t.reset()

# Used to just clear the canvas but leaves the turtle where it was left
#t.clear()

# You can also move backwards
t.backward(100)

# You can also pick the pen up to stop drawing but still move
t.up()
t.right(90)
t.forward(20) 
t.left(90) 

# Putting the pen back down to draw again
t.down() 
t.forward(100)

turtle.done()

