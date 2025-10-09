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


def spaces(n,y,t):
    occupied=0
    for i in range(n):
        # print(y[i],t[i])
        if y[i]=="C" and t[i]=="C":
            occupied+=1
    return(occupied)
        


print(spaces(5,"CCC..","C.C.C."))

# def spaces(x,y):
#     c=0
#     e=0
#     for car in x:
#         if car=="C":
#             c+=1
#         elif car==".":
#             e+=1
#     C=0
#     E=0
#     for cars in y:
#         if cars=="C":
#             C+=1
#         elif cars==".":
#             E+=1