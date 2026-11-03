'''
#1
n= int(input("Enter the sales"))
if n>1000:
    print("Best Seller")
else:
    print("No Output")

#2
n = (input())
if n == True:
    print("Extra Rain charges Applied")
else:
    print("No output")
#print(type(raining)
  
raining = bool(input())
print(raining)
if raining:
    print("Extra rain charges Applied")
else:
    print("No output")

#3
order_value = int(input("Enter the order_value"))

if order_value > 99:
    print(f'Final Bill Amount:{order_value}')
else: 
    print(f'Final Bill Amount:{order_value}+30')

#4
Budget = int(input("Enter the Budget"))
if Budget >10000:
    print("Plan:Trip")
elif Budget >5000:
    print("Plan:Resort Stay")
elif Budget >3000:
    print(" Plan:Movie and dinner")
elif Budget >1000:
    print("Plan:Cafe and Shopping")
elif Budget >500:
    print("Plan:Street Food and Park visit")
else:
    print("Plan:Stay home")
  '''

#repetition Statements (loops) --> loop helps us in automating repetition
#tasks-->for,while
#usage of for:
#ranges..
'''
Syntax :
    for <temp> in collection/range:
    statemnets(s)....
    ......
    ......
    
marks = [25,10,20,16,27]
#marks can be dynamic
marks = list(map(int,input("Enter the marks:").split(',')))
for i in marks:# i is a marks
    print(i)#it tranverses within the loop
#calculate the total marks
    
marks = list(map(int,input("Enter the marks:").split(',')))
total = 0
for mark in marks:
 total = mark + total   
print(total)
print(f'total marks are:{total}')
print(f'Avg marks are:{total/len(marks)}')

details = {'ids' :[121,131,141],
           'marks':[23,53,15]}
for data in details:
    print(data)
for data in details.values():
    print(data)
for key,value in details.items():
    print(key,value)

#range(stop) -->takes by default minimum value as 0
for i in range(5):
    print(f'value of i is {i}')
    print(f'square of i is {i**2}')
#range(start) -->u can mention start annd stop values
#start is included,end is excluded
for i in range(1,11):
    print(i,i**2)
    print('---->')
 
#range(start,stop,step)
for  i in range(1,21,1):
    print(i)
   
for i in range(1,21,2):
    print(i)
    
for i in range(10,0,-1):     
    print(i)   
     
for i in range(65,91):
    #print(i,chr(i))
    # ord -->('s') and chr(i)
     print(chr(i),end=' ')


names = ['Gowthu','mamatha','deepthi','nikitha']
for name in names:
   #print(name)
    print(name,end=' ') #this is return in horizintal
    
for i in range(len(names)):
    print(names[i])

n = int(input("Enter the value:"))
if n>0:
    result = 0
    for i in range(n+1):
   # print(i)
   result = result + i
    print(f'Result of {i} is {result}')
else:
    print("no output")
 '''
#usage: checking daily workout app usage
work_log = [1,1,1,0,1,1,0]
longest_streak = 0#target
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak =  current_streak + 1
    if current_streak > longest_streak:
        longest_streak = current_streak
    else:
            current_streak = 0
print(f'longest streak is {longest_streak}')





