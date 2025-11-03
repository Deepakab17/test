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
subjects=["Maths", "Science", "Hindi", "English", "Social science"]
marks=[]
for subject in subjects:
    score=int(input(f'enter marks in {subject} \n'))
    marks.append(score)

total_marks=sum(marks)
percentage=(total_marks/(len(subjects)*100))*100
if percentage >=65:
    print("grade 'A'", percentage)
elif percentage >=50 and percentage<65:
    print("grade 'B'", percentage)
elif percentage>=33 and percentage<50:
    print("grade 'C'", percentage)
else:
    print("fail", percentage)

    