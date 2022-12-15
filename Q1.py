

# class Vehicle:
#     def __init__(self,mileage,cost):
#         self.mileage=mileage
#         self.cost=cost
#     def show_details(self):
#         print("i am a vehicle")
#         print("mileage of vehicle is ",self.mileage)
#         print("cost of vehicle is ",self.cost)
# v1=Vehicle(500,500)
# v1.show_details()

# class car(Vehicle):
#     def show_car(self):
#         print("i am car")
# c1=car(200,1200)
# c1.show_details()
# # c1.show_car()


# class Employee:
#     def __init__(self,name,age,salary,gender):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.gender=gender
#     def employee(self):
#         print("name of employee is :-",self.name)
#         print("Age of employee is :-",self.age)
#         print("salary of employee is :-",self.salary)
#         print("gender of employe is :-",self.gender)
# e1=Employee("tanu",17,35000,"female")
# # e1.__init__() :- type error  thier is a four arguments
# e1.employee() 


# class phone:
#     def make_call(self):
#         print("making calls")
#     def play_game(self):
#         print("playing games")
# p1=phone()
# p1.make_call()
# p1.play_game()



# class data:
#     def student_data(self):
#         print("tanu")
#     def show_color(self):
#         print("dance")
# p1=data()
# p1.student_data()
# p1.show_color()


# a=[{"fname":'tanu','lastname':"khose","age":32},
#     {"fname":'shivani','lastname':"singh","age":30},
#     {"fname":'arti','lastname':"gupta","age":32}]
# f=list(filter(a[1]))
# print(f)

# a='navgurukul'
# print('123a')


# i=1
# b=[]
# while i<=100:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==2:
#         b.append(i)
#     i+=1
# print(b)



# i=0
# while i<10:
#     i+=1
#     if i==5:
#         continue
#     elif i==8:
#         pass
#     elif i==9:
#         break
#     print(i)
#     # i+=1


# parsentage 


# t=500 #total
# a=175 #apesent
# y=t-a #total - apesent
# p=y/t*100 #present / total * 100
# print(p)

# a=4+5
# print(a)


# a=int(input("enter the number:-"))
# i=1
# while i<=a:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==2:
#         print(i)
#     i+=1


# a='nikita'
# b=5
# c=[]
# i=0
# while i<len(a):
#     c.append(a[i])
#     c.append(b)
#     b+=5
#     i+=1
# print(c)




# a=int(input("enter the number:-"))
# i=1
# while i<=a:
#     if i%2==0:
#         print(i)
#     i+=1


# i=5
# while i>0:
#     j=0
#     while j<i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i-=1                                                                


# i=0
# while i<10:
#     i+=1
#     if i==4:
#         pass        
#     elif i==7:
#         continue
#     elif i==9:
#         break
#     print(i)

# a='navgurukul'
# b=len(a)
# print(b)

# a='python'
# i=0
# while i<len(a):
#     j=0
#     while j<=(i):
#         print(a[j],end="")
#         j+=1
#     print()
#     i+=1

# i=0
# while i<5:
#     j=0
#     while j<5:
#         if i==0:
#             print("*",end=" ")
#         else:
#             if j==2:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         j+=1
#     print()
#     i+=1


# a=int(input("enter the number "))
# i=0
# sum=0
# k=a
# while a>0:
#     i=a%10
#     sum+=i
#     a//=10
# if k%sum==0:
#     print("harshad numbre")
# else:
#     print("not")


# b= "45My 45Name 56Is 87Priyanka 78Dangwal"
# s=b.split()
# p=[]
# for i in range(len(s)):
#     s[i]=str(s[i])
#     for j in range(len(s[i])):
#         p.append(s[i][2: ])
#     k=0
#     list1=[]
#     while k<len(p):
#         if p[k] not in list1:
#             list1.append(p[k])
#         k+=1
# print(list1)



# a=121
# sum=0
# num=0
# i=1
# while i>=a:
#     rev=sum=(rev%10)*(rev%10)*(rev%10)
#     i=i//10
# if a%10:
#     print("palindrome")
# else:
#     print("not")


# a=input("enter the :-")
# i=0
# b=""
# while i<len(a):
#     b+=a[i]
#     j=1
#     b1=""
#     while j<=len(a):
#         b1+=a[-j]
#         j+=1
#     i+=1
# if b==b1:
#     print("P")
# else:
#     print("N")


# a="nitin"
# b=a[::-1]
# c=a[0: ]
# # print(b)
# # print(c)
# if b==c:
#     print("P")
# else:
#     print("N")


# a="tanu"
# print(a*5)


# a=[1,2,3,4,5]
# a.append(7)
# print(a)


# a=[1,2,3,4,5]
# a.clear()
# print(a)


# a=['t','a','n','u']
# i=0
# while i<len(a):
#     # print(a)
#     print(a[i])
#     # print(i)
#     i+=1

# a=int(input("enterthe number:-"))
# b=a//10
# if b%10:
#     print("s",b%10)
# else:
#     print('n')


# def nav(a,b):
#     c=a+b
#     return c
# print(nav(1,2))

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# a=fact(5)
# print(a)


# a=True
# print(a)

# def fname():
#     print("hello")
# fname()



# a=True
# b=False
# print(a or b)

# print(5(2 and 6))

i=1
a=int(input("enter"))
while i<=a:
    if a%i==0:
        print(i)
    i+=1

