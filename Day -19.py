'''
python --->pop,oop
pop -->procedure oriented programing-->
functions ---> a function is a block of statements(code) which performs a specific task
it is a reuseability code-->readbility,reuseability,easy to maintain....

types  of functions-
---------------------
1.user defined function -->def
2.bulit in functions---> python by default (print,len,max,min,sorted,str,list,bool,dict....)
Anonymous functions ---> nameless function -->lambda (map filter)
Recursive functions ----> recursion -->factorial,fibonnacci---> decorators
'''
# 1.user Defined Function
'''
Syntax:
    def fname(parameters): #functions header
        """Doc string (descripition of functions)"""
        statment(s) .......#body of function
        ..........
        return values(s)
        fname(args) # function call
   '''
# simple functions to understand the reuseability

'''
a = 10
b = 15
print(a+b)

#we can function sum or add
def add(a,b):
    """ this function return the summ of given objects"""
    c = a+b
    #print(c)
add(14,20)
add(20,45)
add('code','gnan')
add([1,2],[3,4,5])

#or
def add(a,b):
    """ this function return the summ of given objects"""
    c = a+b
    #print(c)
    return c
print(add(14,20))
print(add(20,45))
print(add('code','gnan'))
print(add([1,2],[3,4,5]))

#another way
def add(a,b):
    """ Sample Add functions"""
    return f'Result is {a+b}'
c,d=map(int,input().split())
print(add(c,d))
print(add("code","gnan"))
g,h = 67,-43
e = add(g,h)

print(e)
'''
# function are also objects
def greeting():
    """Greeting to the user"""
    return"hey guys welcome to codegnan"
    #return 24+256# a function can be have multiple values to return but not
    #multiple return statments
    #return"hey guys","python","PFS--VSP--OO7"
    return len(("hey guys","python","PFS--VSP--OO7"))
#print(greeting())
print(greeting() * 5)
print(type(greeting)) # Return the function
print(type(greeting()))# return type of function















