print(" ====================================== HOW TO USE CLASSES AND OBJECTS =====================================================")

# In the English language we understand "things" as nouns (person, place, or thing). In Python nouns are understood as Objects.

#  ============================= Breaking Things Into Classes ===========================
# In Python objects are defined by classes, which we can think of as a way to classify objects into groups. Let's expand on this with the diagram below to show a way to classify a sidewalk and a giraffe.

#                                   Things
#                               /           \
#                         Inanimate          Animate
#                             |                 |
#                         Sidwalks           Animals
#                                               |
#                                            Mammals
#                                               |
#                                            Giraffes 

# The Animals class is the parent of the  Mammals class, and Mammals is the  parent  of Giraffes.

# Let's think back to the Turtle Module we ised back in Chapter 4. The Pen class had functions for moving forward, backward, turning left/right. An Object can be thought of as a member of the class, and we can create any number of objects for a class.

# Let's make that diagram above
# Make a Class by using the class keyword and the name followed by a colon
# Now we use pass to tell Python that we don't wish to fill out any more info for the class(or for a function) at the moment
class Things:
    pass

# ============================== Children and Parents =============================

# If a class is a part of another class, then it’s a child of that class, and the other class is its parent.
# In our tree diagram, the class above another class is its parent, and the class below it is its child. For example, Inanimate and Animate are both children of the class Things, meaning that Things is their parent.

# To tell Python that a class is a child of another class, we add the name of the parent class in parentheses after the name of our new class, like this:

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass


class Animals(Animate):         
    pass 
class Mammals(Animals):         
    pass 
class Giraffes(Mammals):         
    pass

# ============================ Adding Objects to Classes =============================

# Say we have a giraffe named Reginald. We know that he belongs in the class Giraffes, but what do we use, in programming terms, to describe single giraffe called Reginald? We call Reginald an object of the class Giraffes (you may also see the term instance of the class)

# This code tells Python to create an Object in the Giraffes class and assign it to the variable reginald.
reginald = Giraffes()

# =========================== Defining Functions of Classes =============================
# Reginald doesn't do anything right now. To make our objects useful, when we create our classes, we also need to define functions that can be used with the objects in that class. Rather than just using the pass keyword immediately after the class definition, we can add function definitions.

# To use Functions in a class we define it in the same way we normally do but indent it inside of the class 

# Here's a normal func
def this_is_a_normal_func():
    print("I'm a normal func")
this_is_a_normal_func()
print('------------------------------------------')

# Here's two funcs inside a class 
class ThisIsMyFuncClass:
    def this_is_a_class_function():            
        print('I am a class function')        
    def this_is_also_a_class_function():            
        print('I am also a class function. See?')
print('------------------------------------------')

# ============================== CHARACTERISTICS ==============================
# We can add characteristics to each class to describe what it is and what it can do. A characteristic is a trait that all of   the members of the class (and its children) share

# These characteristics can be thought of as actions, or functions— things that an object of that class can do. To add a function to a class, we use the def keyword.
class Animals(Animate):        
    def breathe(self):            
        pass        
    def move(self):            
        pass        
    def eat_food(self):            
        pass

# Each class will be able to use the characteristics (the functions) of its parent. This means that you don’t need to make one really complicated class; you can put your functions in the highest parent where the characteristic applies. (This is a good way to make your classes simpler and easier to understand.)

class Mammals(Animals):        
    def feed_young_with_milk(self):            
        pass

class Giraffes(Mammals):        
    def eat_leaves_from_trees(self):            
        pass

# Because reginald is an object, we can call (or run) functions pro-vided by his class (the Giraffes class) and its parent classes. We call functions on an object by using the dot operator and the name of the function. To tell Reginald the giraffe to move or eat, we can call the functions like this:

reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()

# We can move a specific Object (Harold in this case) without moving the others (Reginald)
harold = Giraffes()
harold.move()

# Making what's going on more obvious with print statements inside the Functions
class Animals(Animate):        
    def breathe(self):            
        print('breathing')        
    def move(self):            
        print('moving')        
    def eat_food(self):            
        print('eating food')

class Mammals(Animals):        
    def feed_young_with_milk(self):            
        print('feeding young') 

class Giraffes(Mammals):        
    def eat_leaves_from_trees(self):            
        print('eating leaves')

reginald = Giraffes()
harold = Giraffes()
reginald.move()
harold.eat_leaves_from_trees()

print("-------------------- Objects and Classes in Pictures-------------------------")

# When we use turtle.Pen(), Python creates an object of the Pen class that is provided by the turtle module.
# We can create two turtle objects (named Avery and Kate), just as we created two giraffes:

print("You must close the turtle window for the code outside of this unit to run/print in the console")
import turtle
# Each turtle object (avery and kate) is a member of the Pen class.
avery = turtle.Pen()
kate = turtle.Pen()

# Having created our turtle objects, we can call functions on each, and they will draw independently.
# Avery has gone forward 50 and down 20 pixels
avery.forward(50)
avery.right(90)
avery.forward(20)

# Kate has gone up 100 pixels
kate.left(90)
kate.forward(100)

# Let's add a 3rd turtle object named Jacob
jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)

# Remember that every time we call turtle.Pen() to create a turtle, we add a new, independent object. Each object is still an instance of the class Pen, and we can use the same functions on each object, but because we’re using objects, we can move each turtle independently.

# If we create a new object with the same variable name as an object we’ve already created, the old object won’t necessarily vanish. Try it for yourself: Create another Kate turtle and try moving it around.
# I'm making this new kate instance look downwards and move 50 pixels
kate = turtle.Pen()
kate.right(90)
kate.forward(50)

# This is just to keep the turtle prompt up after it completes the task
turtle.done()

print("You should've see a turtle pop up")
print("-------------------------------------")
print("----------------- Inherited Functions -----------------")

# Classes and objects make it easy to group functions. They’re also really useful when we want to think about a program in smaller chunks

# But break these monster programs into smaller pieces, and each piece starts to make sense—as long as you know the language, of course! When writing a large program, breaking it up also allows you to divide the work among other programmers. 

# The Giraffes class inherits functions from the Mammals class, which, in turn, inherits from the Animals class. In other words, when we create a giraffe object, we can use functions defined in the Giraffes class, as well as functions defined in the Mammals and Animals classes.

# Going back to the tree diagram we made before
# Even though Reginald is an object of the Giraffes class, we can still call the move function that we defined in the Animals class because functions defined in any parent class are available to its child classes:

reginald = Giraffes()
reginald.move()

# In fact, all of the functions we defined in both the Animals and Mammals classes can be called from our reginald object because the functions are inherited:

reginald = Giraffes()
reginald.breathe()
reginald.eat_food()
reginald.feed_young_with_milk()

# This is how we typically call our Functions on our objects
print("Our typical call to the function is reginald.move() which prints:")
reginald.move()

# To have a function in the Giraffes class call the move function, we would use the self parameter instead. The self parameter is a way for one function in the class to call another function. For example, suppose we add a function called find_food to the Giraffes class:
class Giraffes(Mammals):        
    def find_food(self):            
        self.move()            
        print("I've found food!")            
        self.eat_food()
    def eat_leaves_from_trees(self):            
        self.eat_food()        
    def dance_a_jig(self):            
        self.move()            
        self.move()            
        self.move()            
        self.move()
# Above we have now created a function that combines two other functions
# Later we will use this to make a game but for right now understand that this is typically used to get a return that we will use in another function (you would do this over and over again in multiple blocks of code)

print('-----------------------------------------------')
# Now let's make this giraffe dance
print("Want to see a giraffe dance?")

# We add this block of code to where it was defined before (202-208)
# def eat_leaves_from_trees(self):            
#     self.eat_food()        
#     def dance_a_jig(self):            
#         self.move()            
#         self.move()            
#         self.move()            
#         self.move()

reginald = Giraffes()
reginald.dance_a_jig()

print('-----------------------------------------------')
print("Finally let's go over intializing an object")

# Sometimes when creating an object, we want to set some values (also called properties) for later use. When we initialize an object, we are getting it ready to be used.

# For example, suppose we want to set the number of spots on our giraffe objects when they are created—that is, when they’re initialized. To do this, we create an __init__ function (notice that there are two underscore characters on each side, for a total of four).

# This is a special type of function in Python classes and must have this name. The init function is a way to set the properties for an object when the object is first created, and Python will automati-cally call this function when we create a new object. Here’s how to use it:

class Giraffes:  
    # We define the init func with 2 parameters, which are self and spots (line 240). Just like the other Functions we've defined in a class it needs self as the first parameter      
    def __init__(self, spots):       
        # This line says, “Take the value of the parameter spots and save it for later (using the object variable giraffe_spots).”
        # Just as one function in a class can call another function using the self parameter, variables in the class are also accessed using self.
        self.giraffe_spots = spots

# We made new Giraffes and gave their spots
ozwald = Giraffes(100)
gertrude = Giraffes(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)

# First, we create an instance of the Giraffes class, using the parameter value 100. This has the effect of calling the __init__function and using 100 for the value of the spots parameter.

# Remember, when we create an object of a class, such as ozwald above (Ozwald is the object of the class Giraffes), we can refer to its variables or functions using the dot operator and the name of the variable or function we want to use example, (ozwald.giraffe_spots). But when we’re creating functions inside a class, we refer to those same variables (and other functions) using the self parameter (self.giraffe_spots).





