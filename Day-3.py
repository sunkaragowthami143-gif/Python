'''age = 22
print(age)
print(type(age))
stock =35
print(type(stock))
batch_rank = 1
print(batch_rank)


#float values
salary = 25000.45
print(salary)
print(type(salary))

temp  = 34.5
print(type(temp))

data = 3 +5j
print(data)
print(type(data))

#boolean  --->True/False

access = True
print(type(access))
result = False
print(type(result))

#none type -->none
#none -->0,false,'',[],(),{},set()

branch_rank = None
print(type(branch_rank))


#Typeconvention -->converting one datatype to another datatype
#explicit  conversion



rank = 5
print(type(rank))
b = float(rank)
print(b)
print(type(b))


c = complex(rank)
print(c)

d = bool(9)
print(d)
print(type(d))

d = bool()
print(d)
print(type(d))

int()
0
float()
0.0
bool()
false
bool(0)
false
bool(none)
false
bool('')
false
bool([])
false


#space is also a character
print(bool([' ']))


price = 45.25
print (type(price))
a = int(price)
print(a)
b = complex(price)
print(b)
c = bool(price)
print(c)



#complex  --->int,float,bool

#signal = 5+6j
# c = int(signal)


acess = True
int(access)


access =True
print (int(access))
print(float(access))
print(complex(access))
print(bool(access))


a = int(float(bool(5)))
print(a)

b = bool(float(int(34)))
print(b)

c = True + 35 + 3.5 + (6+5j)
print(c)

#sequence types --->strings,lists,sets ,dictionaries,frozensets
#string ----> group of characters
#quotations ---> " "' """

place = "codegnan"
print(type(place))
name = "Gowthu"
print(name)

#strings are immutual,ordered,indexed collection

print(len(name)) # len(obj)
print(len(name))
print(len(place))
print(len('Gowthu'))

'''
#Space is also a  character
a = " "
print(a)
print(len(a))

# converting string ----> int,float,complex,boolean
course = "python"
#print(int(course)) #value error
#print(float( course))#raises value error
#print(complex(course))
print(bool(course))



# int ---->str
#float---->str
#complex---->str
#bool------>str



data=56
b = str(data) #it becomes numeric string
print(b)
mileage = 13.5
c = str(mileage)
print(type(c))
d = str(3+5j)
print(d)
e = str(True)
print(e)
























