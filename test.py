# number=int(input("Enter a number\n"))
# if number>0:
#     print("positive number")
#     if number%2==0:
#         print("even number")
#     else:
#         print("odd number")
# elif number<0:
#     print("negative number")
# else:
#     print("zero")
# bank_balance=int(input("enter Available balance\n"))
# withdraw=int(input("Enter withdrawal amount\n"))
# if bank_balance>withdraw:
#     print(f'your amount of rs {withdraw} has been withdrwan from your account')
#     print("available balane is = ", bank_balance-withdraw)
# else:
#     print("insufficient balance")
# subjects=["Maths", "Science", "Hindi", "English", "Social science"]
# marks=[]
# for subject in subjects:
#     score=int(input(f'enter marks in {subject} \n'))
#     marks.append(score)

# total_marks=sum(marks)
# percentage=(total_marks/(len(subjects)*100))*100
# if percentage >=65:
#     print("grade 'A'", percentage)
# elif percentage >=50 and percentage<65:
#     print("grade 'B'", percentage)
# elif percentage>=33 and percentage<50:
#     print("grade 'C'", percentage)
# else:
#     print("fail", percentage)

# n=int(input("enter how many pairs you want to enter\n"))
# pairs=()
# for i in range(n):
#     key=input(f'Enter {i+1} key\n')
#     value=input(f'Enter {i+1} value\n')
#     if value.isdigit():
#         value=int(value)
    
#     pairs.append((key,value))

# dictonary=dict(pairs)
# print("tuple is")
# print("new dictionary is ", dictonary)
# username="chai aur code"
# def func():
#     #username="code"
#     print(username)

# print(username)
# func()
# x=88

# def func(b):
#     c=x+b
#     return c

# print(func(2))
# def power(num):
#     def actual(x):
#         return x**num
#     return actual
# a=power(2)
# b=power(3)
# print(a(5))
# print(b(5))
# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i



# a=even_generator(10)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
#  print(id(a))
#  print(id(a))
#  print(id(a))

# print(next(even_generator(10)))
# print(next(even_generator(10)))
# print(next(even_generator(10)))
# def factorial(num):
#     factorial=1
#     for i in range(1,num+1):
#         factorial=factorial*i
#     return factorial
    

# fac=factorial(5)
# print(fac)
# def perfect(num):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#          sum=sum+i

#     if sum==num:
#        print("perfect number")
#     else:
#        print("not perfect")




# # perfect(6)
# def armstrong(num):
#     sum=count=0
#     original= new=num

#     while num>0:
#         count=count+1
#         num=num//10
#     while new >0:
#         digit=new%10
#         sum=sum+digit**count
#         new=new//10

#     if sum==original:
#         print( "armstrong number")
#     else:
#         print ("not armstrrong")


# arm=armstrong(370)
# print(arm)
        
# def prime(number):
#     count=0
#     for i in range(1,number+1):
#         if number%i==0:
#             count=count+1
#     if count==2:
#         print("prime number")
#     else:
#         print("not prime")

# p=prime(13)
# n=int(input("enter how many pairs you want to write\n"))
# list=[]
# for i in range(1,n+1):
#     key=input(f'enter {i} no key\n')
#     value=input(f'Enter {i} value\n')
#     if value.isdigit():
#         value=int(value)
#     list.append((key,value))

# dictnory=dict(list)
# print(f'converted dictonary is {dictnory}')
# n=int(input("enter number of rows in pyramid"))
# for i in range(1,n+1):
#     print(' '*(n-i)+' *' *i)
# n = int(input("Enter number of rows in pyramid: "))

# for i in range(1, n + 1):
#     spaces = ' ' * (n - i)

#     if i == 1:
#         print(spaces + ' *')
#     elif i == n:
#         print(' *' * n)
#     else:
#         print(spaces + ' *' + '  ' * (i - 2) + ' *')
# t=int(input("enter number of key and value\n"))
# pairs=()
# for i in range(1,t+1):
#     key=input(f'enter {i} key\n')
#     value=input(f'enter {i} value\n')
#     if value.isdigit():
#         value=int(value)
#     pairs=pairs+((key,value),)
# dictionary=dict(pairs)
# print(f'new dictionary is {dictionary}')
# print(type(pairs))
# i=1
# while i<=3000:
#     if i%100==0:
#         print(i)
#     else:
#         pass
#     i=i+1
# for i in range(1,3001):
#     if i%100==0:
#         print(i)
#     else:
#         pass
# l=[2,4,6,8,10,12,14,16,18,20]
# inp=int(input("enter how many numbers you want to enter\n"))
# l=[]
# for i in range(1,inp+1):
#     num=int(input(f'enter no {i} number\n'))
#     l.append(num)

    
# print(sum(l))
# n=int(input('enter till how many numbers you want fibonaci series'))
# a=0
# b=1
# i=1
# while i<=n:
#     print(a)
#     c=a+b
#     a=b
#     b=c
#     i=i+1
# n=int(input('enter till how many numbers you want fibonaci series'))
# a=0
# b=1
# while a<=n:
#     print(a)
#     c=a+b
#     a=b
#     b=c
# num=int(input("enter a number to find factorial"))
# factorial=1
# i=1
# while i<=num:
#     factorial=factorial*i
#     i=i+1

# print(factorial)
# count=0
# for i in range(1,21):
#     if i%2==0:
#         count=count+1
#         print(i,"is even number and no of count is = ", count)
#     else:
#         pass
# for i in range(50,61):
#     if i%3==0:
#         continue
#     else:
#         print(i,"is not divisible by 3")
# a=int(input("enter 1 number"))
# b=int(input("enter 1 number"))
# c=int(input("enter 1 number"))
# if a>b and a>c:
#     print(a,"is greater")
# elif b>a and b>c:
#     print(b, "is greater")
# else:
#     print(c, "is greater")
# n=int(input("enter how many terms you want to print"))
# a=0
# b=1
# i=1
# while i<=n:
#     print(a)
#     c=a+b
#     a=b
#     b=c
 
#     i=i+1



        

  






    
   








