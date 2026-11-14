'''
star pyramid pattern:(Equilateral triangle)
    *
   * *
  * * *
 * * * *
* * * * *


   '''
n =  int(input("enter the value:"))
'''for i in range(1,n+1):
    for j in range(1,n+1):
        if j <= n - i:
            #print(i,j)
            print(" ",end="")
        else:
            print("*",end=" ")
    print()'''
#another way
#without using nested loop
#upper part
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))
    #lower part
for i in range(n):
    print(" "*(i+1)+"* "*(n-i-1))
  
