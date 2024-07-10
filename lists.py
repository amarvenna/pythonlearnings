countries = ['India', 'Portugal', 'Serbia', 'Spain']
print(countries) # used to print all the items in list
print(countries[0][0]) # used to get specific character in specific string
print(countries[2:]) # from index 2 to till end
print(countries[0:2]) # 0 specifies where to start, 2 specifies where to end i.e it will end at index 1
countries[1] = 'Argentina' # replacing the portugal with argentina
print(countries)
print(countries[-2]) # when we use minus, it starts from back side
print(len(countries)) # returns length
mixedList = ['Amar', 21, 93.5, True]
print(mixedList)
print(type(mixedList)) 
print(type(mixedList[0]))
print(type(mixedList[1])) 
print(type(mixedList[2])) 
print(type(mixedList[3]))  
player = list(('Name', 18, True)) #another way of initialising using list constructor
print(player)
print(type(player))


