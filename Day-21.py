
'''# 4. variable length arguments ---> we can capture any number of positional
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


#In above case we used '*' to pack the values into a tuple
a,b,c = 2,4,-6
print(a,b,c)
a,*b,c=2,4,5,6,65,12,-12
print(a)
print(c)
print(b) # in this call all values are stored into list
#a,*b,c = 2,4,5,6,64,31,-12
print(a)
print(c)
print(b)


# find the sum of values
def add(*a):
    """usage  of variable length arguments"""
    #print(a)
    #print(type(a))
    print(a)
    result = 0
    for value in a:
        #if type(value) in (int,float):# membership operator
        if type(value) == int or type(value) == float:
            result = result + value
                #print(result)
    return result
#print(add())
#add(1,3,4,5) # 1+3+4+5 --->13
#add(12,2,4,5,-76,6)
#print(add(1,2,4,-2,'codegnan',2,12,'gowthami'))
#what if we accept group of values
d = list(map(int,input().split()))
print(d)
print(add(*d)) #we need to use * to unpack the values from the tuple

# we will use above usage of variable length arguments for ordering pizza 

def order_pizza(size,*toppings):
    """usage of *args """
    print(f'Size of pizza is {size}')
    #print(f"Topping:{toppings}")
    for topping in toppings:
        print(f'Topping added : {topping}')
order_pizza("large","onions","panner","capsicum","olives","mushrooms")

# 5. keyword variable lenght arguments :any number of keyword arguments,
#data is stored in dictionary, we can **kwargs...

def sample(**a):
    """usage of **kwargs"""
    print(a)
    print(type(a))
sample()
sample(name="gowthami",batch="pfs-vsp-007",place="vizag",branch ="CSE",course="PFS")
'''


def order_pizza(size,*toppings,**details):
    """usage of *args """
    print(f'Size of pizza is {size}')
    #print(f"Topping:{toppings}")
    for topping in toppings:
        print(f'Topping added : {topping}')
    for key,value in details.items():
        print(f'Data is {key},result is {value}')
order_pizza("large","onions","panner","capsicum","olives","mushrooms",
            name ="Gowthami",
            bill = 200,
            delivery=False,tip = 50)








