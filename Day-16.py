'''
while -->intialized statement,counter..

#banking scenario --->PIN authentificatoin if more than
# 3 attempts account locked
pin = "2612"
max_attempts = 3
#you need to have a current attempts
current_attempt = 0
while current_attempt < max_attempts:
    enter_pin = input("Enter the ATM Pin")
    if enter_pin == pin:
        print("login succesful")
        print("withdraw the money...")
        break
    else:
        print("Entered PIN is wrong.try again carefully")
        current_attempt += 1
else:
    print("Account Locked... try again after 24 hours")
'''
#BMI scernario (usecase),we will makesure of control block statements:
#BMI -->body mass index --->bmi = weights(kgs)/(heights**2) (meters)

'''
feet -->1 feet -->12 inches ---> 2.54cm -->30.48 cms
----> 5 feet 6 inches ---> 167.78 cms -->1.67 metres


n = int(input("how many users:"))
for i in range(n):
    weight = int(input("enter the weight in kgs:"))
    height = int(input("enter the height in metres:"))
    if weight > 0 and height > 0:
        bmi = (weight)/((height)**2)
        #print(bmi)
        #(<18.5  --> underweight,18.5  -24.9 --> healthy.25-29.9 -->overnight
        #>=30 --> obesity)
        if bmi < 18.5:
            print(f'{name} -->you are underweight as BMI is{bmi}')
        elif bmi >= 18.5 and bmi <=24.9:
            print(f'{name} -->you are in perfect physique,BMI is {bmi}')
        elif bmi >=25 and bmi <=29.9:
            print(f'{name} --> you are overweight need to maintain diet,BMI is {bms}')
        elif bmi >30:
            print(f'{name} -->obesity ,BMI is {bmi}')
    else:
        print(f'enter only + values')


#task : --> for same above BMI calculator ,store the details in dictionaries
#BMI_result ={'names':['akash','vinay','sandeep'],
               'BMI_value':[24.657,25.456,28.945]}
               
'''
#assert --->it is mainly used in debugging checkingb during  checking during development
# it tests wherther a given condition is satisfied or not its
#a madatory else it will raise the error .it is mainly used
#to catch
#by ensuring the conditions hold true..

#syntax: assert<condintion> "error message"
x = int(input("enter the value :"))
#assert x>0
assert x>0,"enter the values" 
x = x**2
print('f final result is {x}')
assert x in [24,25,12,10],"checking the data"
print(f'search found')



















