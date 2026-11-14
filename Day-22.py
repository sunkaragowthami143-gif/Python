
'''#usage of varaible length and keyword varible length arguments
def scores(*marks,branch="Codegnan",**names):
    """Scores Scenario with Variable and keyword variable length args"""
    print(marks)
    print(names)
    total = 0
    for mark in marks:
        if type(mark) in (int,float):
            total += mark
    print(f'Total Marks are: {total}')
    for name,value in names.items():
    #for name in names.values():
        print(f'Name : {name}')
        print(f'Value : {value}')
    print(f'Branch is {branch}')

scores(25,20,15,18,16,name="gowthu",place ="Ranchi",batch ="pfs-vsp-007")
        
# position arguments always follows keyword arguments
#non default always follows default args
'''
#scope --> Determines where a variable can be accesed within a program
# A variabe is only accessible  within region where it is define
''' Type of Scope :Local Scope.Global scope,Global keyword,nonlocal Scope

#1.local Scope :variables defined and accesible only inside the functiom...
def fname():
    """usage of local variables"""
    name = "codegnan"
    return f'{name} is in Vizag'
print(fname())
#print(name)# Name error as localScope name is inside the function
print(fname())
name = "Gowthu"
print(name)


#2. Global Variable ---> A variable declared outside all functions is called a global variable.
# it can be accesed from anywhere in the program

name = "codegnan"
def uname():
    """Global Scope"""
    return f'{name} is in vizag,vijaywada,Hyderabad.'
print(uname())
print(name)

# Local variable get the higher priority inside the function
name = "codegnan"
def uname():
    """Global Scope"""
    name="Gowthu"
    return f'{name} is in vizag,vijaywada,Hyderabad.'
print(uname())
print(name)


#3. Global Keyword--->used when we want to modify a global variable
#inside the function
count = 15
def update():
    """ Global Keyword Usage """
    Count =count+5 # unboundLocalError so we need to use  global keywords
    return f'updated count is {count}'
print(update())
print(f'new count is {count}')
values =[ 2,3,45]
values.append(count)
print(values)
#non local scope is used in nested fuctions..allows modification of
#variables from the outer fuctions

def outer():
    """Outer function"""
    count = 10
    def inner():
        """Inner function"""
        nonlocal count
        count = count + 15
        return f'Result from Inner function is {count}'
    print(inner())
    return f'Result from outer function is {count}'
print(outer())
# LEGB --> LOCAL,Enclosing---. Global-->built-in
len =45
a =['codegnan','python']
#print(len(a)) # here we have used built in fuctions as identifiers it fails
#pass by value and pass by object Refrence
# pass by value -->Immutable objects -->int,float,string,tuple
#when immuable objects are passed to function ,changes inside the function
#do not effect the origin value
#original value remains unchange
def update(number):
    """ Pass by value Usage"""
    number = 15
    print("Inside Function:",number)
x = 20
update(x)
print("outside value is 20")

'''

def update(number):
    """ Pass by value Usage"""
    return number * 3
    #print("Inside Function:",number)
number= 20
print(update(number))
print(update(25))

    








    
