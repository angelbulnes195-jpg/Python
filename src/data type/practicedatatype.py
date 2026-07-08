# simple data tipe

# str
"Hello World, my name is Angel"

# int
2028

# float
3.1415926535

# boolean
True








# structured data type

# list
list = ["Lion", "Cow", "Horse", "Whale", "Cat", "Beaver"]
list[4] = 3.1415926535

# tuple
tuple = ("Lion", "Cow", "Horse", "Whale", "Cat", "Beaver")

# set
set = {"Lion", "Cow", "Horse", "Whale", "Cat", "Beaver", "Horse", "Lion", "Beaver"}

# dict -- structure = 'key': value,
dict = {
    'name': "Lion",
    'color': "Orange",
    'age': 18,
    'species': "Mammal"
}

# list can be modified, so the following line will print the modified value at index 4, we can also add elements to the list using append() method, remove elements using remove() method, and sort the list using sort() method
list.append("Dog")
print(list[6])

# On the other hand, tuple can't be modified
print(tuple[4])

# set change the order of the elements and remove duplicates, so the following line will print the unique elements in the set
print(set)

# dictionaries are accessed using keys, so the following line will print the value associated with the key 'species'
print(dict['species'])


