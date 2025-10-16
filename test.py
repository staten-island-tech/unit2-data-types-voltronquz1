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
# GCF CHALLENGE 4
# num1=input("give me a number")
# num2=input("give me anothe number")
# cf=[]
# fac1=[]
# fac2=[]
# def gcf(x,y): 
#     for i in range(1,num1+1):
#         if num1%i==0 and num2%i==0:
#             gcf.append(i)
# print(gcf)




def gcf():  #defines gcf as a function
    number1 = int(input("Enter 1st number:"))
    number2 = int(input("Enter 2nd number:"))
    common_factors = []
    list_of_factor1 = []        #list for store the factors
    list_of_factor2 = []
    for i in range(1, number1 + 1): #for anynumber/i between of i and number1, start at 1 and keep add 1 to number1
        if number1 % i == 0:    #divide number1 + 1 by i and if remainder = 0 store fir list1
            list_of_factor1.append(i)
    for i in range(1, number2 + 1): #for anynumber/i in range of i and number2, starts at 1 keeps adding 1 to number2
        if number2 % i == 0:    #divide number2 + 1 by i and if remainder = 0 store for list2
            list_of_factor2.append(i)
    for i in list_of_factor1:
        if i in list_of_factor2:        #check for same numbers in both lists and founded same numbers get add to common_factors list
            common_factors.append(i)
    gcf = max(common_factors)   #max find biggest number in common_factors list and define it as variable gcf
    print(f"The GCF of {number1} and {number2} is {gcf}")

gcf()
