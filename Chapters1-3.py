# Python reads code from top to bottom so if a var is redefined than it is overwritten
# This also means that you must declare your variables before calling for them 

# =========================================== PRINT STATEMENTS, DECLARATIONS, INSERTS =========================================================
# print statement  
print("hello world")

# PEMDAS
print (6 + 5)
print (4 * 2)
print (2 - 2)
print (2 / 1)

# Declaring an int
Lydia = 64 
print (Lydia)

# You can have both letters and numbers in a variables declaration
Num2 = 2
print(Num2)

# using the new line command 
print ("You are \n dumb")

# making string blocks 
print ("""You are
the best dog
in the world """)

# understanding apostrophes, best practice is to use double quotes 
print ('Marku\'s')
print ("Mark's cute dog")

# inserting variables into strings
score = 1000 
message = ("My score %s points")
print(message % score)

# Idk nick did this 
name = ("who are you? ")
name = ("Markus")
# f is a format string literal
print (f"hello %s" % (name))

# Inserting multiple variables into strings (dynamic change) 
messages = ("These are my messages: %s and  %s")
print(messages % (0.6, 8))
print (messages % ("T", 7))
print ( message % ( name))

# 
print ("this is" , 3 , "stupid")

# mess = ("This is" + 1)
mess = (22 * "l")
print(mess)


spaces = ' ' * 25
print('%s 12 Butts Wynd' % spaces)
print('%s Twinklebottom Heath' % spaces)
print('%s West Snoring' % spaces)
print()
print()
print('Dear Sir')
print()
print('I wish to report that tiles are missing from the')
print('outside toilet roof.')
print('I think it was bad wind the other night that blew them away.')
print()
print('Regards')
print('Malcolm Dithering')

# Yusuf = ("Pretty cool %s and he is ")
# Age = (2)
# print(Yusuf % Age)

# Python has lists instead of arrays 
# They are both 0 indexed and lists are defined with []

# Python decalres variables based on value rather than predefining them: name = String, Shweta = int, check = boolean
name = "Markus "
Shweta = 3
check = True

# ===============================================  LISTS, TUPLES, SETS, + DICTIONARIES =======================================================

# Lists are ordered, changeable, and allow duplicates 
wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
print(wizard_list[0:2])

numList = [1,2,3,4,5]
print(numList)

# This is a set which is unordered and unindexed, it will print everything
mySet = {1,2,3,4,5}
print(mySet)

# This is a tuple which is ordered and unchangeable
# They are 0 indexed like lists/arrays but are unchangeable like constants 
# example call of the index with (...[0])
myTuple = ("Shweta", "Lydia", "Markus", "Laura")
print(myTuple[1])

# Dictionaries are ordered, changeable, and do not allow duplicates
# Dictionaries are like key pairs 
myDictionary = {
    "Name" : "Markus",
    "Age" : 2,
    "Float" : 2.4,
    "MySet" : mySet
}

myDictionaries = {
    "Name": "Markus"
}
print(myDictionary)
print(myDictionaries)

# You are able to have both string and int values within a list 
newList = ["Laura", "found", 5, "snakes"]
print(newList)

newestList = [wizard_list, newList]
print(newestList)

# Adding items to the list, always shows up at the end of the list
newList.append("in bow ties")
print(newList)

# Removing items from the list based off of their index 
del newList[0]
print(newList)

# Adding lists together just puts the values of the second list after the first 
addedList = newList + wizard_list
print(addedList)

# You can mult lists just like you could add them 
# Just like if you did numList + numList
multiplyingLists = numList * 2 
print(multiplyingLists)

# Dictionaries work the same as lists but can't have repeating keys
# To call upon the value you would call its key (index value)
# You cannot join maps together like you could lists
# Complicated Excel spreedsheat

myDict = {
    "Shweta" : "bee",
    "Laura" : "snake",
    "Markus" : "snake"
}
print (myDict)
print(myDict["Shweta"])

# Changing the value of a key in a dictionary 
myDict["Laura"] = "ladybug"
print(myDict)







