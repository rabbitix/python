



# Python Collections (Arrays)

# There are four collection data types in the Python programming language:

#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered and unindexed. No duplicate members.
#     Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


# ===============
# access by index - indexes starts from 0 :)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


# Slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# a_list[start:stop:step]

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


thislist = ["apple", "banana", "cherry"]
print(len(thislist))
 

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# make a list with `list(iter)`


# ======= strings =========
text = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(text)


a = "Hello, World!"
print(a[1])


# Slicing
b = "Hello, World!"
print(b[2:5])


# length
a = "Hello, World!"
print(len(a))


a = "Hello, World!"
print(a.split(","))


# https://www.w3schools.com/python/python_ref_string.asp


txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

a = "Hello"
b = "World"
c = a + b
print(c)


a = "Hello"
b = "World"
c = a + " " + b
print(c)


# f string 

name = 'ali'

print(f'my name is {name}')
