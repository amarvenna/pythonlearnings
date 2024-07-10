# stores data in key value pairs
# duplicates in keys are not allowed, unlike in list & tuple
my_dict = {
    'name' : 'Amar',
    'nationality' : 'Indian',
    'age' : 22,
    'isGenius' : True,
    'weight':90.5,
    'family' : ['Teja','Koteswari'] # we can have multiple types in dictionary
}

print(type(my_dict))
print(my_dict)
print(len(my_dict))
print(my_dict['nationality']) # accessing individually