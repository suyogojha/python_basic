eng = int(input("enter your english marks: "))
nep = int(input("enter your nepali marks: "))
math = int(input("enter your math marks: "))

total_marks = eng + nep + math


percentage = total_marks / 3
print("Your total marks is: ", total_marks)

print("your percentage is: \n", percentage)
    

if percentage>=91 and percentage<=100:
    print("Your Grade is A1")
elif percentage>=81 and percentage<91:
    print("Your Grade is A2")
elif percentage>=71 and percentage<81:
    print("Your Grade is B1")
elif percentage>=61 and percentage<71:
    print("Your Grade is B2")
else: 
    print("fail")