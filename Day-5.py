'''
operators -->operators  help to perform operations between oprends
arithemrtic  operators -->+,-,*,/, **,//,%(modulus -->remaider)
Assignment -->it helps to assigns,update(increment,decrement) values
# = (assignemt), +=(adition&assign) ,-=(subtraction&assign),*=(multiplication&assigns)

data = 20
print(data)
print(type(data))

stock = data
print(stock)
#INCREMENT THE VALUE OF STOCK
stock =stock+5 #stock+=5
print(stock)

#decrement the value of data by 2 value

data = data -2
print(data)
stock-=data
print(stock)

stock =100
stock*=2 #**-->square number
print(stock)
 
# comparsion operators (relational operators )-->it performs comparsions
#between the opreands and results in boolean True/False  ---> condtions
# ==,!=,<=,>,>=
name = 'vinay'
vinay_attendance = 75
print(vinay_attendance == 80)
print(vinay_attendance >= 80)
print(vinay_attendance <= 80)
print(vinay_attendance < 80)
print(vinay_attendance > 80)
print(vinay_attendance != 80)

#logical operators -->and,or,not(keywords)
#and --> it needs al conditions to be satisfied(two or more)
#0r ---> it needs any one condition to be satisfied
#not ---> opp to existing 

max_marks = 80
vinay_marks = 75
max_att = 75
vinay_att = 70
vinay_marks +=10
certificate = vinay_marks >= max_marks and vinay_att >= max_att
print(certificate)
chance = vinay_marks >= max_marks or vinay_att >= max_att
print(chance)


data = []
print(data)
print(not(data)) # returns True

data = [1,2,3,4]
print(not(data))# returns false because as data is existing
# both logical and comparsion operators will returns in boolean


# membership operators ---> IN,NOT IN
Name = ['gowthu','mamatha','nikitha','deppika']
name = 'rama'
print(name in name)
print(name not in name)
print('12' in '121')
# print(12 in 121) #typeError as we have taken int type)


print('ajay' in 'ajay')# string to string -->True
print(['ajay'] in ['ajay']) # list to list-->false



#Identity operators -->it specifically refers to object(memory location)
#id--> is, is not 

a = 15
b = 15
print(a==b)
print(id(a))
print(id(b))


c = a
print(id(c))
print(c is a)#as id of both a and c are same -->True

a = [1,2,3,4]
b = [1,2,3,4]
print(a == b)
print(id(a))
print(id(b))
# as  we have taken two lists eventhough with similar values identity
print(a is b)
c = a
print(id(c))
print(c is a)


# when we check with the Interpreter mode and scripting mode above
# tuple result changes
# logical,membership, identity,comparsion(relational) -->always result is in boolean


#bitwise operators --->it performs bitwise opreations --->&(bitwise and)
#| (botwise OR),^(bitwise XOR)
#AN Integers will be converted binary format and performs bitwise operation
#following integer to binary conversion

print(7 & 3)
print(7 | 3)
print(7 ^ 3) # XOR operation it returns  4
# 7 to binary -->0111
# 3 to binary -->0011
# 7^3 --> 0100
'''
#shifting operators (<< , >>)
print(7 << 1)





























