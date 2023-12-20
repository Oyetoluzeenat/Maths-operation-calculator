from math import sqrt

print ("\n****************  WELCOME TO ZIYTECHS CALCULATOR  **************** \n\n")
print("Here are some mathematical operations you can perform: \n")

def operation():
    print("press 1 for Addition") 
    print("press 2 for Subtraction") 
    print("press 3 for Multiplication") 
    print("press 4 for Division")
    print("press 5 for power")
    print("press 6 for Square root")
operation()

def add():     #This function adds two numbers. 
    num1 = eval(input("Enter the first number --> "))
    num2 = eval(input("Enter the second number --> "))
    result = num1+num2
    print("\nHurray! ",num1, "+" ,num2 ,"=", num1+num2, "\n")  

def subtract():     #This function subtract two numbers. 
    num1 = eval(input("Enter the first number --> "))
    num2 = eval(input("Enter the second number --> "))
    result = num1-num2
    print("\nHurray! ",num1, "-" ,num2 ,"=", result, "\n")  

def multiply():     #This function multiplies two numbers. 
    num1 = eval(input("Enter the first number --> "))
    num2 = eval(input("Enter the second number --> "))
    result = num1*num2
    print("\nHurray! ",num1, "X" ,num2 ,"=", result, "\n")  

def divide():     #This function divides numerator by non-zero denominator. 
    try:
        num1 = eval(input("Enter the first number --> "))    #numerator
        num2 = eval(input("Enter the second number --> "))   #denominator
        result = round(num1/num2,3)
    except ZeroDivisionError:
        print("\nCan't divide by zero, second number must be greater than zero \n\nPlease try again!\n")
        divide()
    else:
        print("\nHurray! ",num1, "/" ,num2 ,"=", result, "\n")  

def power():     #This function compute the exponent of a number. 
    base = eval(input("Enter the base number --> "))
    exponent = eval(input("Enter the exponent ----> "))
    result = pow(base, exponent)
    print("\nHurray! ",base, "^" ,exponent,"=", result, "\n")  

def square_root():     #This function compute the square root of a number. 
    num = eval(input("Enter the number --> "))
    result = round(sqrt(num),3)
    print("\nHurray! ", "The square root of ", num ,"=", result, "\n")  

def maths_operation(): #Validate input and call the appropriate function to compute output
    option= str(input("\nWhat mathematical operation would you like to perform? ---> "))
    if option =="1":
       add() 
    elif option == "2":
       subtract()
    elif option == "3":
        multiply()
    elif option == "4":
        divide()
    elif option == "5":
        power()
    elif option == "6":
        square_root()
    else:
        print("\nInvalid choice, Please try again! \n")
        operation()
        maths_operation()

maths_operation()  

while True:
    def carry_on():
        choice = input("\nWill you like to perform another mathematical operation? \n\npress Y for Yes \npress N for No  \n\n --->")
        if choice == "Y" or choice == "y":
            operation()
            maths_operation()
        elif choice == "N" or choice == "n":
            print("\nThank you for using ZIYTECHS Program. \n")
            exit()
        else: 
            print("\nInvalid choice, Please try again! \n")
            carry_on()

    carry_on()