'''
Tokens -->operators

control statements -->these are the statements which makes the programing flow to be possible.
they control the entire of the program
---->when to excute,ehat is excute,how to excute
---->conditional statements --->if,else,elif
---->jumping statements ---->break,continue,passs
assert,try,except ,finally
---->repetition statements(loops)--> for ,while
'''
#conditional Statements -->statements rely on the condition
'''
syntax if:
if <condition>:s
     Statement(s)...
     .....

#data = false
data = True
if data:
    print("welcome to codegnan")
    print("This is PFS-VSP-007")
    print("today is friday")

#mark = 25
mark = int(input("Enter a value"))
marks =[12,14,16,25]
if mark in marks:
    print("Marks successfully fetched")
    print(f'Marks are{mark}')
print(f'its done for the day')

stock = int(input("enter the value"))
total_stock = 100
if stock >0 and stock < total_stock:
    print(f'you can  order the item')
    print(f'item selected and placed into cart')
    print(f'item ordered')
else:
    print(f'Invalid entry)

#usage of else:
if <condtion>:
statement(s)...
else:
statement(s)..

 #task
          
age = int(input("enter the age")
if age > 18 and age < 18 
    print(f'eligible')
    print(f'not eligible')
else:
    print(f'wait to get vote eligiblity')

  
algo:
accept the input from the user
make the eligiblity case as age greaterthan equal to 18:
elgiblity granted
if age is not matching eligibility:
inform  number of years to wait

 Dry run:

 Age -->19 --->result -->19 >= 18 and 19>0
 age --->12 --->result--->18-12-->6
  
  #code
age = int(input("Enter the age:"))
if age > 0:
   if age >0 and age >=18:
       print(f'You have Vote Eligibility')
       print(f'Use your vote right to get the change---->')
   else:
      print(f'If you need to wait for{18-age} years')
else:
    print(f'Enter only +ve values for the age')


#if-elif-else-->we wanted to map multiple conditions
if condtion1:
    statement(s)...
elif condtion2:
    statement(s)...
elif condition3:
    statement(s)...
else:
    statement(s)...
    ......

age= int(input("enter the age:"))
if age>0 and age>=18 and age<=100:
    print(f'You have Vote Eligibility')
    print(f'Use your vote right to get the change---->')
elif age>0 and age<18:
    print(f'you need to wait for{18-age} years')
else:
    print(f'Invalid Age entry--->Entry only +ve values')
'''
#task --> placement elegiblity Tracker/system
print("------placement eligible checker-------")
name = input("enter the name of the student:")
attendance = float(input("enter the attendance of the student:"))
Technical_score = float(input("enter the Technical score:"))
mock_interview_score = float(input("enter the mock Interview score:"))
projects = int(input("enter the number of the projects"))

avg_score = (techical_score + mock_interview_score)/2
if attendance >=75 and avg_score >=75 and projects >2:
    print(f'result:student is placement ready he/she falls in hotlist')
elif attendance >=60 and avg_score >=60 and projects >1:
    print(f'result:student need more preparation -->Improvement Stage')
else:
    print(f'result:student is in foundation stage --->need practice session')

         
         
         
    



          
          
          
    
