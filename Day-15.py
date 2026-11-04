'''
usage of for with conditional statements
normal completion --->looping is going thruogh the entire sequence naturally
else block will run
Interecption -->break

#notifications =[0,0,0,0]
notifications = [0,1,1,1,0]
#0--> notification read
#1 --> unread notification
#notification checker
for notification in notifications:
    if notification == 1:
        print("unread Notification")
else:
    print("All Notification are caught up")


# searching scenario same above program to be transform -->
#if target  is found
#notifications =[0,0,0,0]
notifications = [0,1,1,1,0]
#0--> notification read
#1 --> unread notification
#notification checker
for notification in notifications:
    if notification == 1:
        print("unread Notification")
        break # its stops exits early the else block will be skipped
else:
    print("All Notification are caught up")
   
#searching in a list
#you want to handle the "item not found" case
fruits = ["apple","banana","mango","kiwi"]
item = input("which fruit you want:")
for fruit in fruits:
    if item == fruit:
        print(f'you got your desired {item}')
        break
else:
    print(f'could not find {item} in the  fruits')
'''
#continue ---> will skip the current iteration and proceeds for the remaining iteration
'''
fruits = ["apple","banana","mango","kiwi"]
item = input("which fruit you want:")
for fruit in fruits:
    if item == fruit:
        print(f'you got your desired {item}')
        continue 
else:
    print(f'could not find {item} in the  fruits')


#observe by the modifying usage of break and contiune with else blocks
notifications = [0,1,1,1,0]
#0--> notification read
#1 --> unread notification
#notification checker
for notification in notifications:
    if notification == 1:
        print("unread Notification")
        break
else:
    print("All Notification are caught up")

# while -->loops -->it is mainly used when we rely condition,
#it will be completly excuted until the conditions is executed

while <condition>..
      statement(S)
while True:
      print("yes")

#initalizer with which we need to intialise
i = 0 #initialised statement
while i<=10:
      print(i)
      i=i+1
      
i = 10
while i>=1:
      print(i)
      i=i-1#decremnet
'''
i = 1
while i<=10:
      print(10-i)
      i = i+1









        
