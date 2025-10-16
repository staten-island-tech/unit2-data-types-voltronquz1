import random

# bill= input("How much is the bill?")
# bill=float(bill)


# tip=bill*0.18

# total= tip + bill
# print(str("Your total is ")+ str(total))

# values = [1,2.23,5,7,2,30,15]
# print(values)

# print(values[0])
# print(values[6])


# x=input("Do you want to buy  thing? (y/n)")

# while x is not "n":
#     item=input("what yu wanna buy")
# print("thanks for purchase")



# y=random.randit(1,100)
# print(y)



# x = "this is a thing"
# y= x.split()
# z = y[0]
# print(y)
# print(z)
 # ASSESSMENT
# Sent= input("Input a sentence")
# Sentence = Sent.split( )
# z=len(Sentence)
# print(z)

# day_of_week = input("what day is it? ")
# if day_of_week == "Friday":
#     print("correct")
# else:
#     print("incorrect")

# x = "test"
# print(f"hello {x}")




# temp = 75
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:
#     print('cold')


# odd=int(input("Give me a number"))

# if odd%2 == 0:
#     print("even")
# else:
#     print("odd")



# CHALLENGE 2

# bill= input("How much is the bill?")
# bill=float(bill)
# service=input("How was the service? Bad,Okay,Good,Great: ")
# Bad=float(0)
# Okay=float(0.15)
# Good=float(0.2)
# Great=float(0.25)
# tip=0
# if service == 'Bad':
#     tip= bill * Bad
# elif service == 'Okay':
#     tip=bill * Okay
# elif service == 'Good':
#     tip=Good * bill
# elif service == 'Great':
#     tip=bill * Great

# print(str("Your tip amount is: ")+str(tip))
# total=tip+bill
# print(str("Your total bill is ")+str(total))


# CHALLENGE 3
# factors= []
# x=int(input("give me a number to factor"))
# for i in range(1,x+1):
#     if x%i==0:
#         factors.append(i)
# print(f"The factors of {x} is {factors}")
#GCF CHALLENGE 4
num1=input("give me a number")
num2=input("give me anothe number")
fac1=[]
fac2=[]
cf=[]
def gcf(x,y): 
    for i in range(1,num1+1):
        if num1%i==0:
            fac1.append(i)
    for i in range(1,num2+1):
        if num2%i==0:
            fac2.append(i)
    for i in fac1:
        if i in fac2:
            cf.append(i)
        gcf=max(cf)
print("Gcf of {num1} and {num2} is {gcf}")





