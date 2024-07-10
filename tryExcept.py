try:
    x=int(input('enter value: '))
    print(x)
except:
    print('only int values are accepted..') # this will execute if try runs into error
else:
    print('int value printed..')             #this is executed if try runs perfectly
finally:
    print('try except finished..')            #irrespective to try and except it will execute at last