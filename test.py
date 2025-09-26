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





bill= input("How much is the bill?")
bill=float(bill)
bill=input("How was the service? Bad,Okay,Good,Great")
Bad=float(0)
Okay=float(0.15)
Good=float(0.2)
Great=float(0.25)

if Bad:
    tip=bill*Bad
elif Okay:
    tip=bill*Okay
elif Good:
    tip=Good*bill
elif Great:
    tip=bill*Great

print(str("Your tip amount is:")+str(tip))
total=tip+bill
print(str("Your total bill is")+str(total))