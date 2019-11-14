# A function is a block of code which only runs when it is called.


def my_function():
    print("Hello from a function")


my_function()


# with parameter

def function(fname):
    print(fname + " Refsnes")


function("Emil")
function("Tobias")
function("Linus")


# default value
def my_func(country="Norway"):
    print("I am from " + country)


my_func("Sweden")
my_func("India")
my_func()


# a list as parameter
def fun(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

fun(fruits)

# returning value


def func(x):
    return 5 * x


print(func(3))
print(func(5))


# This way the order of the arguments does not matter.

def function2(child3, child2, child1):
    print("The youngest child is " + child3)


function2(child1="Emil", child2="Tobias", child3="Linus")


# ============= Classes ========

# classes has property and methods

#  Methods in objects are functions that belong to the object.
class Person:
    size = 'x'  # this is a property

    def set_name(self, name):  # this is a method
        self.name = name

# All classes have a function called __init__(),
#  which is always executed when the class is being initiated.

# Use the __init__() function to assign values
#  to object properties, or other operations that are necessary to do when the object is being created:


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getst(self):
        print('nothing')



p1 = Person2("John", 36)

p1.getst()

print(p1.name)
print(p1.age)


# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age

#     def myfunc(abc):
#         print("Hello my name is " + abc.name)

p1 = Person(1)
p1.set_name('alex')


# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class sth:
    pass


# ================ Files ===============
'''
The key function for working with files in Python is the open() function.

open has a mode argument


"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

'''

# Reading a file

f = open('fileName.txt','r')

print(f.read()) # read all texts in a file
print(f.readline()) # read a line
print(f.readlines()) # return a list of lines

f.close() # to close a file

# ==== Write in file

'''
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
'''

f = open("a.txt", "a")  # this will append
f.write("Now the file has more content!")
f.close()



f = open("a.txt", "w")  # this will overwrite it
f.write("Now the file has more content!")
f.close()