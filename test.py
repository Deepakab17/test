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
def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i



a=even_generator(10)
b=even_generator(10)
c=even_generator(10)

print(id(a))
print(id(b))
print(id(c))

# print(id(even_generator(10)))
# print(id(even_generator(10)))
# print(id(even_generator(10)))


