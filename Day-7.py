'''
sequences --> string ,lists,tuples,sets,frozensets,dicts
string --> A String is a group of characters,it is immutable ,orderd,indexed,collection.we can denote it in single,double
or triple..

data = ' '#empty string
print(data)
print(type(data))

#operations -->concenatio,repetition indexed ,slicing
sub1 = "python"
sub2 = "Mysql"
print(sub1+sub2)
print(f'{sub1},{sub2}')

#Repetition -->String can be repeated any number of iteams with avalid int
print("*")
print('*' *10)
name = "Gowthu";place = "vizag"
print(f'{name * 10}*')
print(f'----->{name} is in ----->{place}')


#membership -->in,not in
print("jay" in "Ajay")

#Indexing -->accessing each position (index) is an object
#its starts at 0 to ends
#positive indexing
name = 'Gowthami'
print(name[3])
print(name[5])
#print(name[11])#false because out  of range
#negative indexing
print(name[-0])
print(name[-3])

#slicing -->group of characters -->[start:end]
#excluded (len(obj)-1)
name = "Gowthami"
print(name[0:5])
print(name[4:7])
print(name[0: ])#returns all characters
print(name[4:7])
print(name[5:7])
print(name[:])#returns all characters
print(name[5:1])

name = "gowthami"
print(name[ :-4])
print(name[2: ])
print(name[5:3])
print(name[-1])
print(name[-4:-7])#returns empty

# task --> create a string and explore above possibiltes




#striding --->[start:end:step]
s = "gowthami"
#print(s[::0])# returns values error
print(s[ :2])# skips each alternative element from beginning 
print(s[::4])
print(s[7:5])
print(s[1:7:2])# first perform [1:7] then skip one element
print(s[4:2])

# what ifwe give -1
s = "visakhapatnam"
print(s[::-1])
print(s[1:3:-3])
print(s[:4])
# Built in functions -->type(),len(),min(),max(),ord(),char(),sorted()
password= "admin123"
print(len(password))
print(type(password))
print(min(password)) # min() returns min object in collection
#ASCII values
print(ord('a'))
print(ord('A'))
print(ord('Z'))
print(chr(120))
print(sorted(password))
'''
# task --> create a string and explore above possibiltes
a = "Gowthamisunkara"
print(a[:3])
print(a[2: ])
print(a[: :])
print(a[2:10:2])
print(a[: : 3])
print(a[: -4])
print(a[-5:])
print(a[-7:])
print(a[1:-6:3])





