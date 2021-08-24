def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1

def multiply_numbers(num1, num2):
    return num1 * num2

def div_numbers(num1, num2):
    if num1 > num2:
        return num1 / num2
    else:
        return num2 / num1

print("-----------------Welcome to the simple calculator design******************")
a = int(input("enter first number: "))
b = int(input("enter second number: "))

for i in range(5):
    choice = int(input("""
                    Enter your choice
                    1.Add
                    2.Subtract
                    3.Multiply
                    4.Divide
                    5.Exit\n"""))

    if choice == 1:
            _sum = add_numbers(a, b)
            print(f"The sum of {a} and {b} is: ", _sum)
            
    elif choice == 2:
            sub = subtract_numbers(a, b)
            print(f"The subtraction of {a} and {b} is: ", sub)
            
    elif choice == 3:
            mul = multiply_numbers(a, b)
            print(f"The Multiplication of {a} and {b} is: ", mul)
            
    elif choice == 4:
            div = div_numbers(a, b)
            print(f"The Division of {a} and {b} is: ", div)
            
    elif choice == 5:
            print("you have exited the program")
            break
else:
        print("sorry you select wrong number!!!")