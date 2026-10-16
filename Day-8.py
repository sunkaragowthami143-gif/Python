'''
string methods -->case conservation ,replacing,finding,white trailing spaces,testing methods,
allignment methods

#case conversation -->upper(),lower(),title(),capitalize(),swapcase()
data = "codegnan"
print(type(data))
#print(dir(data)) # dir() returns available methods/function

#upper()---> converts objects to upper case
print(data.upper())
e = data.upper()
print(e)

#lower()-->conerts to lowerr
f = data.lower()
print(f)

##captitalize() --->it will capitalize the first letter in the word
print("codegnan vizag".capitalize())

##title()-->it will capitalize every first letter in each word
print("codegnan vizag".title())

#testing methods (which will give the result as boolean(True / false)
#isupper(),islower(),isalnum(), isalpha ,isdigit()...
print("SUnkArA GOwthaMI".swapcase()) #converts upper to lower and lower to upper
print("gowthami".isupper())
print("gowthami".islower())

print("sunkaragowthami".isupper())
print("sunkaragowthami".islower())
print("admin123".isalpha())
print("admin123".isalnum())
print("47382".isdigit())
print("47382".isalnum())
print("Python".istitle()) # it returns true because starting letter is upper case
print("Python aptitude".istitle()) # it returns false because both word are not havinh upper case only one word 

print("Gowthami".startswith('G'))
data = "python Aptitude"
print(data.startswith("A"))
print(data[7:].startsth("A"))
print(data.startswith("A",7))
print(data.endswith("e"))
print(data.endswith("n",0,6))
print(data.endswith("o",0,6))

print("12.34".isalnum())
print("12.34".isdigit())
print("III".isnumeric()) # roman numbercase will possibile but we need to encode the data
print("2".isnumeric())
print("½".isnumeric())# fractions ,romans numerics


#finding and searching methods-->find(),index(),count()
data =" codegnan is in vizag"
print(data.find('a')) # returns only first occurance
print(data.find('a',7))# here we will check for the next occurances
#find() will returns -1 if the given object is not present
print(data.find("a"))
print(data.index("e"))#it returns the  first occurence
#if given object is not present it raise value error
#print("querty".index("s")) # raise value error
print("querty".index("werty")) #as substring is strating with 'w'

#rindex() returns last occurances
print("qwertywerty".rindex("y"))

#count() will return total number of occurance
print("codegnan".count("n"))
print("codegnan".count("t")) #returns 0 as 't' is not present

#split(),join(),strip(),lstrip(),zfill()
a = "python Apitude Softskills MYSQL"
b = a.split()# by default space is treated
print(b)
a = "python,Aptitude,softskills.MYSQL"
c = a.split(',')# by comma
print(c)

#join()
print("code".join("gnan")) # concatenates every object with the given iterable
print("#".join("Gowthami"))
print(" ".join("Gowthu"))
print("*".join("Gowthu"))
#white space & Trimming Methods----> strip(),lstrip(),rstrip()
a =  "gowthami"
print(len(a))
a = a.strip()
print(len(a))

#allignment methods --->zfill()
#pads zero from left
print("python".zfill(10)) # zfill() make sure to pass width >len(10)
print("codegnan".zfill(1))

print("codegnan".center(10,'*'))
print("python".ljust(10,'*'))# returns the leftjustified string 

print("python".rjust(10,'*')) #returns the rightjustified string
'''
# sequence -->lists[],tuples(),sets set(),frozensets,dicts{}

