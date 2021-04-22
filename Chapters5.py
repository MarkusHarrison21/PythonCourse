#  =================================== IF AND ELSE STATEMENTS =========================================

# An if statement, follow it with a colon ':' to intiate the code block 
age = 12
if age > 20:
    print('You are too old!')

# This is the first time we are dealing with indentations in Python. It is improtant to know that indentation(spaces) plays an important role in tell the computer you are still in a code block but also it let's the user know.

aged = 64
if aged > 20:
    print('You are too old!')
    print("Shouldn't you go scroll on facebook?")
    print("Go get a mortgage!")

# ---------------------------------------------------------------------
    # There are 4 spaces in a tab/indentation
    # If code has the same indentation it is in the same block 

    # block one
    # block one
    # block one
        # block two
        # block two
        # block two
            # block three
            # block three
            # block three
        # block two
        # block two


# Below blocks 2 and 3 are different because there is a block with less indentation between them

    # block one
    # block one
    # block one
        # block two
        # block two
        # block two
    # block one
    # block one
    # block one
        # block three
        # block three
        # block three
# ---------------------------------------------------------------------

# You don't have to have each indent be 4 spaces (it is common practice and the way you should do it) but as long as the amount of spaces in the indentation are the same it is the same block
# In this example we use 6 spaces and not 4
ages = 21
if ages > 20:
      print('I hate the way you indent (6 spaces and not 4)')
      print('Just use 4 spaces you monkey')

# ---------------------------------------------------------------------
# Good old fashion operators:

# Don't forget = means to set something's value to

#   ==  Equal to
#   !=  Not equal to
#   >   Greater than
#   <   Less than
#   >=  Greater than or Equal to
#   <=  Less than or Equal to

# ---------------------------------------------------------------------

ages = 17
if ages <= 17:
    print('You are a child!')


# ======================================== IF THEN ELSE STATEMENT ===========================================

# “If something is true, then do this; or else, do that.”
# If it mets the criteria then TRUE else FALSE

print("Hey want to hear a secret?")
age = 21
if age == 21:
    print("We're having a sleepover")
else:
    print("Yeah, you're not invited")

# Now let's use else-if statements as well. Python uses ELIF which is short for else-if
# It passes the information down from top to bottom to see if it meets the conditions as it makes it's way down
# Once it passes the condition it does not check the rest of them but rather continues inside of the condition or breaks from the if-else
# age should pass both elif == 12: and elif <= 13: but only does the first passing condition

age = 12  
if age == 10:         
    print("What do you call an unhappy cranberry?")        
    print("A blueberry!")
elif age == 11:        
    print("What did the green grape say to the blue grape?")        
    print("Breathe! Breathe!") 
elif age == 12:         
    print("What did 0 say to 8?")        
    print("Hi guys!")
elif age <= 13:        
    print("Why wasn't 10 afraid of 7?")        
    print("Because rather than eating 9, 7 8 pi.")
else:        
    print("Huh?")


# If statements can "or" inside the statement to see if it passes either conditional 
if age == 10 or age == 11 or age == 12 or age == 13:        
    print('What is 13 + 49 + 84 + 155 + 97? A headache!')
else:        
    print('Huh?')

# You can use "and" statements inside the if conditional to check if it passes both
if age >= 10 and age <= 13:       
    print('What is 13 + 49 + 84 + 155 + 97? A headache!')
else:        
    print('Huh?')

# In Python, an empty value is referred to as None, and it is the absence of value. And it’s important to note that the value None is different from 0, since the 0 will be interpreted as an int 
# Used to "reset a value", make it NONE (NULL) and then redeclare/overwrite it later in the program
# Also can be used to declare a variable
myVal = None
print(myVal)

if myVal == None:
    print("I don't think you entered your name correctly")

# !!!!!! User Input is always understood as a string !!!!!!

# User Input example; showing how you would take a str user input and change it into a int
age = '10'
converted_age = int(age)
if converted_age == 10:
    print("omg it worked")

# Changing a int to a string
Lydia = 64 
converted_num = str(Lydia)
if converted_num == '64':
    print("My dog is cute")

# Changing floats
ages = '10.5'
if ages == '10.5':
    print("It's a string")
converted_ages = float(ages)
if converted_ages == 10.5:
    print("Changed to a float")
    print (converted_ages)





