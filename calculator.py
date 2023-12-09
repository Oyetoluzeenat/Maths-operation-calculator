"""
ZIYTECHS CALCULATOR PROGRAM
	Welcome the user
	Inform the user about the available mathematical operations
	List the available operations (Addition, Subtraction, Multiplication, Division, Square, square root, Exit program (Alert, are you sure you want to exit this program?))
	Ask the user the kind of operation they intend to perform and take their response
	Convert the response to float, and save the response in a variable.
	Handle user input errors
	Request for the numbers intended for mathematical operation (num1, num2)
	Handle user input errors
	Save the responses in a variable
	Write a function to perform the operations and display the results. Comment on the function of each function.
	For the division function, check for zero denominator error. You can’t perform divide by zero operation. Use conditional statement to handle zero input for denominator.
	Print the result
	Thank the user  
	Request if the user intends to perform another operation (If yes, rerun the program, if no Terminate the program safely)
	Exit the program

Note: Use line breaks and comments where necessary.

"""
import math

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
    return result

def subtract():     #This function subtract two numbers. 
    num1 = eval(input("Enter the first number --> "))
    num2 = eval(input("Enter the second number --> "))
    result = num1-num2
    print("\nHurray! ",num1, "-" ,num2 ,"=", result, "\n")  
    return result

def multiply():     #This function multiplies two numbers. 
    num1 = eval(input("Enter the first number --> "))
    num2 = eval(input("Enter the second number --> "))
    result = num1*num2
    print("\nHurray! ",num1, "X" ,num2 ,"=", result, "\n")  
    return result

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
    return result

def power():     #This function compute the exponent of a number. 
    base = eval(input("Enter the base number --> "))
    exponent = eval(input("Enter the exponent ----> "))
    result = pow(base, exponent)
    print("\nHurray! ",base, "^" ,exponent,"=", result, "\n")  
    return result

def square_root():     #This function compute the square root of a number. 
    num = eval(input("Enter the number --> "))
    result = round(math.sqrt(num),3)
    print("\nHurray! ", "The square root of ", num ,"=", result, "\n")  
    return result


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

"""
AREA_OF_IMPROVEMENTS
    Instead of running the program over and over without the user's consent. FIXED

    it will be better to ask the user if they will like to perform another transaction before running it again FIXED

    If an invalid option is entered into the first question, the program should request for a correct option, it should not proceed. FIXED

    The "carry_on" function run once, I will like to keep asking "if the user will like to perform another operation after each operation", 
    if yes, the program should run, if No, the program should terminate. FIXED
    

    Fix the division error, and complete the function for square root FIXED

    I am still trying to figure out how to integrate the power and square opration into the calculator.  FIXED 

NOTES  
    A converted string case does not work in "IF" statement. So i have to use "Y" or "y", "N" or "N"
   
    There is a limit for exponential value in Python. If you input a value that exceeds 4300, the program will return a "ValueError". It also recommends a solution. ValueError: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
    
    It does not multiply numbers that begin with zero. It thrown back a syntax error. 
         SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
   
"""
