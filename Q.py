# a=["mom","bro","sister","dad",'nitin']
# count=0
# i=0
# while i<len(a):
#     b=a[i]
#     rev=b[::-1]
#     if b==rev:
#         count+=1
#     i+=1
# print(count)


# a=[101,102,103,104,105]
# b=[]
# i=1
# while i<len(a):
#     b.append(((a[i]+(9*i)))-1)
#     i+=1
# print(b)


# a="my name is tanu"
# print((a.split()))

# a=[1,2,3,4,5]
# b="smile"
# i=0
# c=[]
# while i<len(a):
#     # if i%2!=0:
#     #     c.append(a[i])
#     #     c.append(b[i])
#     # else:
#     c.append(a[i])
#     c.append(b[i])
#     i+=1
# print(c)

# a=["navgurukul","pune"]
# b=[]
# i=0
# while i<len(a):
#     c=a[i]
#     rev=c[::-1]
#     print(rev)
#     revitem=[]
#     j=0
#     while j<len(rev):
#         revitem.append(rev[i])
#         j+=1
#     b.append(revitem)
#     i+=1
# print(b)

# a="navgurukul"
# b=[]
# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])
# print(b)
# c=[]
# for i in range(len(b)):
#     c.append(a[i])
# print(c)
# if b==c:
#     print("pal")
# else:
#     print("not")




# a="nav"
# i=0
# b=""
# while i<len(a):
#     b+=a[i]
#     j=1
#     b1=""
#     while j<=len(a):
#         b1+=a[-j]
#         j+=1
#     print(b1)
#     i+=1
# if b==b1:
#     print("P")
# else:
#     print("N")

# a=["navgurukul","pune"]
# i=0
# b=[]
# while i<len(a):
#     c=(a[i])[::-1]
#     b.append(c)
#     i+=1
# print(b)
# d=[]
# i=0
# while i<len(b):
#     j=0
#     while j<len(b[i]):
#         d.append(b[i][j])
#         j+=1
    
#     i+=1
# print(d)

# a=["navgurukul","pune"]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==str:
#       j=1
#       sum=""
#       while j<=len(a[i]):
#         sum=sum+a[i][-j]
#         j=j+1
#     i=i+1
# print(b)
            

# a="navgurukul is small in pune"
# b=a[ :3]
# b1=a[3:6]
# b2=a[7:10]
# b3=a[11:13]
# b4=a[20:22]
# b5=a[23: ]
# print(b,b1,"\n",b2,b3,"\n",b4,b5)


# a1="3+5j"
# a1=complex(a1)
# b=21.4
# b=int(b)
# c="divya"
# d="14.5"
# d=float(d)
# d=int(d)
# a=c
# b=(b+d+a1)
# b=str(b)
# print(a+b)


# a=[50,40,23,70,56,12,5,10,7]
# i=0
# mx=0
# mx2=0
# while i<len(a):
#     if a[i]>mx:
#         mx=a[i]
#     i+=1
# print(mx)
# i=0
# while i<len(a):
#     if a[i]>mx2 and a[i]!=mx:
#         mx2=a[i]
#     i+=1
# print(mx2)\



# a=input("intr:-")
# i=0
# b="aeiou"
# c=0
# while i<len(a):
#     if a[i] in b :
#         c+=1
#         # print(a[i])
#     if c==1:
#         print(a[i])
#     i+=1