# ==================================== LOOPS ===========================================

# Let's say I wanted to print "hello" 5 times
# Typically I would have to do something like:
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")

# A FOR LOOP (0,1,2,3,4) so it prints 5 times. Count from zero and stop before 5. For each each number counted store the value in the variable x
for x in range(0,5):
    print('hello')

print('------------------------------------------')

# This function creates a list of numbers from the starting number through the number before the last (10-19)
# Range is what goes from 10-19
# List obviously taking the values of the range and putting them inside a list
print(list(range(10,20)))

# Let's put an insert (%s) inside a FOR LOOP
x = 0

for x in range(0, 5):        
    print('hello %s' % x)

# Rather than writing this print statement 5 times I use the FOR LOOP
print('hello %s' % x)

# The reason I put none here is so I can use the x variable in the future (not required for this FOR LOOP)
x = None
print('------------------------------------------')

# Looping through a list with a FOR LOOP
wizard_list = ['spider legs', 'toe of frog', 'snail tongue', 'bat wing', 'slug butter', 'bear burp']
for i in wizard_list: 
    print(i)

# Rather than writing this print statement 6 times I use the FOR LOOP
print(wizard_list[0])

print('------------------------------------------')

# We made a list hugehairypants and started a FOR LOOP that iterates through i. 
hugehairypants = ['huge', 'hairy', 'pants']
for i in hugehairypants:
    print(i)
    print(i)

print('------------------------------------------')

# The loop i iterates ("huge" ... "hairy" ... "pants") once before the full iteration of j
for i in hugehairypants:
    print(i)
    for j in hugehairypants:
        print(j)

print('------------------------------------------')

# Iterating through the week FOR LOOP for coins for weeks 1-52
found_coins = 20 
magic_coins = 70
stolen_coins = 3 
coins = found_coins
for week in range(1, 53):        
    coins = coins + magic_coins - stolen_coins         
    print('Week %s = %s' % (week, coins))

print('------------------------------------------')
# A FOR LOOP is a loop that has a definite end (only runs for a certain period, its iteration)
# A WHILE LOOP is for when you don't know when it needs to end (it runs until told to stop)

# A FOR LOOP would be used for something like climbing a staircase
# A WHILE LOOP would be used for climbing a mountain 

# This is sudo code for a WHILE LOOP, we haven't defined the variables within so it will not run

# step = 0
# while step < 10000:    
#     print(step)    
#     if tired == True:        
#         break    
#     elif badweather == True:        
#         break    
#     else:        
#         step = step + 1


# The basic steps to a WHILE LOOP is as follows 
#   1) Check the condition
#   2) Execute the code in the block
#   3) Repeat

# while True:    
#   lots of code here    
#   lots of code here    
#   lots of code here    
#   if some_value == True:        
#       break

# Here is a basic WHILE LOOP using conditionals 
x = 45
y = 80
while x < 50 and y < 100:        
    x = x + 1        
    y = y + 1        
    print(x, y)
print('------------------------------------------')


print('============================================== RECYCLING MODULES AND FUNCTIONS ===================================================')

# FUNCTIONS are chunks of code that tell Python to do something
# There is one way to reuse code - FUNCTIONS. You can use them over and over again
# FUNCTIONS are essential in long or complicated programs (if you intend on finishing the code this century)
list(range(0, 100))

# There are 3 parts to a FUNCTIONS: Name, Parameters, Body
# I've named this FUNCTION testfunc, myname is pased as the parameter, and the body is the code that immediately follows the def (define)
def testfunc(myname):
    print('hello %s' % myname)

# We have just called the FUNCTION using it's name and parameter value
testfunc('Mary')
print('------------------------------------------')

# FUNCTIONS can take any number of parameters
def testfunc(fname, lname):
    print('Hello %s %s' % (fname, lname))

testfunc('Joe', 'Bob')
print('------------------------------------------')

# Let's makes some variables then call them 
firstname = 'Bill'
lastname = 'Anderson'
testfunc(firstname, lastname)
print('------------------------------------------')

# Using a function to get a return statement
def savings(pocket_money, paper_route, spending):
    return pocket_money + paper_route - spending
print(savings(10, 10, 5))
print('------------------------------------------')

# Variables and scope
def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable

print(variable_test())

# Showing scope by trying to print a variable outside of the scope (gives an error)
# print(first_variable)

# Showing scope by defining var before the FUNCTION
another_variable = 100
def variable_test2():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable * another_variable
print(variable_test2())
print('------------------------------------------')

# Making a function, defining the cans var, making a FOR LOOP for the weeks in a year (52), making a print statement with inserts
def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print("Week %s = %s cans" % (week, total_cans))

# Calling my function and adding the value for cans 
spaceship_building(2)
print('------------------------------------------')

# Modules are used to group functions, variables, and other things together into larger, more powerful programs. Some modules are built in to Python, and you can download other modules separately.

# One such example of a built in MODULE is time
import time

print(time.asctime())

# Now suppose that you want to ask someone using your program to enter a value, perhaps their date of birth or their age. You can do this using a print statement, to display a message, and the sys (short for system) module, which con-tains utilities for interacting with the Python system itself. First, we import the sys module:

import sys

# Inside the sys module is a special object called stdin (for standard input), which provides a rather useful function called readline. The readline function is used to read a line of text typed on the keyboard until you press enter.

# import sys 
# print(sys.stdin.readline())

# We just made the value of the var age into an integer that is inputted by the user
def silly_age_joke():        
    print('How old are you?')         
    age = int(sys.stdin.readline())         
    if age >= 10 and age <= 13:                
        print('What is 13 + 49 + 84 + 155 + 97? A headache!')        
    else:                
        print('Huh?')

silly_age_joke()