'''#lists --> A list is an ordered ,multable indexd and hetrogenous collection
#we use [] -->lists
#studnets details,order details,stock entries....
 
details = [1,'gowthu','pfs7','vizag',67.5]
print(len(details))
print(type(details))

stu_ids =  ['CGVIO134','CGVI0135','CGVI0137']
print(stu_ids[2])

stu_ids = ['codegnan'] #here we are using indexing
print(stu_ids[0])

#tuples ----> it is also immutable,oeder,index,heterogence
#collections,we use ()-->parenthesis
#dimensions,coordinates




places = ('hyderabad','vizag','vijaywada')
print(places)
#print(len(places))
#print(type(places))
places[0] = 'chennai'
print(places)


dimensions = 10,20,30 # by default it becomes tuples
print(dimensions)
print(type(dimensions))

# sets --->a set is a unique collection (remove duplicates)
# A Set is  an unordered, unindexed,mutable collection
ids = set()  #empty set
print(ids)
ids = set((123,134,135,123))
print(ids)


courses = { 'PFS' , 'JFS' ,'DA'}
print(courses)
print(type(courses))
print(courses[0]) 

#dictionaries  ---> a dictionary (mapping objets) is a collection of
#key value pairs ---->  dict = {k:v}
details = {'branch' : 'vizag' ,
             'batch' :  ['PFS-VSP-007' , 'PFS-VSP-006' ,'PFS-VSP-005','PFS-VSP-004'],
             ' course' : 'PFS',
             'count'  : 19}
print(details)
print(type(details))
print(len(details))
print(details['batch']) 
print(details['batches']) # we access by giving only keys

# every built -in datatypes is a built in functions
#int,float,str,complex,bool,list,tuple,set,dict

marks = [35,24,54]
a = tuple(marks)
print(a)
b = set(marks)
print(b)
c = str(marks) # its makes every symbol as a character

#print(c)
#print(len(c))

marks = [35,24,54]
#d = dict(marks) # its not possible like this
e = dict.fromkeys(marks)
#taken will become keys and values will be none
print(e)

# tuples ----> list,set,str,dict
#sets ----->list,tuple,str,dict

#dictionaries --->lists,tuples,sets
ids ={1:123,2:234}
a = list(ids) #it will only fetch keys 
print(a)
b= tuple
print(b)
c = set(ids)
print(c)
d = str(ids)  #every symbol/objects will be character
print(d)
print(len(d))

#frozensets ---> its is an immutable set,unindexed,inordered
a = frozenset((12,32,12,32))
print(a)
print(type(a))
print(len(a))

b =list(a)
print(b)
c = tuple(a)
d = set(a)
e = dict.fromkeys(a)
f = str(a)
print(c,d,e,f)
print(len(f))

d = 'gowthami'
e = list(d)
f =tuple(d)
g = set(d)
h = dict.fromkeys(d)
print(e,f,g,h)
'''

# operators
#logic,members,identity,bitwise operators
#ARTHIMETIC ----> +,-,*,/(FLOAT DIVISION),//(FLOOR DIVISION) QUOTIENT
#% modules (REMAINDER),**(EXPONTIAL)
a = 3
b =2
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)









































