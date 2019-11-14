# Dictionary

# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# You can access the items of a dictionary by referring to its key name, inside square brackets:


x = thisdict["model"]


x = thisdict.get("model")


# Change Values
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018


for x, y in thisdict.items():
  print(x, y) 


  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


# ================
# package manager
