for letter in 'Amareswara':
    print(letter)

mylist = ['sa', 're', 'ga', 'ma', 'pa']
for values in mylist:
    print(values)

for values in mylist:
    if values == 'ma':
        break
    print(values)

my_dict = {
    'name' : 'Amar',
    'nationality' : 'Indian',
    'age' : 22,
    'isGenius' : True,
    'weight':90.5,
    'family' : ['Teja','Koteswari'] 
}

for values in my_dict:
    print(values)          # it is printing only key values

for x in range(5,10):
    print(x)
else:
    print('Loop finished!..')