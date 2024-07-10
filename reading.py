countriesList = open('countries.txt','r')
print(countriesList.readable()) #returns boolean value if it is readable or not
print(countriesList.readline()) # reads first line
print(countriesList.readline()) # reads next line sequentially
countriesList.close()

# print(countriesList.readlines()[0]) # using index to specify line
# print(countriesList.readlines()) # reads all lines
'''using for loop to read all countries
   for lines in countriesList:
       print(lines)
'''