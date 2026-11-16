
'''#pass of refernce -->when mutable objects(lists,sets,dict) are passed into the functions
#changes inside the functions  affect the original obkect...

def update(items):
    """We will assume items as list"""
    #items.append("laptop")
    items.extend(["laptop","power bank","camera"])
cart = ["mobile","Watch"]
print(update(cart)) #returns none
print(cart)#original list changes
#print(update("gowthu"))#raises  Attribute error

#Dictionary Usage: -->updating profile
def update(profile):
    """usage of Dictionary"""
    profile['branch'] = "vizag"
students = {'names':['gowthu','deepthi','mamathaa']}
pfs_studnets ={'batches':['PFS-VSP-007','PFS-VSP-OO6','PFS-VSP-005'],
                 'subjects':['python','MYSQL','Aptitude']}         
update(students)
print(students)
print(pfs_studnets)
update(pfs_studnets)

#pass by value -->original data will not change,immutable objects
#pass by objects reference -->original data will change ,mutable objects

#built -in functions -->functions which are built in python
#print(),len(),min(),max(),sorted(),int(),float(),bool(),complex(),str()
#list(),tuple(),set(),dict(),input(),eval(),help()

print(dir())
#print(dir('__builtins__'))
#print(dir(__builtins__)) # returns list of built functiona and errors
#print(help(print))
#print(help(len))


#abs(),chr(),ord()
print(abs(-34)) #returns the absolute value of a numbers
print(chr(67))
print(ord('@')) #returns the ASCII value
data = [24,56,21,0]
print(any(data))  #any() --> compares bool(x) for any valuer -->True
print(all(data))  #all() --> needs all values to be present
#print(all(none))
print(all([None]))
print(bin(6))  #returns binary object
print(help(enumerate))
data=["Gowthu","Deepthi","Mamatha"]
c =dict(enumerate(data))
print(c)
d=dict(enumerate(data,1))
print(d)


'''
#zip --> it combines multiple collections into a single collection
data =["Gowthu","Mamatha","Deepthi"]
marks = [25,28,30]
f = dict(zip(data,marks)) # zip check for length matching
#f = list(zip(data,marks))# list 
print(f)









