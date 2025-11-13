# Assessment Pratice
# def lang(x):
    # print(x[0])
    # for char in x:
    #     print(char)

# def language(x):
#     print("do something")
# lang("Cadee computer never seems to work in the morning")



# def lang(x):
#     s=0
#     t=0
#     for char in x:
#         if char=="s" or char=="S":
#             s+=1
#         elif char=="t" or char=="T":
#             t+=1
#     if s>t:
#         print("E")
#     if s<t:
#         print("F")
# lang("Lorsque j'avais six ans j'ai vu, une fois,")

# Pratice 1
# def spaces(n,y,t):
#     occupied=0
#     for i in range(n):
#         # print(y[i],t[i])
#         if y[i]=="C" and t[i]=="C":
#             occupied+=1
#     return(occupied)
        


# print(spaces(5,"CCC..","C.C.C."))



def honi(y):
    honicounter=0
    h=0
    o=0
    n=0
    i=0
    for i in range(honi):
        len(honi)
        if y[i]=="H":
            h+=1
        if y[i]=="O": 
            o+=1 
        if y[i]=="N":
            n+=1
        if y[i]=="I":
            i+=1
            if y[i]:
                honicounter+=1
            print(honicounter)
honi("HHHHOOOONNNNIIII")


# def mc(n,s,a):
#     correct=0
#     for i in range(n):
#         if s[i]==a[i]:
#             correct+=1

# def pass(x):
#     lower=0
#     upper=0
#     digit=0
#     if len(x)>8 and len(x)<12:
#         for char in x:
#             if char.islower():

# def elder(o,n,duels):
#     owner=o
#     owners=1
#     for i in range(n):
#         if duels[i][1]:
#             owner=i[0]
#             owner=owners+1

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
