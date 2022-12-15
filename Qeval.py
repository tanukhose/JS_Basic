# a=eval(input("enter the data type :-"))
# if type(a)==int:
#     print("int")
# elif type(a)==float:
#     print("float")
# elif type(a)==complex:
#     print("complex")
# elif type(a)==str:
#     print("srt")
# else:
#     print("wrong")

# a=int(input("enter the number :-"))
# c=0
# i=1
# while i<=a:
#     if a%i==0:
#         c+=1
#     i+=1
# if c==2:
#     print("prime")








# i=1
# while i<=5:
#     print(" "*(5-i),end=" ")
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1
# i=4
# while i>=1:
#     print(" "*(5-i),end=" ")
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i-=1


# i=97
# while i<=100:
#     j=97
#     while j<=i:
#         print(chr(j),end=" ")
#         j+=1
#     print()
#     i+=1
i=1
while i<=100:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    if c==2:
        print(i)
    i+=1
