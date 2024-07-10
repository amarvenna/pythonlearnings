list1 = [2,5,4,7,9,1,4]
list2 = ['banana','cherry','dosakai']

print(list1)
print(list1.count(4)) # counts occurences of element
list1.remove(4) #removes specified element
print(list1)
list1.sort() # sorts in ascending order
print(list1)
list1.extend(list2) # merge two lists
print(list1)
list2.append('carrot') # appends at last
print(list2)
list2.insert(0,'apple') # inserts at specified index
print(list2)
list2.reverse() #reverse all the elements inside it
print(list2)
list2.pop() # pops last element out
print(list2)
list2.pop(0) # removes specified index value
print(list2)
list3 = list2.copy() #duplicates one list to another 
print(list3)
del list2[2]
print(list2)
list2.clear() # returns empty list
print(list2)




