'''
functions --> a reusable block of code
  def fname(parameters): #fun defn --> formal arguments
   """Doc string"""
   statements
   .....
    return value(s)#actual arguments
    there are 5 arguments
   1. postional arguments --->count of arguments to be matched
   2.default arguments ----> we can make argumrnts as default
   3.keyword arguments---->order/keyword name to be matched
   4.variable length arguments --->we can pass any number of postional arguments
   5.keyword variable length arguments(**kwargs)  -->we can pass any number of keyword arguments
   
# 1.positional arguments
--------------------------> #count of arguments to be matched.count is  should be match
def data(a,b,c):
    """Function to perform arithematic operators"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g = a/b/c
    return d,e,f,g
print(data(12,4,1))
#print(data(34,17,))#TypeError as count is missmatch
d,e,f = map(int,input().split()) #space sep values
result =data(d,e,f)
print(f'result is {result}')


#2.default arguments


def data(a,b=5,c=6):
    """Function to perform arithematic operators"""
    d = a+b+c
    e = a-b-c
    f = a*b*c
    g = a/b/c
    return d,e,f,g
print(data(2,4,6))
print(data(12))# here we need not mention other args as they are default
print(data(2,4))#here one default argument taken
print(data())# mandatory should pass atleast one.
#print(data(a=34,6,4))

# 3. keyword arguments -->keyword name to be matched
# grocery purchase

#def grocery(item,price):
#def grocery(item="milk",price):#not at all possible
def grocery(item,price=40):
    """usage of keyword arguments"""
    print(f'Item is {item}')
    print(f'value of item is {price}')
grocery("pizza")
grocery("Milk",35)
grocery(40,"bread") #in this case order differs result changes
grocery(item='jam',price = 60) #TypeEror -->keyword argument mismatched
 '''
# 4. variable length arguments ---> we can capture any number of positional
# arguments ,we use (*args),captures excess positional argumets and
# pack them into tuple..

def sample(*a):
    """ usage of arbitrary arguments"""
    print(a)
    print(type(a))
sample()
sample(1,2,)
sample('gowthami','codegan')
sample([12,14,5,7,9])
















